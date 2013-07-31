// * standard initialization procedures
// File:          reg.cpp

///register the node with maya

#include <maya/MFnPlugin.h>
#include "intersectionDeformer.h"

MStatus initializePlugin( MObject obj ) {
    MString vendorStr( "" );
    vendorStr += __DATE__;
    vendorStr += " @ ";
    vendorStr += __TIME__;

    MFnPlugin plugin( obj, vendorStr.asChar(), "beta", "Any");
    MStatus result;
    result = plugin.registerNode( "intDeformer", intersectionDeformer::id, intersectionDeformer::creator, 
                                  intersectionDeformer::initialize, MPxNode::kDeformerNode );

    MGlobal:: displayInfo("intersectionDeformer plugin loaded (see script editor for details).");
    MGlobal:: displayInfo( vendorStr.asChar() );
   
    return result;
}

MStatus uninitializePlugin( MObject obj) {
    MStatus result;
    MFnPlugin plugin( obj );
    result = plugin.deregisterNode( intersectionDeformer::id );
    return result;
}
