#ifndef __SNAPPYDEF__
#define __SNAPPYDEF__
#include <maya/MPlug.h>
#include <maya/MDataBlock.h>
#include <maya/MPxDeformerNode.h>
#include <maya/MGlobal.h>


class snapDeformer: public MPxDeformerNode {
public:
    snapDeformer() {};

    virtual ~snapDeformer() {};

    static void    *creator();

    static MStatus	initialize();

    virtual MStatus deform(MDataBlock &data, MItGeometry &iter, const MMatrix &mat, unsigned int multiIndex);

    static MTypeId id;
    static MObject weight;
    static MObject space;
    static MObject spaceSource;
    static MObject pointList;
    static MObject snapMesh;
};


#endif
