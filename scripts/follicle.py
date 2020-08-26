"""
usage:

import follicle
import maya.cmds
reload(follicle)
x = follicle.folliclesFromSel(parent=True)

1) select transforms to attach
2) run follicle() method
3) parent the top resulting nul to anywhere in rig or constrain it so it follows rig

returns a list of dictionaries for each null attached
    [
        {
            'null'      : transform
            'nurbs'     : nurbs surface node
            'follicle'  : follicle shape node
            'transform' : follicle transform node
            'uv'        : uv data
                            {
                                'u'  : u               # U parameter
                                'v'  : v               # V parameter
                                'n'  : (n.x, n.y, n.z) # normal
                                'nu' : nu              # uniform U value (0-1)
                                'nv' : nv              # uniform V value (0-1)
                            }
        }
    ]

david@ventosum.com
"""

import maya.cmds
import maya.OpenMaya
import maya.api.OpenMaya

def getClostestUV(null, nurbs):
    """
    Given a null, what's the closest U V N values in coordinate and uniform space
    Borrowed some logic from this thread: http://www.soup-dev.com/forum.html?p=post%2Fclosestpointonsurface-node-in-maya-python-api-8005994
    """

    # check validity of args
    if not maya.cmds.objExists(null):
        return

    if not maya.cmds.objExists(nurbs):
        return

    if maya.cmds.nodeType(nurbs) != 'nurbsSurface':
        return

    # work around maya python api
    uu = maya.OpenMaya.MScriptUtil()
    pu = uu.createFromDouble(0.0)
    pu = uu.asDoublePtr()
    uv = maya.OpenMaya.MScriptUtil()
    pv = uv.createFromDouble(0.0)
    pv = uv.asDoublePtr()

    # get dag path to nurbs surface
    sl = maya.OpenMaya.MSelectionList()
    sl.add(nurbs)

    dp = maya.OpenMaya.MDagPath()
    sl.getDagPath(0, dp)

    fn = maya.OpenMaya.MFnNurbsSurface(dp)

    # get the closest point on surface to provided point
    mm = maya.cmds.xform( null, q=True, matrix=True, ws=True )
    p = maya.OpenMaya.MPoint(mm[12], mm[13], mm[14])
    cpos = fn.closestPoint(p)

    # get U and V parameters from the point on surface
    fn.getParamAtPoint(cpos, pu, pv)
    u = uu.getDouble(pu)
    v = uv.getDouble(pv)

    # get normal at U and V parameters
    n = fn.normal(u, v)

    # normalize U V to 0-1 for uniform values for nFollicles
    mxu = maya.cmds.getAttr(nurbs+'.mxu')
    mxv = maya.cmds.getAttr(nurbs+'.mxv')
    nu = u
    nv = v
    if u > 0:
        nu = u/mxu

    if v > 0:
        nv = v/mxv

    return {'u':u, 'v':v, 'n':(n.x, n.y, n.z), 'nu':nu, 'nv':nv}


def getWorldTransform (obj):
    """
    Return Matrix for worldpace coordinates of a transform null
    """
    return maya.api.OpenMaya.MMatrix ( maya.cmds.xform( obj, q=True, matrix=True, ws=True ) )


def createFollicle(nurbs, u=0.0, v=0.0):
    """
    Create a follicle for a nurbs surface given U and V. Duplicates can exist.
    """

    # check validity of args
    if not maya.cmds.objExists(nurbs):
        return

    if maya.cmds.nodeType(nurbs) != 'nurbsSurface':
        return

    # get nice xf path to nurbs
    name = maya.cmds.listRelatives(nurbs, p=True, pa=True, f=True)[0].split('|')[-1]

    # get number of existing follicle to nurbs
    fols = maya.cmds.listConnections(nurbs+'.local', d=True, s=False, p=False)
    if fols:
        num = str(len(fols))
    else:
        num = str(0)

    # create the follicle
    fol = maya.cmds.createNode('follicle', name=name+'_'+num.zfill(2)+'_follicle')
    maya.cmds.setAttr(fol+'.simulationMethod', 0) # static

    # name follicle xf
    xf = maya.cmds.listRelatives(fol, p=True)[0]
    xf = maya.cmds.rename( xf, name+'_'+num.zfill(2)+'_f')

    # hook up the nurbs and follicle
    maya.cmds.connectAttr( nurbs+'.local', fol+'.inputSurface', f=True)
    maya.cmds.connectAttr( nurbs+'.worldMatrix[0]', fol+'.inputWorldMatrix', f=True)
    maya.cmds.connectAttr( fol+'.outRotate', xf+'.r', f=True)
    maya.cmds.connectAttr( fol+'.outTranslate', xf+'.t', f=True)
    maya.cmds.setAttr( fol+'.parameterU', u)
    maya.cmds.setAttr( fol+'.parameterV', v)
    maya.cmds.setAttr( xf+'.t', l=True )
    maya.cmds.setAttr( xf+'.r', l=True )

    # return our follicle and its parent xf
    return {'follicle':fol, 'transform':xf}


def follicleFromNode(null, nurbs, parent=True):
    """
    Create an attachment of follicle for a null to a nurbs patch.
    """

    # check validity of args
    if not maya.cmds.objExists(nurbs):
        return

    if maya.cmds.nodeType(nurbs) != 'nurbsSurface':
        return

    # get the UV params
    uv = getClostestUV(null, nurbs)

    # create the follicle attachment
    fols = createFollicle(nurbs, u=uv['nu'], v=uv['nv'])

    # parent and move to bottom so follicle is first in stack
    if parent:
        null = maya.cmds.parent(null, fols['transform'])
        maya.cmds.reorder(null, f=True)

    return {
        'null': null,
        'nurbs':nurbs,
        'follicle':fols['follicle'],
        'transform':fols['transform'],
        'uv':uv
        }


def folliclesFromSel(parent=True):
    """
    Create attachment follicles per selected transforms to selected nurbs.
    - Only works on one patch at a time.
    - Parents transforms by default.
    """

    # check for transforms and a nurbs surface
    s = maya.cmds.ls(sl=1, type='transform', l=True)
    nurbs = maya.cmds.ls(s, ap=True, dag=True, type='nurbsSurface')

    # if nurbs check for history intermediates
    nurbs_parents = list(set(maya.cmds.listRelatives(nurbs, p=True, pa=True, f=True)))
    if len(nurbs_parents) != 1:
        print('Only one nurbs surface in the stack of selected transforms supported (more than one nurbs transform selected.')
        return

    # get the nurbs parent and remove it from transforms list
    np = maya.cmds.listRelatives(nurbs, p=True, type='transform', pa=True, f=True)
    nurbs = nurbs[0]
    s.remove(np[0])

    # build follicles if only one nurbs and one or more transforms
    r = []
    for n in s:
        f = follicleFromNode(n, nurbs, parent=parent)
        r.append(f)

    return r

# EOF
