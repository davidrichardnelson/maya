import maya.OpenMaya
import maya.api.OpenMaya
import maya.cmds
from math import pow,sqrt

def isCurve(crv):

    # Check object exists
    if not maya.cmds.objExists(crv): 
        return False

    # Check shape
    if maya.cmds.objectType(crv) == 'transform': 
        crv = maya.cmds.listRelatives(crv, s=True, ni=True, pa=True)
        if crv:
            crv = crv[0]
        else:
            return False

    if maya.cmds.objectType(crv) != 'nurbsCurve': 
        return False
    
    return True


def curveVectors(crv):
    """
    given a curve, generate a dictonary of the following:
    {
        'curve'    : original curve
        'position' : list from 0:end of (0,0,0) coordinates of nearest points on curve to CVs (root to anchor to)
        'up'       : list from 0:end of (0,0,0) coordinates of CVs from curve
        'tangent'  :  List from 0:end of (0,0,0) coordinates of each CV
        'param'    : List from 0:end of coordinate on curve value for each CV
    }
    """
    
    if not isCurve(crv):
        return
    
    dag = maya.OpenMaya.MDagPath()
    sel = maya.OpenMaya.MSelectionList()
    sel.add(crv)
    sel.getDagPath(0, dag)
    space = maya.OpenMaya.MSpace.kWorld

    cvFn = maya.OpenMaya.MFnNurbsCurve(dag)
    msu = maya.OpenMaya.MScriptUtil()
    paramPtr = msu.asDoublePtr()
    mp = maya.OpenMaya.MPoint()

    # get all CVs in the defined space
    CVs = maya.OpenMaya.MPointArray()
    cvFn.getCVs(CVs, space)

    # define params to output
    r = {'curve' : crv}
    p = []
    u = []
    t = []
    cpos = []

    # iterate over all the cvs
    for cv in range(CVs.length()):
        # get the position of the CV (this is the up vector since it is up off the curve
        pt = CVs[cv]

        # we get the closest point on the curve for the current cv
        ptOnCurve = cvFn.closestPoint(pt, paramPtr)
        param = msu.getDouble(paramPtr)

        # get the position on curve closest to the CV
        ptPosOnCurve = cvFn.getPointAtParam(param, mp, space)

        # get the tangent of the current CV
        tan = cvFn.tangent(param, space)

        # pass the params for return
        cpos.append(param)
        u.append((pt.x, pt.y, pt.z))
        p.append((mp.x, mp.y, mp.z))
        t.append((tan.x, tan.y, tan.z))

    # pass the params for return to dict
    r['position'] = p
    r['up'] = u
    r['tangent'] = t
    r['param'] = cpos

    return r


def jointsAtParams(crv):
    """
    build a chain from a curve from 0:end of joints and align their aim to each other 
    based on the curve chain n to n+1 vector and where up is n+1 up vector from curve to nearest CV
    """

    if not isCurve(crv):
        return
    
    # get curve params
    r = curveVectors(crv)

    # build temp aim and up vectors from list of base positions on curve nearest CVs
    aims = []
    ups = []
    for i in range(len(r['position'])):

        aim = ( maya.cmds.createNode('joint') )
        maya.cmds.setAttr(aim +'.t', r['position'][i][0], r['position'][i][1], r['position'][i][2])
        aims.append(aim)

        up = ( maya.cmds.createNode('joint') )
        maya.cmds.setAttr(up +'.t', r['up'][i][0], r['up'][i][1], r['up'][i][2])
        ups.append(up)

    # build chain from n+1 to end
    # aim n at n+1
    # if end just use joint since it is on curve already
    # delete the cruft when done
    js = []
    for i in range(len(r['position'])):

        if i != len(r['position'])-1:

            aim = aims[i+1]
            root = maya.cmds.createNode('joint')
            up = ups[i+1]

            maya.cmds.setAttr(root+'.t', r['position'][i][0], r['position'][i][1], r['position'][i][2])

            ac = maya.cmds.aimConstraint(aim, root, wut='object', wuo=up)
            maya.cmds.setAttr(ac[0]+'.worldUpType', 1)
            maya.cmds.select(root)
            j = maya.cmds.joint(n=crv+'_'+str(i)+'_JNT')

            j = maya.cmds.parent(j, w=1)[0]

            maya.cmds.delete(root)

        else:
        
            j = maya.cmds.duplicate(aims[i], rr=True, n=crv+'_'+str(i)+'_JNT')[0]

        js.append(j)

    # delete the temp aim and up vector nulls
    maya.cmds.delete(aims, ups)

    # parent joints to each other 
    for j in range(1, len(js)):
        js[j] = maya.cmds.parent(js[j], js[j-1])[0]


    js = maya.cmds.ls(js, dag=True, ap=True)
    for j in range(len(js)-1):
        d = distance(js[j], js[j+1])
        maya.cmds.setAttr(js[j]+'.radius', (d * 0.5) )

    # zero out the end joint
    end = js[len(js)-1]
    maya.cmds.setAttr(end+'.jo', 0, 0, 0)
    endParent = maya.cmds.listRelatives(end, p=True)[0]
    maya.cmds.setAttr( endParent+'.r', -90, 0, 0 ) # weird hack, not sure why circles are off on loft at end-1?
    maya.cmds.setAttr( end+'.radius', maya.cmds.getAttr( endParent +'.radius' ) )

    return js


