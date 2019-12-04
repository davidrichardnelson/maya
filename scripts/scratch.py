from pprint import pprint
import follicle
import maya.cmds
reload(follicle)
r = follicle.folliclesFromSel(parent=True)
pprint(r)

import maya.cmds as mc
for i in range(43):
    c = mc.cluster('necklace_BIND.cv['+str(i)+'][0:1]')
    j = mc.createNode('joint', n='bind_necklace_'+str(i).zfill(2)+'_JNT')
    mc.delete(mc.pointConstraint(c[1], j))
    mc.delete(c)
    
    
import maya.cmds as mc
for i in range(43):
    c = mc.cluster('necklace_BIND.cv['+str(i)+'][0:1]')
    j = mc.createNode('joint', n='bind_necklace_'+str(i).zfill(2)+'_JNT')
    mc.delete(mc.pointConstraint(c[1], j))
    mc.delete(c)