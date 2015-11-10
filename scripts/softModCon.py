'''
daverichardnelson@gmail.com

usage: place into your projects/data dir and use the following shelf cmd:
import sys
sys.path.append(workspace(q=1, dir=1).replace('/scenes/','scripts/'))
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
31 January 2014
'''

import maya.cmds
import math

def softModCon():
    s = maya.cmds.ls(sl=1)
    if not s:
        error('nothing selected')

    ov='softModName'
    if maya.cmds.optionVar(ex=ov): 
        name = maya.cmds.optionVar(q=ov)
    else: 
        maya.cmds.optionVar(sv=(ov,name))
        
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
    
    ctrl = maya.cmds.circle(n=name+'_ctrl', r=size, ch=0, nrx=1, nry=0, nrz=0)[0]
    c2   = maya.cmds.circle(r=size, ch=0, nrx=0, nry=1, nrz=0)[0]
    c3   = maya.cmds.circle(r=size, ch=0, nrx=0, nry=0, nrz=1)[0]
    maya.cmds.parent(maya.cmds.listRelatives([c2,c3], s=1, ni=1), ctrl, r=1, s=1)
    maya.cmds.delete(c2,c3)
    
    rad = maya.cmds.curve(n=name+'_rad', d=1, p=((-1,-1,1),(-1,-1,-1),(1,-1,-1),(1,-1,1),(-1,-1,1),(-1,1,1),(-1,1,-1),(-1,-1,-1),(-1,1,-1),(1,1,-1),(1,-1,-1),(1,1,-1),(1,1,1),(1,-1,1),(1,1,1),(-1,1,1)), k=(0,1,2,3,4,1,6,7,8,9,10,11,12,13,14,15) )
    maya.cmds.setAttr(rad+'.s', type = 'double3', *(size,size,size))
    
    maya.cmds.delete(maya.cmds.pointConstraint(sm[1], ctrl))
    maya.cmds.delete(maya.cmds.pointConstraint(sm[1], rad))
    maya.cmds.makeIdentity(ctrl, a=1)
    maya.cmds.makeIdentity(rad, a=1)
    
    shape = maya.cmds.parent(maya.cmds.listRelatives(sm[1], c=1), ctrl, r=1, s=1)[0]
    maya.cmds.setAttr(shape+'.v', 0)
    maya.cmds.connectAttr(ctrl+'.worldMatrix', sm[0]+'.matrix', f=1)
    maya.cmds.delete(sm[1])
    
    loc  = maya.cmds.createNode('locator')
    locp = maya.cmds.listRelatives(loc, p=1)
    maya.cmds.delete(maya.cmds.pointConstraint(ctrl, locp))
    maya.cmds.makeIdentity(locp, a=1)
    loc = maya.cmds.parent(loc, rad, r=1, s=1)[0]
    maya.cmds.setAttr(loc+'.v', 0)
    maya.cmds.delete(locp)
    maya.cmds.connectAttr(rad+".worldPosition[0]", sm[0]+".falloffCenter", f=1)
    maya.cmds.connectAttr(rad+'.worldInverseMatrix[0]', sm[0]+'.bindPreMatrix', f=1)
    
    hmnul=maya.cmds.createNode('transform', n=name+'_parent')
    maya.cmds.delete(maya.cmds.pointConstraint(ctrl,hmnul))
    maya.cmds.makeIdentity(hmnul, a=1)
    rad=maya.cmds.parent(rad, hmnul)[0]
    
    ctrl=maya.cmds.parent(ctrl, rad)[0]
    
    maya.cmds.addAttr(ctrl, ln='falloffRadius', at='float', dv=(size*5), r=1, h=0, k=1)
    maya.cmds.connectAttr(ctrl+'.falloffRadius', sm[0]+'.falloffRadius', f=1)

    for c in maya.cmds.ls(hmnul, ap=1, dag=1, typ='nurbsCurve'):
        maya.cmds.reorder(c, b=1)
        shapename = maya.cmds.listRelatives(c, p=1, f=1, pa=1)[0].split('|')[-1]+'Shape'
        maya.cmds.rename(c, shapename)

    ret = [ctrl, rad, hmnul, sm[0]]
    maya.cmds.select(ret)

    return ret
