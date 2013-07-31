//register the node with maya

#include <maya/MFnPlugin.h>
#include "snapMeshDeformer.h"
#include "snapMeshCmd.h"

MStatus initializePlugin( MObject obj ) {

	MString vendorStr( "" );
	vendorStr += __DATE__;
	vendorStr += " @ ";
	vendorStr += __TIME__;

	MFnPlugin plugin( obj, vendorStr.asChar(), "1.0", "Any");
	MStatus result;
	result = plugin.registerNode( "snapMeshDeformer", snapDeformer::id, snapDeformer::creator, 
								  snapDeformer::initialize, MPxNode::kDeformerNode );

	if (result)result = plugin.registerCommand("snapMeshCmd", snapMeshCmd::creator);

    MGlobal:: displayInfo("snapMeshCmd -s source -t target -max 1");
	MGlobal:: displayInfo("snapDeformer plugin loaded (see script editor for details).");
	MGlobal:: displayInfo( vendorStr.asChar() );
   
	return result;
}

MStatus uninitializePlugin( MObject obj) {
	MStatus result;
	MFnPlugin plugin( obj );
	result = plugin.deregisterNode( snapDeformer::id );
    if (result)result = plugin.deregisterCommand("snapMeshCmd");
	return result;
}
