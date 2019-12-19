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

# define body mesh joint list to copy weights to primary target from for ribbons of head or other hair
INF = ["L_bind_finger_thumb_04_JNT","R_bind_limb_arm_08_JNT","R_bind_limb_arm_01_JNT","R_bind_limb_arm_03_JNT","R_bind_limb_arm_mid_JNT","R_bind_limb_arm_09_JNT","R_bind_finger_index_02_JNT","R_bind_limb_arm_end_JNT","R_bind_limb_arm_upper_JNT","R_bind_limb_arm_05_JNT","R_bind_limb_arm_04_JNT","R_bind_limb_arm_07_JNT","R_bind_midHand_JNT","R_bind_fingerTips_JNT","R_bind_finger_index_01_JNT","R_bind_hand_JNT","R_bind_finger_middle_02_JNT","R_bind_finger_middle_01_JNT","R_bind_finger_index_04_JNT","R_bind_finger_index_03_JNT","R_bind_finger_index_05_JNT","R_bind_finger_middle_04_JNT","R_bind_finger_middle_05_JNT","R_bind_finger_ring_01_JNT","R_bind_finger_middle_03_JNT","L_bind_limb_arm_03_JNT","L_bind_limb_arm_01_JNT","L_bind_limb_arm_upper_JNT","L_bind_limb_arm_mid_JNT","L_bind_finger_index_04_JNT","L_bind_finger_middle_01_JNT","L_bind_limb_arm_09_JNT","L_bind_midHand_JNT","L_bind_limb_arm_08_JNT","L_bind_fingerTips_JNT","L_bind_limb_arm_07_JNT","L_bind_limb_arm_05_JNT","L_bind_limb_arm_end_JNT","L_bind_finger_index_02_JNT","L_bind_limb_arm_04_JNT","L_bind_finger_index_03_JNT","L_bind_finger_index_01_JNT","L_bind_hand_JNT","L_bind_finger_index_05_JNT","L_bind_finger_ring_01_JNT","L_bind_finger_middle_02_JNT","L_bind_finger_middle_03_JNT","L_bind_finger_ring_02_JNT","L_bind_finger_ring_05_JNT","L_bind_finger_thumb_01_JNT","L_bind_finger_middle_05_JNT","L_bind_finger_thumb_02_JNT","L_bind_finger_middle_04_JNT","L_bind_finger_ring_04_JNT","L_bind_finger_ring_03_JNT","L_bind_finger_thumb_03_JNT","R_bind_finger_thumb_02_JNT","R_bind_finger_thumb_03_JNT","R_bind_finger_thumb_01_JNT","R_bind_finger_thumb_04_JNT","bind_basic_tail_05_JNT","bind_basic_tail_07_JNT","L_bind_limb_leg_03_JNT","L_bind_limb_leg_upper_JNT","bind_basic_tail_02_JNT","bind_basic_tail_08_JNT","bind_basic_tail_01_JNT","bind_basic_tail_04_JNT","bind_basic_tail_03_JNT","bind_basic_tail_06_JNT","L_bind_limb_leg_01_JNT","L_bind_limb_leg_mid_JNT","L_bind_limb_leg_05_JNT","L_bind_toeTips_JNT","L_bind_limb_leg_04_JNT","L_bind_finger_indexToe_01_JNT","L_bind_finger_ringToe_03_JNT","L_bind_ankle_JNT","L_bind_finger_indexToe_02_JNT","L_bind_finger_indexToe_03_JNT","L_bind_limb_leg_08_JNT","L_bind_limb_leg_end_JNT","L_bind_limb_leg_09_JNT","L_bind_finger_middleToe_01_JNT","L_bind_finger_middleToe_03_JNT","L_bind_limb_leg_07_JNT","L_bind_ball_JNT","L_bind_finger_middleToe_02_JNT","L_bind_finger_ringToe_01_JNT","L_bind_finger_ringToe_02_JNT","R_bind_limb_leg_01_JNT","R_bind_ankle_JNT","R_bind_limb_leg_upper_JNT","R_bind_limb_leg_07_JNT","R_bind_toeTips_JNT","R_bind_limb_leg_03_JNT","R_bind_finger_indexToe_01_JNT","R_bind_limb_leg_05_JNT","R_bind_limb_leg_mid_JNT","R_bind_ball_JNT","R_bind_limb_leg_08_JNT","R_bind_limb_leg_end_JNT","R_bind_limb_leg_04_JNT","R_bind_limb_leg_09_JNT","R_bind_finger_middleToe_03_JNT","R_bind_finger_ringToe_01_JNT","R_bind_finger_ringToe_02_JNT","R_bind_finger_middleToe_02_JNT","R_bind_finger_indexToe_02_JNT","R_bind_finger_middleToe_01_JNT","R_bind_finger_indexToe_03_JNT","R_bind_finger_ringToe_03_JNT","R_bind_finger_ring_02_JNT","R_bind_finger_ring_04_JNT","R_bind_finger_ring_05_JNT","R_bind_finger_ring_03_JNT","bind_spine_05_JNT","bind_spine_04_JNT","bind_basic_root_01_JNT","bind_spine_02_JNT","bind_spine_03_JNT","bind_spine_01_JNT","bind_basic_head_03_JNT","bind_spine_07_JNT","bind_basic_neck_01_JNT","bind_basic_neck_02_JNT","bind_basic_head_01_JNT","bind_basic_neck_03_JNT","bind_spine_06_JNT","bind_basic_head_02_JNT"]

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


def attach(cs, inf=INF):

    pxy = []
    fols = []

    for c in cs:
    
        # delete ribbon history
        maya.cmds.delete( c['ribbon'][0], ch=True )

        # # unparent chain or it crashes maya, ugh
        # # build follicles to attach joint chain to
        maya.cmds.select(c['influences'], c['ribbon'][0])
        f = follicle.folliclesFromSel()

        # bind ribbon by influence body list and copy weights
        skin = maya.cmds.skinCluster(inf, [c['ribbon'][0]], tsb=True, mi=1, obeyMaxInfluences=True)[0]
        maya.cmds.copySkinWeights(ss="body_skinCluster", ds=skin, noMirror=True, surfaceAssociation='closestPoint', influenceAssociation="closestJoint")

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

        maya.cmds.setAttr(c['proxy'][0]+'.v', 0)
        #maya.cmds.setAttr(c['ribbon'][0]+'.v', 0)

        # generate a softMod deformer at the end of the curve; hard coded to last knot for now, whatevs, deadlines brah.
        sm = softModCon.doIt(c['curve'].replace('_CRV',''), s=c['ribbon'][0])
        cls = maya.cmds.cluster(c['curve']+'.cv[7]')
        maya.cmds.delete( maya.cmds.pointConstraint(cls[1], sm['zero']))
        maya.cmds.delete(cls)
        maya.cmds.setAttr(sm['control']+'.falloffRadius', 20)

        # get rid of pxy
        maya.cmds.delete(c['proxy'][0])
        
        # clean ribbon so each line has same weighted verts after copy weights
        cleanRibbonWeights(c['ribbon'][0])


def cleanRibbonWeights(ribbon):

    numv = int(maya.cmds.getAttr(ribbon+'.mxv')+3)
    for i in range(0,numv):
        print i
        maya.cmds.select(ribbon+'.cv[0:1]['+str(i)+']')
        glTools.tools.copyPasteWeights.copyWeights()
        glTools.tools.copyPasteWeights.pasteWeights()


# EOF