def distance(a, b):
    """
    Get the distance between two nodes
    """

    a1, b1 = maya.cmds.xform(a, ws=True, t=True, q=True), maya.cmds.xform(b, ws=True, t=True, q=True)    

    return sqrt(pow(a1[0]-b1[0],2)+pow(a1[1]-b1[1],2)+pow(a1[2]-b1[2],2))


def curve(null, curve='circle', radius=1.0, degree=3):
    """
    Put a circle under a null with history for control or construction history
    """

    # check validity of args
    if not maya.cmds.objExists(null):
        return
    
    if maya.cmds.nodeType(null) == 'transform' or maya.cmds.nodeType(null) == 'joint':

        if curve == 'circle':
            cir = maya.cmds.circle(c=(0,0,0), nr=(1,0,0), sw=360, r=radius, d=degree, ut=0, tol=0.01, s=6, ch=1)[0]
        elif curve == 'line':
            radius = radius * 0.2 # smaller than circle
            cir = maya.cmds.curve(d=1, p=[(0,0,radius), (0,0,(-1*radius))], k=(0,1) )

        cir = maya.cmds.parent(cir, null, r=1)
        shape = maya.cmds.parent(maya.cmds.listRelatives(cir, s=1, f=1, pa=1, type='nurbsCurve'), null, r=1, s=1)

        maya.cmds.delete(cir)

        return {'null' : null, 'make' : maya.cmds.listHistory(shape), 'curve' : shape[0] }


def jointFromJoint(j, radius=1.0, name=''):
    """
    Create a joint from a joint with zero jointOrient
    """

    if not maya.cmds.objExists(j):
        return
        
    if maya.cmds.nodeType(j) != 'joint':
        return

    s = maya.cmds.ls(sl=True)

    maya.cmds.select(j)
    newj = maya.cmds.joint(n=name)
    maya.cmds.setAttr( newj+'.radius', (maya.cmds.getAttr( j +'.radius' ) * radius) )

    if s:
        maya.cmds.select(s)
    
    return newj


def curveFromTransforms(nulls):
    """
    Create a nurbsCurve from transforms
    """

    pos = []
    for i in range(len(nulls)):
        m = [maya.cmds.xform(nulls[i], q=True, t=True, ws=True)]
        pos.extend(m)

    degree = 1
    if len(pos) > 3:
        degree = 3

    c = maya.cmds.curve(d=degree, p=pos)

    return c



def circles(crv, loft=True, bind=True, sets=True):
    """
    Build circles per null with history
    """

    if not isCurve(crv):
        return

    js = jointsAtParams(crv)

    shapes = []
    cs = []
    nulls = []
    lines = []

    for j in range(len(js)):
        
        circle_j = jointFromJoint(js[j], name=js[j]+'_CIRCLE_JNT')
        
        # create nurbsCircle and set makeNurbsCircle radius to joint radius
        c = curve(circle_j, curve='circle', radius = 0.5)
        maya.cmds.setAttr( c['make'][1]+'.radius', maya.cmds.getAttr( js[j]+'.radius' ) )

        nulls.append(c['null'])
        shapes.append(c['make'][0])
        cs.append(c['make'][1])

        line_j = jointFromJoint(js[j], radius = 0.5, name=js[j]+'_LINE_JNT')
        l = curve(line_j, curve='line')

        lines.append(l['curve'])

    r = {
        'circles' :  cs,
        'shapes' : shapes,
        'nulls' : nulls,
        'lines' : lines
    }

    if loft:
        loft_tube = maya.cmds.loft(r['shapes'], n=crv+'_TUBE', ch=True, u=True, c=False, ar=True, d=3, ss=True, rn=False, po=False, rsn=True)
        loft_ribbon = maya.cmds.loft(r['lines'], n=crv+'_RIBBON', ch=True, u=True, c=False, ar=True, d=3, ss=True, rn=False, po=False, rsn=True)
        r['tube'] = loft_tube
        r['ribbon'] = loft_ribbon

    if bind and loft:
        bind = []
        for j in range(len(js)):
            n = jointFromJoint(js[j])
            if maya.cmds.listRelatives(n, p=True):
                n = maya.cmds.parent(n, w=True)[0]
            bind.append(n)

        bind = bind[::-1] # reverse hier

        for j in range(len(bind)-1):
            bind[j] = maya.cmds.parent( bind[j], bind[j+1])[0]

        pols = maya.cmds.nurbsToPoly(loft_tube[0], n=crv+'_PXY', mnd=1, ch=True, f=3, pt=1, pc=200, chr=0.9, ft=0.01, mel=0.001, d=0.1, ut=1, un=3, vt=1, vn=3, uch=0, ucr=0, cht=0.2, es=0, ntr=0, mrt=0, uss=1)

        skin = maya.cmds.skinCluster(bind, [pols[0],loft_tube[0],loft_ribbon[0]], tsb=True, mi=1, obeyMaxInfluences=True)[0]
        r['skin'] = skin

    if sets:
        lines_set = maya.cmds.sets(lines, n=crv+'_lines_set')
        circles_set = maya.cmds.sets(shapes, n=crv+'_circles_set')

    return r
    
    
# EOF