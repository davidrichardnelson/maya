import maya.cmds as cmd
import maya.mel as mel
import re

def makeCenterLine(c=1, j=1):
    # track selection order must be ON for this to work
    points = 'curve -d 3 '
    sel = cmd.ls(os=True, fl=True)
    ob = cmd.ls(o=True, sl=True)
    num = []
    out = []
    edges = []
    joints = []
    for one in sel:
        strip = re.search(r"\[([0-9]+)\]", one)
        num.append(strip.group(1))
    size = len(num)
    if (size):
        if size == 1:
            edges = cmd.polySelect(edgeRing=(int(num[0])), ns=True)
        if size == 2:
            edges = cmd.polySelect(edgeRingPath=(int(num[0]), int(num[1])), ns=True)
        if size > 2:
            edges = num
        for one in edges:
            cmd.select(ob)
            cmd.polySelect(elb=int(one))
            clust = cmd.cluster(n='poo#')
            cmd.select(clear=True)
            posi = cmd.getAttr(clust[1]+'.origin')
            if c:
                points = points + ('-p %s %s $%s ' %(posi[0][0], posi[0][1], posi[0][2]))
            if j:
                joints.append(cmd.joint(p = (posi[0][0], posi[0][1], posi[0][2])))
            cmd.delete(clust)
        if c:
            print points
            out.append(mel.eval(points))
        if j:
            for i in reversed(range(1, len(edges))):
                cmd.parent(joints[i], joints[i-1])
            cmd.joint(joints[0], e=True, oj='xyz', sao='zup', ch=True, zso=True)
            cmd.joint(joints[-1], e=True, o = (0,0,0))
            out.append(joints[0])
        cmd.select(out)
    else:
        print('Nothing is selected.')
        
