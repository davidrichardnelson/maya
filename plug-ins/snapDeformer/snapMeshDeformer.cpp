#include <maya/MFnMesh.h>
#include <maya/MMatrix.h>
#include <maya/MPointArray.h>
#include <maya/MItGeometry.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnTypedAttribute.h>
#include <mayaFuntions.h>
#include <KdTree.h>

#include "snapMeshDeformer.h"

MTypeId snapDeformer::id( 0x8000e );
MObject snapDeformer::weight; 
MObject snapDeformer::space;
MObject snapDeformer::spaceSource;
MObject snapDeformer::pointList;
MObject snapDeformer::snapMesh;

void *snapDeformer::creator() {
    return new snapDeformer;
}

MStatus snapDeformer::initialize() {
	MStatus stat;

    MFnNumericAttribute FnNumeric;
    MFnNumericAttribute FnNumericA;
    MFnTypedAttribute FnTyped;
    MFnEnumAttribute FnEnum;

	//weight
	weight = FnNumeric.create("weight", "we", MFnNumericData::kFloat);
	FnNumeric.setKeyable(true);
	FnNumeric.setStorable(true);
	FnNumeric.setReadable(true);
	FnNumeric.setWritable(true);
    FnNumeric.setDefault( 1.0 );
	addAttribute( weight );


    ///space target
	space = FnEnum.create("space", "sp", 0);
	FnEnum.addField("world",0);
	FnEnum.addField("object",1);
	FnEnum.setStorable(true);
	FnEnum.setKeyable(true);
	addAttribute(space);

    ///space source
	spaceSource = FnEnum.create("spaceSource", "sps", 0);
	FnEnum.addField("world",0);
	FnEnum.addField("object",1);
	FnEnum.setStorable(true);
	FnEnum.setKeyable(true);
	addAttribute(spaceSource);


	//pointlist
	pointList = FnNumericA.create("pointList", "pl", MFnNumericData::kInt);
	FnNumericA.setArray( true );
	FnNumericA.setKeyable(false);
	FnNumericA.setStorable(true);
	FnNumericA.setReadable(true);
	FnNumericA.setWritable(true);
    FnNumericA.setIndexMatters(true);
	addAttribute( pointList );


	//snapMesh
	snapMesh = FnTyped.create("snapMesh", "sm", MFnData::kMesh);
	FnTyped.setArray( false );
	FnTyped.setReadable(true);
	FnTyped.setWritable(true);
	addAttribute( snapMesh );



	attributeAffects(snapMesh, outputGeom);
	attributeAffects(pointList, outputGeom);
	attributeAffects(space, outputGeom);
    attributeAffects(spaceSource, outputGeom);
	attributeAffects(weight, outputGeom);

    return stat;
}

MStatus snapDeformer::deform(MDataBlock &data, MItGeometry &iter, const MMatrix &mat, unsigned int multiIndex) {
	MStatus stat;


    //lets see if we need to do anything
	MDataHandle DataHandle = data.inputValue(envelope, &stat);
	float env = DataHandle.asFloat();
	if (env == 0)
		return stat;
    DataHandle = data.inputValue(weight, &stat);
	const float weight = DataHandle.asFloat();
    if (weight == 0)
		return stat;
    
    env = (env*weight);


	//space target
	DataHandle = data.inputValue(space, &stat);
    int SpaceInt = DataHandle.asInt();

    //space source
	DataHandle = data.inputValue(spaceSource, &stat);
    int SpaceSourceInt = DataHandle.asInt();

    //pointlist
    MArrayDataHandle pointArrayHandle = data.inputArrayValue(pointList);


	//snapMesh
	MFnMesh	SnapMesh;
	DataHandle = data.inputValue(snapMesh, &stat);
    if (!stat)
        return Err(stat,"Can't get mesh to snap to");
    MObject SnapMeshObj = DataHandle.asMesh();
    SnapMesh.setObject(SnapMeshObj);
    MPointArray snapPoints;
    if (SpaceSourceInt==0)
        SnapMesh.getPoints(snapPoints, MSpace::kWorld);
    else
        SnapMesh.getPoints(snapPoints, MSpace::kObject);
    


    iter.reset();
    for ( ; !iter.isDone(); iter.next()) 	{
        //check for painted weights
        float currEnv = env * weightValue(data, multiIndex, iter.index());

        //get point to snap to
        unsigned int index;
        stat = pointArrayHandle.jumpToElement(iter.index());
        if (!stat)
            index = 0;
        else {
            DataHandle = pointArrayHandle.outputValue();
            index = DataHandle.asInt();
        }

        if (index != -1) {
            //calc point location
            MPoint currPoint;
            if (snapPoints.length() > index)
                currPoint = snapPoints[index];

            if (SpaceInt == 0)
                currPoint *= mat.inverse();

            if (currEnv !=1)
            {
                MPoint p = (currPoint- iter.position());
                currPoint = iter.position() + (p*currEnv);
            }


            //set point location
            iter.setPosition(currPoint);
        }
            
            
    }

    return stat;
}