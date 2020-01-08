'''
usage: place into your projects/data dir and use the following shelf cmd:
import softMod
reload(softMod)
softMod.softModCon()

1) select a mesh(es)
2) run tool softModCon()
3) enter name
4) parent the top resulting nul to anywhere in rig or constrain it so it follows rig
5) start animating:

    * the sphere is the CTRL which deformers the geometry, transform it and see
    * tune the falloffRadius to make its affect broader or more refined
    * the cube is the parent of the sphere control and affects where the center
        of the deformation occurs from
    * place pivot where you want deformation to occur, then animate control
    * you can orient the direction of the control with the pivot as well, or it's parent
    * once deformed, you can animate the pivot parent for a bug under rug kind of affect

david@ventosum.com
'''

import maya.cmds
import math

def softModCon():
    s = maya.cmds.ls(sl=1)
    if not s:
        error('nothing selected')

    ov='softModName'
    name = ''
    if maya.cmds.optionVar(ex=ov):
        name = maya.cmds.optionVar(q=ov)
    else:
        try:
            maya.cmds.optionVar(sv=(ov,name))
        except:
            print 'OptionVar issue, whatever...'

    result = maya.cmds.promptDialog(title='name',message='name',tx=name, button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
    if result == 'OK':
        name = maya.cmds.promptDialog(query=True, text=True)
    else:
        return

    maya.cmds.optionVar(sv=(ov,name))

    ret = doIt(name, s)
    return ret

def doIt(name, s=maya.cmds.ls(sl=1, r=1, o=1)):

    if not s:
        error('no meshes selected')

    if not name:
        error('no name specified for softMod')

    objs = maya.cmds.ls(s, o=1, r=1)
    sm = maya.cmds.softMod(objs, n=name)

    size = 0.0000001
    for obj in objs:
        max=list(maya.cmds.getAttr(obj+'.boundingBoxMax'))[0]
        min=list(maya.cmds.getAttr(obj+'.boundingBoxMin'))[0]
        cur = math.sqrt( (max[0] - min[0]) ** 2 + (max[1] - min[1]) ** 2 + (max[2] - min[2]) ** 2 )
        cur = cur*0.1
        if cur > size: size = cur

    ctrl = maya.cmds.circle(n=name+'_CON', r=size, ch=0, nrx=1, nry=0, nrz=0)[0]
    c2   = maya.cmds.circle(r=size, ch=0, nrx=0, nry=1, nrz=0)[0]
    c3   = maya.cmds.circle(r=size, ch=0, nrx=0, nry=0, nrz=1)[0]
    maya.cmds.parent(maya.cmds.listRelatives([c2,c3], s=1, ni=1), ctrl, r=1, s=1)
    maya.cmds.delete(c2,c3)

    piv = maya.cmds.circle(n=name+'_PIV', r=(size*1.1), ch=0, nrx=0, nry=1, nrz=0)[0]

    maya.cmds.delete(maya.cmds.pointConstraint(sm[1], ctrl))
    maya.cmds.delete(maya.cmds.pointConstraint(sm[1], piv))
    maya.cmds.makeIdentity(ctrl, a=True)
    maya.cmds.makeIdentity(piv, a=True)

    shape = maya.cmds.parent(maya.cmds.listRelatives(sm[1], c=1), ctrl, r=1, s=1)[0]
    maya.cmds.setAttr(shape+'.v', 0)
    maya.cmds.connectAttr(ctrl+'.worldMatrix', sm[0]+'.matrix', f=1)
    maya.cmds.delete(sm[1])

    loc  = maya.cmds.createNode('locator')
    locp = maya.cmds.listRelatives(loc, p=1)
    maya.cmds.delete(maya.cmds.pointConstraint(ctrl, locp))
    maya.cmds.makeIdentity(locp, a=1)
    loc = maya.cmds.parent(loc, piv, r=True, s=True)[0]
    maya.cmds.setAttr(loc+'.v', 0)
    maya.cmds.delete(locp)
    maya.cmds.connectAttr(piv+".worldPosition[0]", sm[0]+".falloffCenter", f=1)
    maya.cmds.connectAttr(piv+'.worldInverseMatrix[0]', sm[0]+'.bindPreMatrix', f=1)

    zero = maya.cmds.createNode('transform', n=name+'_ZERO')
    maya.cmds.delete(maya.cmds.pointConstraint(ctrl,zero))
    maya.cmds.makeIdentity(zero, a=True)

    piv = maya.cmds.parent(piv, zero)
    ctrl = maya.cmds.parent(ctrl, piv)

    maya.cmds.addAttr(ctrl, ln='falloffRadius', at='float', dv=(size*1500), r=1, h=0, k=1)
    maya.cmds.connectAttr(ctrl[0]+'.falloffRadius', sm[0]+'.falloffRadius', f=1)

    for c in maya.cmds.ls(zero, ap=1, dag=1, typ='nurbsCurve'):
        maya.cmds.reorder(c, b=1)
        shapename = maya.cmds.listRelatives(c, p=1, f=1, pa=1)[0].split('|')[-1]+'Shape'
        maya.cmds.rename(c, shapename)

    ret = {
        'control' : ctrl[0],
        'pivot' : piv[0],
        'zero' : zero,
        'softMod' : sm[0]
    }
    maya.cmds.select(ctrl)

    return ret
