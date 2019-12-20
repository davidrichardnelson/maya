from pprint import pprint
import maya.cmds
import follicle
import chains
import skinCluster
import softModCon

import glTools.tools

reload(follicle)
reload(chains)
reload(skinCluster)
reload(softModCon)

"""
import scratch
reload(scratch)

# run first
cs = scratch.build()

# wait for it, memory fails if not run line at a time, FML, moving on....
scratch.attach(cs)
"""

def build():
    """
    Build hair patches and bind to geom from generated curves
    """

    cs = []
    for crv in maya.cmds.ls(sl=1):
    
        # build the curve ribbons and proxy
        c = chains.circles(crv)
        c['curve'] = crv
        cs.append(c)

    return cs


def jointAtRibbon(name, ribbonShape, u, v):

    pos = maya.cmds.createNode('pointOnSurfaceInfo')
    maya.cmds.connectAttr( ribbonShape+'.worldSpace[0]', pos+'.inputSurface' )
    x = maya.cmds.createNode('transform')

    maya.cmds.connectAttr( pos+'.position', x+'.t', f=1 )
    maya.cmds.setAttr( pos+'.parameterU', u )
    maya.cmds.setAttr( pos+'.parameterV', v )

    tj = maya.cmds.createNode('joint', n=name+'_JNT')
    maya.cmds.delete( maya.cmds.pointConstraint(x, tj) )
    maya.cmds.delete( x, pos )

    f = follicle.follicleFromNode(tj, ribbonShape, parent=True)
    maya.cmds.setAttr(f['null'][0]+'.t', 0,0,0)
    maya.cmds.setAttr(f['null'][0]+'.r', 0,0,0)
    maya.cmds.setAttr(f['null'][0]+'.jo', 0,0,0)

    j = maya.cmds.parent(f['null'], w=True)[0]
    z1 = maya.cmds.createNode( 'transform', n=name+'_A_ZERO')
    maya.cmds.delete( maya.cmds.pointConstraint( j, z1 ) )
    maya.cmds.delete( maya.cmds.orientConstraint( j, z1 ) )
    z2 = maya.cmds.duplicate( z1, n=name+'_B_ZERO', rr=True )[0]
    z2 = maya.cmds.parent(z2, z1)
    c = maya.cmds.duplicate( j, rr=True, n=name+'_CON')[0]
    c = maya.cmds.parent(c, z2)[0]
    j = maya.cmds.parent(j, c)[0]

    shapeXf = maya.cmds.curve(n=c+'Shape', d=1, p=((-1,-1,1),(-1,-1,-1),(1,-1,-1),(1,-1,1),(-1,-1,1),(-1,1,1),(-1,1,-1),(-1,-1,-1),(-1,1,-1),(1,1,-1),(1,-1,-1),(1,1,-1),(1,1,1),(1,-1,1),(1,1,1),(-1,1,1)), k=(0,1,2,3,4,1,6,7,8,9,10,11,12,13,14,15) )
    shapeXf = maya.cmds.parent(shapeXf, c, r=1)[0]
    shape = maya.cmds.parent(maya.cmds.listRelatives(shapeXf, s=1, f=1, pa=1, type='nurbsCurve'), c, r=1, s=1)

    maya.cmds.delete(shapeXf, f['transform'])
    
    return {'joint':j, 'control':c, 'zero':z1}


def bindRibbonWithCons(ribbon):

    joints = []
    zeroes = []
    cons = []
    uvs = [[0.5,0.0], [0.5,0.1], [0.5,0.5], [0.5,0.9], [0.5,1.0]]

    name = ribbon.split('_CRV')[0]

    for i in range(len(uvs)):
        r = jointAtRibbon(name+'_'+str(i), ribbon, uvs[i][0], uvs[i][1])
        joints.append(r['joint'])
        zeroes.append(r['zero'])
        cons.append(r['control'])

    maya.cmds.delete( ribbon, ch=True )
    skin = maya.cmds.skinCluster( joints, ribbon, tsb=True, mi=2, obeyMaxInfluences=True)[0]

    # quick hacks to parent ends to end minus 1 on each end of surface/curve
    zeroes[0] = maya.cmds.parent(zeroes[0], cons[1])[0]
    zeroes[4] = maya.cmds.parent(zeroes[4], cons[3])[0]

    # clean ribbon so each line has same weighted verts after copy weights
    cleanRibbonWeights(ribbon)
    
    # parent to RIG joints
    head = 'basic_head_01_FOLLOW'
    neckB = 'basic_neck_02_FOLLOW'
    neckA = 'basic_neck_01_FOLLOW'
        
    zeroes[1] = maya.cmds.parent(zeroes[1], head)[0]
    zeroes[2] = maya.cmds.parent(zeroes[2], neckB)[0]
    zeroes[3] = maya.cmds.parent(zeroes[3], neckA)[0]
    
    return {'influences':joints, 'zero':zeroes, 'controls':cons, 'skin':skin}


def attach(cs, inf=INF):
    """
    After manually checking twists on ribbons for any anomolies (twisting) then run this.
    """

    pxy = []
    fols = []

    for c in cs:
    
        # delete ribbon history
        maya.cmds.delete( c['ribbon'][0], ch=True )

        # # unparent chain or it crashes maya, ugh
        # # build follicles to attach joint chain to
        maya.cmds.select(c['influences'], c['ribbon'][0])
        f = follicle.folliclesFromSel()

        # build ribbon IK cons
        bindRibbonWithCons(c['ribbon'][0])

        # delete proxy history to pass weights to it.
        maya.cmds.delete([c['proxy'][0]], ch=True)

        # bind the proxy mesh with ribbon chain and tube weights
        tubeSkin = maya.cmds.skinCluster(c['influences'], [c['proxy'][0]], tsb=True, mi=1, obeyMaxInfluences=True)[0]
        maya.cmds.copySkinWeights(ss=c['skin'], ds=tubeSkin, noMirror=True, surfaceAssociation='closestPoint', influenceAssociation="closestJoint")

        # get rid of nurbs tube
        maya.cmds.delete(c['tube'])

        # get rid of nurbs generated nulls for loft to tube
        maya.cmds.delete( maya.cmds.listRelatives(c['nulls'], p=1) )

        # copy weights from crv to model geom by assumed naming convention
        mesh = maya.cmds.ls( c['curve'].replace('_CRV','_REN') )
        skinCluster.copy_skin(c['proxy'][0], mesh[0])

        # get rid of pxy
        maya.cmds.delete(c['proxy'][0])
        


def cleanRibbonWeights(ribbon):

    numv = int(maya.cmds.getAttr(ribbon+'.mxv')+3)
    for i in range(0,numv):
        print i
        maya.cmds.select(ribbon+'.cv[0:1]['+str(i)+']')
        glTools.tools.copyPasteWeights.copyWeights()
        glTools.tools.copyPasteWeights.pasteWeights()


# EOF
