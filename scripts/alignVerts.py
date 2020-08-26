import maya.cmds as mc
import numpy as np
import maya.OpenMaya as om

def distance(p, q, r):
    p = np.array(p)
    q = np.array(q)
    r = np.array(r)
    x = p-q
    return np.dot(r-q, x)/np.dot(x, x)

def line_param(p, q, r):
    p = np.array(p)
    q = np.array(q)
    r = np.array(r)
    return np.linalg.norm(distance(p, q, r)*(p-q)+q-r)

def point(p, q, r):
    p1=np.array(p)
    p2=np.array(q)
    p3=np.array(r)
    d=np.cross(p2-p1,p3-p1)/np.linalg.norm(p2-p1)
    return d

def intermediates(p1, p2, nb_points=3):
    """"Return a list of nb_points equally spaced points
    between p1 and p2"""
    # If we have 8 intermediate points, we have 8+1=9 spaces
    # between p1 and p2
    x_spacing = (p2[0] - p1[0]) / (nb_points + 1)
    y_spacing = (p2[1] - p1[1]) / (nb_points + 1)

    return [[p1[0] + i * x_spacing, p1[1] +  i * y_spacing] for i in range(1, nb_points+1)]
    #print(intermediates([1, 2], [10, 6.5], nb_points=8))

def curve(a, b):
    return mc.curve(d=1, p=(a,b))
    #npoc = mc.createNode('nearestPointOnCurve')
    #mc.connectAttr(c+'.create', npoc+'.inputCurve', f=True)
    #xf = mc.createNode('transform')
    #mc.connectAttr(xf+'.t', npoc+'.inPosition', f=True)

def closestPointOnCurve(location, curveObject):

    curve = curveObject

    # put curve into the MObject
    tempList = om.MSelectionList()
    tempList.add(curve)
    curveObj = om.MObject()
    tempList.getDependNode(0, curveObj)  # puts the 0 index of tempList's depend node into curveObj

    # get the dagpath of the object
    dagpath = om.MDagPath()
    tempList.getDagPath(0, dagpath)

    # define the curve object as type MFnNurbsCurve
    curveMF = om.MFnNurbsCurve(dagpath)

    # what's the input point (in world)
    point = om.MPoint( location[0], location[1], location[2])

    # define the parameter as a double * (pointer)
    prm = om.MScriptUtil()
    pointer = prm.asDoublePtr()
    om.MScriptUtil.setDouble (pointer, 0.0)

    # set tolerance
    tolerance = .00000001

    # set the object space
    space = om.MSpace.kObject

    # result will be the worldspace point
    result = om.MPoint()
    result = curveMF.closestPoint (point, pointer,  0.0, space)

    position = [(result.x), (result.y), (result.z)]
    curvePoint = om.MPoint ((result.x), (result.y), (result.z))

    # creates a locator at the position
    #mc.spaceLocator (p=(position[0], position[1], position[2]))

    parameter = om.MScriptUtil.getDouble (pointer)

    # just return - parameter, then world space coord.
    return [(result.x), (result.y), (result.z)]# parameter]


def alignVerts():
    v = mc.ls(orderedSelection=True, fl=True)
    if len(v) > 2:
        a = mc.pointPosition(v[0], w=1)
        z = mc.pointPosition(v[-1], w=1)
        crv = curve(a,z)
        j = mc.createNode('joint')
        for i in range(1, len(v)-1):
            x = mc.pointPosition(v[i], w=1)
            p = closestPointOnCurve(x, crv)
            c = mc.cluster(v[i])
            mc.setAttr(j+'.t', p[0], p[1], p[2])
            mc.delete(mc.pointConstraint(j,c[1]))
        mc.delete(crv, j)
        mc.delete(mc.ls(v, r=1, o=True), ch=True)
