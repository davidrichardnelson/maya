#include <maya/MSelectionList.h>
#include <maya/MDagPath.h>
#include <maya/MFnMesh.h>
#include <maya/MFnIntArrayData.h>
#include <maya/MPlug.h>
#include <mayaFuntions.h>
#include <KdTreeMaya.h>

#include "snapMeshCmd.h"

void* snapMeshCmd::creator() {
   return new snapMeshCmd;
}

bool snapMeshCmd::isUndoable() const {
   return true;
}

MStatus snapMeshCmd::doIt(const MArgList& args) {
    Args = args;
   	return redoIt();
}

MStatus snapMeshCmd::redoIt() {
    MStatus stat;
    const MArgList args = Args;
    //get source
    int pos = getArgPosition(args, "-s");
    if (pos == -1)
        return Usage(MStatus::kInvalidParameter);

    MSelectionList list;
    MDagPath source, target;
    MObject tempObject;
    list.add(args.asString(pos+1));
    stat = list.getDagPath(0,source,tempObject);
    if (!stat)
        return Err(stat, "can't get source object");

    //get target
    pos = getArgPosition(args, "-t");
    if (pos == -1)
        MGlobal::getActiveSelectionList(list);
    else
    {
        list.clear();
        list.add(args.asString(pos+1));
        stat = list.getDagPath(0,target,tempObject);
        if (!stat)
            return Err(stat, "can't get target object");
    }


    //max dist
    float maxDist = 1;
    pos = getArgPosition(args, "-max");
    if (pos != -1)
        maxDist = float(args.asDouble(pos+1));

    newDeformer = createSnapMesh(source,target,maxDist, &stat);
   	return stat;
}

MStatus snapMeshCmd::undoIt() {
    MStatus stat;
    MGlobal::deleteNode(newDeformer);
   	return stat;
}

MObject snapMeshCmd::createSnapMesh(const MDagPath &source,
                                    const MDagPath &target,
                                    const float maxDist, MStatus *stat) {
    //get soure mesh and create tree
    MObject deformer;
    MFnMesh sourceMesh(source);
    MPointArray sourcePoints;
    sourceMesh.getPoints(sourcePoints, MSpace::kWorld);
    KdTree_map<int> sourceKd = KdFromPointArray(sourcePoints);


    //get target mesh and compair to kd tree
    MPointArray targetPoints;
    MFnMesh targetMesh(target);
    targetMesh.getPoints(targetPoints, MSpace::kWorld);
    MIntArray indexResults;

    KdTree<int>* results;
    for (unsigned int i=0; i< targetPoints.length(); i++) {
        float pos[3] = {float(targetPoints[i].x), float(targetPoints[i].y), float(targetPoints[i].z)};
        results = new KdTree<int>[20];
        //MGlobal::displayInfo("making intersection");
        int pointsFound = sourceKd.closestPoints(results, pos, maxDist, 19);
        //MGlobal::displayInfo("made intersection");
        if (pointsFound>0)
            indexResults.append(*results[0].Info());
        else
            indexResults.append(-1);
    }

    delete[] results;

    //create deformer
    MStringArray resultString;
    MGlobal::selectByName(targetMesh.name(), MGlobal::kReplaceList);
    MGlobal::executeCommand("deformer -type snapMeshDeformer -name snapMeshDeformer", resultString);
    MSelectionList list;
    list.add(resultString[0]);
    list.getDependNode(0,deformer);
    MFnDependencyNode nodeDep(deformer);
    MDGModifier dgModifier;


    //connect souce to deformer
    MPlug snapMeshP = nodeDep.findPlug("snapMesh");
    MFnDependencyNode meshDep(sourceMesh.object());
	MPlug sourceMeshP = meshDep.findPlug("worldMesh");
    MStatus statA;
    MPlug sourceMeshPA = sourceMeshP.elementByPhysicalIndex(0, &statA);
    sourceMeshP.selectAncestorLogicalIndex(0,sourceMeshP.attribute());
    if (statA)
	    dgModifier.connect(sourceMeshPA, snapMeshP);
    else
        dgModifier.connect(sourceMeshP, snapMeshP);
    dgModifier.doIt();
    //write data to deformer
    MPlug pointsP = nodeDep.findPlug("pointList");
	MFnIntArrayData intArrayData;
	MObject	intArrayObject = intArrayData.create(indexResults);
	pointsP.setValue(intArrayObject);

    for (unsigned int i=0; i < indexResults.length(); i++) {
        pointsP.selectAncestorLogicalIndex(i,pointsP.attribute());
        pointsP.setValue(indexResults[i]);
    }


    return deformer;
}
