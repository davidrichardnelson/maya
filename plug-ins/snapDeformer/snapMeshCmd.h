#include <maya/MGlobal.h>
#include <maya/MStatus.h>
#include <maya/MPxCommand.h>
#include <maya/MArgList.h>

// MAIN CLASS DECLARATION FOR THE MEL COMMAND:
class snapMeshCmd : public MPxCommand {
public:
    snapMeshCmd(){};
    virtual ~snapMeshCmd() {};
    static void* creator();
    bool isUndoable() const;
    MStatus doIt(const MArgList&);
    MStatus redoIt( );
    MStatus undoIt( );
    MObject createSnapMesh(const MDagPath &source,
                            const MDagPath &target,
                            float maxDist, MStatus *stat);
private:
    MObject newDeformer;
    MArgList Args;

};


inline MStatus Usage(MStatus status) {
    MGlobal::displayInfo("usage:  snapMeshCmd -s source -t target -max 1");
    return status;
}
