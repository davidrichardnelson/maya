/*
 * smDef.h
 *
 *  Created on: may 24, 2009
 *      Author: katrin.schmid
*/

#ifndef smoothDeformer_H_
#define smoothDeformer_H_

#include <maya/MPxDeformerNode.h> 
#include <maya/MImage.h>
#include <maya/MColor.h>

/*! \class smoothDeformer 
* \brief defines deformation node
*
*/
class smoothDeformer : public MPxDeformerNode
{
public:
    smoothDeformer();
    virtual ~smoothDeformer();

    static  void*   creator();
    static  MStatus initialize();
    // deformation function
    virtual MStatus deform(MDataBlock&  block,
                         MItGeometry&   iter,
                         const MMatrix& mat,
                         unsigned int   multiIndex);
    static  MTypeId id;

private:
    // node attributes
    static MObject aScale;   
    static MObject aKeepBorder;  
    static MObject aIterations;         
    static MObject aUVMap;

};
#endif