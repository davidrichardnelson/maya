/** \defgroup Cellnoise
 * @file
 * @author  katrin schmid <info@lo-motion.de>
 * @version 0.2.0
 *
 * 
 * @section DESCRIPTION
 * \brief 
 * A smooth deformer that averages vertices based on a paintable vertex weights.
 * Option to keep border edges at position.
 *
 * To install: copy to maya bin\plugins directory or anywhere in plugin path
 * Create by "deformer -type smoothDeform" mel, paint bvetrex attributes in 
 * Modify > Paint attributes tool. 
 
 *
 * */


#ifdef debug
#undef debug
#endif
//#define debug


#define MAKE_INPUT(attr)                                                \
    CHECK_MSTATUS( attr.setKeyable(true) );     \
        CHECK_MSTATUS( attr.setStorable(true) );        \
    CHECK_MSTATUS( attr.setReadable(true) );    \
        CHECK_MSTATUS( attr.setWritable(true) );


#define McheckErr(stat,msg)             \
        if ( MS::kSuccess != stat ) {   \
                cerr << msg;                            \
                return MS::kFailure;            \
        }


#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MGlobal.h>

#include <maya/MFnDependencyNode.h>
#include <maya/MItDependencyGraph.h>
#include <maya/MObject.h>
#include <maya/MDagPath.h>
#include <maya/MIOStream.h>
#include <maya/MGlobal.h>
#include <maya/MIOStream.h>
#include <maya/MTypeId.h> 
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnTypedAttribute.h>

#include <maya/MItMeshVertex.h>
#include <maya/MItMeshPolygon.h>
#include <maya/MFnMesh.h>
#include <maya/MPoint.h>
#include <maya/MVector.h>
#include <maya/MPointArray.h>
#include <maya/MItGeometry.h>
#include <maya/MFnDependencyNode.h>

#include <vector>
#include <math.h>

#include "smDef.h"

MTypeId smoothDeformer::id( 0x8123c );
MObject smoothDeformer::aScale;
MObject smoothDeformer::aIterations;
MObject smoothDeformer::aKeepBorder;  

void getAverageVector(std::vector <MVector> directionVectors, int neighboursSize, float &avX, float &avY, float &avZ)
{
    avX = avY =avZ=0.f;// Todo: make this a vector
    for (int y=0; y< directionVectors.size(); y++)
    {
        avX += directionVectors[y].x;
        avY += directionVectors[y].y;
        avZ += directionVectors[y].z;
    }

    avX = avX / float (neighboursSize);
    avY = avY / float (neighboursSize);
    avZ = avZ / float (neighboursSize);
}

   
smoothDeformer::smoothDeformer() 
{}

smoothDeformer::~smoothDeformer()
{}

void* smoothDeformer::creator()
{
    return new smoothDeformer();
}


MStatus smoothDeformer::initialize()
{
    MFnNumericAttribute nAttr;
    aScale=nAttr.create( "scale", "sc", MFnNumericData::kDouble );
    nAttr.setDefault(1.);
    nAttr.setMin(-10.0),
    nAttr.setMax(10.0),
    nAttr.setKeyable(true);
    addAttribute( aScale); 
                
    aIterations=nAttr.create( "smoothIterations", "its", MFnNumericData::kInt );
    MAKE_INPUT(nAttr);
    nAttr.setDefault(0);
    nAttr.setKeyable(true);
    addAttribute( aIterations);
   
    aKeepBorder=nAttr.create( "keepBorders", "kbe", MFnNumericData::kBoolean, true);
    MAKE_INPUT(nAttr);
    nAttr.setDefault(1);
    nAttr.setKeyable(true);
    addAttribute( aKeepBorder);
        
    attributeAffects( smoothDeformer::aKeepBorder, smoothDeformer::outputGeom );
    attributeAffects( smoothDeformer::aScale, smoothDeformer::outputGeom );
    attributeAffects( smoothDeformer::aIterations, smoothDeformer::outputGeom);

    MGlobal::executeCommand( "makePaintable -attrType multiFloat -sm deformer smoothDeform weights;" );

    return MS::kSuccess;
}

