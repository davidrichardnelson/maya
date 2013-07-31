/*
 * 
 *  main.cpp
 *  
 * standard initialization procedures
 *  Created on: may 24, 2010
 *      Author: katrin.schmid
*/

#include <maya/MFnPlugin.h>
#include "smDef.h"


MStatus initializePlugin( MObject obj )
{
    MStatus result;
    MFnPlugin plugin( obj, "www.lo-motion.de", "3.0", "Any");
    result = plugin.registerNode( "smoothDeform", smoothDeformer::id, smoothDeformer::creator, 
                                                                  smoothDeformer::initialize, MPxNode::kDeformerNode );

    return result;
}

MStatus uninitializePlugin( MObject obj)
{
    MStatus result;
    MFnPlugin plugin( obj );
    result = plugin.deregisterNode( smoothDeformer::id );
    
    return result;
}