#ifndef __MAYA_FUN_TIONS
#define __MAYA_FUN_TIONS

#include <maya/MGlobal.h>
#include <maya/MArgList.h>

///quicky error message
inline MStatus Err(MStatus status, const std::string messsage)
{
    MGlobal::displayError(messsage.c_str());
    return status;
}

inline int getArgPosition(const MArgList &args, const std::string flag)
{
	unsigned argData = args.flagIndex(flag.c_str());
	if (argData == args.kInvalidArgIndex)
		return -1;
	int value(argData);
	return value;
}

#endif