// Description:   Deform the point with a smoothDeformer algorithm
//  iter  : an iterator for the geometry to be deformed
//  m     : matrix to transform the point into world space
//  multiIndex : the index of the geometry that we are deformin
MStatus smoothDeformer::deform( MDataBlock& block, MItGeometry& iter, const MMatrix& m, unsigned int multiIndex)
{
    MStatus status = MS::kSuccess;

    MObject node = this->thisMObject();
    
    float vLength, defMulti, w, moveToX, moveToY, moveToZ, minLength = 1316134912;
    float avLength, avX, avY,avZ, maxLength =0;
    MVector pos, diffVec;
    MPoint condPointPos, objPos;                                            
    MPointArray pointArray, outPoints;                          
    MIntArray condPoints;
    std::vector <MVector> directionVectors;
    std::vector <float>   vWeights; 
    MObject geoData;

    MDataHandle envData = block.inputValue(envelope,&status);   
    McheckErr(status, "Error getting envelope data handle\n");      
        
        MPlug ip_plug(node, aScale);  
    float scaleV = ip_plug.asFloat();  
    MPlug kb_plug(node, aKeepBorder);  
    bool keepBorder = kb_plug.asBool(); 

    MFnDependencyNode fnDependNode( node );
    // Assign the '.inMesh' tPlug from the mesh node.
    MPlug inMeshPlug = fnDependNode.findPlug( "outputGeometry" );//arrayPlug
    MPlug it_plug(node, aIterations);   
    int smoothIterations=it_plug.asInt();

    // Get the envelope and blend weight
    float env = block.inputValue( envelope ).asFloat();

    MArrayDataHandle cpHandle= block.outputArrayValue(inMeshPlug);
    cpHandle.jumpToElement(multiIndex);
    MDataHandle pntHandle = cpHandle.outputValue();
    geoData=pntHandle.data();
    if (geoData.isNull())
        return status;

    MItMeshPolygon mMeshPolygon(geoData, &status);
    MFnDependencyNode fnDep (geoData);  
    MFnMesh meshFn(geoData);
    MItMeshVertex iterMesh(geoData) ;//! Mesh iterator, over origMeshData

    if (env > 0)
    {
        int pointCount=iterMesh.count();
        for (int z=0 ; z < smoothIterations ; z++ )
        { 
            meshFn.getPoints (pointArray, MSpace::kObject);     
            iterMesh.reset();
            
            // loop points
            for (int g=0 ; g < pointCount; g++ )
            {
                objPos = pointArray[g];
                //objPos = iterMesh.position(MSpace::kObject);      
                if (z==0)
                {
                    if (keepBorder==1 && iterMesh.onBoundary(&status)==1)
                        w=0.0;
                    else
                        w = (weightValue( block, multiIndex, g))*env;

                    vWeights.push_back(w);
#ifdef debug
                   std::cout <<g<<" w: " << vWeights[g] <<" "<<iterMesh.onBoundary(&status) <<" " << keepBorder<<std::endl;
#endif
                }               
                else
                    w=vWeights[g];
#ifdef debug
                std::cout <<g<<" w: " <<w<< " "<<(w<=0.001)<<std::endl;
#endif
        
                if (w<0.001)// clamp weights
                    outPoints.append( objPos);
                else
                {
                    condPoints.clear();
                    directionVectors.clear();
                    iterMesh.getConnectedVertices(condPoints);//indices of the vertices surrounding the current vertex
                    avLength =0.f;
                    
                    for (int i=0; i<condPoints.length();i++)
                    {
                        condPointPos =pointArray[condPoints[i]];
                        diffVec=MVector(objPos -condPointPos);
                        directionVectors.push_back(diffVec );// direction
                        vLength= diffVec.length();
                        avLength+=vLength;
                        
                        // check min-max length vectors
                        if (vLength < minLength )
                            minLength = vLength ;
                        if (vLength > maxLength )
                            maxLength = vLength;
                    }

                    getAverageVector(directionVectors, condPoints.length(), avX, avY, avZ);
                    // get average length
                    avLength = float (avLength) / float (condPoints.length());
        
                    if (scaleV <= 0)
                    {
                        defMulti = minLength + (avLength - minLength);
                        if (defMulti != 0)
                            defMulti = scaleV*w/10 *defMulti / avLength;
                    }
                    else if (scaleV > 0)
                    {
                        defMulti = avLength + ( maxLength - avLength );
                        if (defMulti != 0)
                            defMulti = scaleV*w/10 * defMulti/avLength;
                    }
#ifdef debug
                    std::cout << defMulti << " : "<<minLength<<scaleV <<" defMulti " <<  avLength <<" : "<< maxLength<<std::endl;
#endif

                    moveToX = objPos[0]-(avX *defMulti/(z+1)*w);
                    moveToY = objPos[1]-(avY*defMulti/(z+1)*w);
                    moveToZ = objPos[2]-(avZ*defMulti/(z+1)*w);
                    outPoints.append( MPoint(moveToX, moveToY, moveToZ));
                }
                iterMesh.next() ;                       
            }//point loop
        
            if (outPoints.length()== pointArray.length())
            {
                //if (z >= smoothIterations-1)
                status=iter.setAllPositions(outPoints, MSpace::kObject);
                pointArray.clear();
                outPoints.clear();
            }
        }//iterations
    }

    return status;
}