__author__ = 's.sherbakov'

"""
Serge Scherbakov
realismus@gmail.com
www.serge-scherbakov.com
______________________________________________________________________________

AlignNormals.py - Snap vertices and Align Normals.
______________________________________________________________________________

    How to install:
        - save script into your maya script directory
        - open Script Editor and switch to Python tab in Maya
        - write two following strings:
            import AlignNormals
            AlignNormals.main()

______________________________________________________________________________

    How to use:
        - select Group of vertices on the first mesh and press "Ref" button
        - select vertices to adjust
        - press "Snap" to snap vertices to the nearest reference
        - press "AR" to align normals at selected vertices with normals at the nearest reference
        - press "AA" to set both normals (selected and the nearest reference) to calculated average value

______________________________________________________________________________

"""

import maya.cmds as cmds
import maya.OpenMaya as om
import math


class UI():
    def __init__(self):
        self.aligner = VertexAligner()
        self.__initUI__()

    def __initUI__(self):
        if cmds.window("alignNormalWin", exists=True): cmds.deleteUI("alignNormalWin", window=True)
        cmds.window("alignNormalWin", title="Normal Tools", minimizeButton=False, maximizeButton=False, sizeable=False)
        cmds.rowLayout(numberOfColumns=2, rowAttach=(1, "both", 0),
                       columnAttach=((1, "both", 0), (2, "both", 0)))
        self.refBtn = cmds.button(label="Ref\n0", width=60, height=70, c=lambda x: self.setRefVers())
        cmds.setParent("..")
        cmds.columnLayout(columnAttach=('both', 0), rowSpacing=3, columnWidth=45)
        cmds.button(label="Snap", height=35, c=lambda x: self.snapToRef())
        cmds.button(label="AR", height=35, c=lambda x: self.alignWithRef())
        cmds.button(label="AA", height=35, c=lambda x: self.alignAverage())
        cmds.showWindow("alignNormalWin")


    def setRefVers(self):
        verts = self.getSelectedVerts()
        if not verts:
            self.aligner.refVerts = []
            cmds.button(self.refBtn, edit=True, label="Ref\n0")
        else:
            self.aligner.refVerts = verts
            cmds.button(self.refBtn, edit=True,
                        label="Ref\n" + str(len(self.aligner.refVerts)))

    def getSelectedVerts(self):
        selection = cmds.ls(sl=True, long=True)
        if not selection:
            return None
        else:
            cmds.select(cmds.polyListComponentConversion(toVertex=True), replace=True)
            verts = cmds.filterExpand(sm=31, expand=True, fullPath=True)
        cmds.select(selection, replace=True)
        return verts

    def snapToRef(self):
        verts = self.getSelectedVerts()
        if verts:
            self.aligner.snapToRef(verts)

    def alignWithRef(self):
        selection = cmds.ls(sl=True, long=True)
        if not selection:
            cmds.error("Select Edges or Verts to align.")
        self.aligner.alignToRef()

    def alignAverage(self):
        selection = cmds.ls(sl=True, long=True)
        if not selection:
            cmds.error("Select Edges or Verts to align.")
        self.aligner.alignAverage()


class VertexAligner():
    def __init__(self):
        self.refVerts = None

    def findNearestVertIndex(self, vert):
        vertAT = cmds.xform(vert, q=True, ws=True, t=True)
        indexOfMin = 0
        minLen = float("inf")
        for index in range(len(self.refVerts)):
            vertBT = cmds.xform(self.refVerts[index], q=True, ws=True, t=True)
            vlen = math.sqrt(math.pow((vertAT[0] - vertBT[0]), 2) +
                             math.pow((vertAT[1] - vertBT[1]), 2) +
                             math.pow((vertAT[2] - vertBT[2]), 2))
            if vlen < minLen:
                minLen = vlen
                indexOfMin = index
        return indexOfMin

    def snapToRef(self, verts):
        print "snaping", verts
        if len(self.refVerts) == 0:
            cmds.error("Set reference vertices and try again.")

        selection = cmds.ls(sl=True, long=True)
        if not selection: cmds.error("Select Edges or Vertices to snap and try again.")
        cmds.select(cmds.polyListComponentConversion(toVertex=True), replace=True)
        verts = cmds.filterExpand(sm=31, expand=True, fullPath=True)
        for vert in verts:
            index = self.findNearestVertIndex(vert)
            refVertTransforms = cmds.xform(self.refVerts[index], q=True, ws=True, t=True)
            cmds.xform(vert, ws=True, t=refVertTransforms)

        cmds.select(selection, r=True)

    def alignToRef(self):
        if len(self.refVerts) == 0:
            cmds.error("Reference vertexes are not defined. Please define ref first.")
        selection = cmds.ls(sl=True, long=True)
        cmds.select(cmds.polyListComponentConversion(toVertex=True), replace=True)
        verts = cmds.filterExpand(sm=31, expand=True, fullPath=True)

        shape = str(self.refVerts[0]).split(".")[0]
        refTransform = cmds.listRelatives(shape, parent=True, path=True, fullPath=True)[0]

        shape = str(verts[0]).split(".")[0]
        objTransform = cmds.listRelatives(shape, parent=True, path=True, fullPath=True)[0]
        objTransformMatrixInverse = getTransformMatrix(objTransform).inverse()

        refRot = cmds.xform(refTransform, q=True, ws=True, ro=True)
        refAngle = om.MEulerRotation(math.radians(refRot[0]),
                                     math.radians(refRot[1]),
                                     math.radians(refRot[2]),
                                     om.MEulerRotation.kXYZ)
        for vert in verts:
            refVertIndex = self.findNearestVertIndex(vert)
            refNormal = cmds.polyNormalPerVertex(self.refVerts[refVertIndex], q=True, xyz=True)

            vec = om.MVector(refNormal[0], refNormal[1], refNormal[2])
            refNormal = vec.rotateBy(refAngle)
            normalVector = om.MVector(refNormal[0], refNormal[1], refNormal[2])
            newVector = normalVector * objTransformMatrixInverse
            # Assuming normals are equal for all triangles at this vert, and using the first triple.
            cmds.polyNormalPerVertex(vert, xyz=(newVector[0], newVector[1], newVector[2]))
        cmds.select(selection, r=True)

    def alignAverage(self):
        if len(self.refVerts) == 0:
            cmds.error("Reference vertexes are not defined. Please define ref first.")
        selection = cmds.ls(sl=True, long=True)
        cmds.select(cmds.polyListComponentConversion(toVertex=True), replace=True)
        verts = cmds.filterExpand(sm=31, expand=True, fullPath=True)

        shape = str(self.refVerts[0]).split(".")[0]
        obj1Transform = cmds.listRelatives(shape, parent=True, path=True, fullPath=True)[0]
        n1Rot = cmds.xform(obj1Transform, q=True, ws=True, ro=True)
        n1Angle = om.MEulerRotation(math.radians(n1Rot[0]),
                                    math.radians(n1Rot[1]),
                                    math.radians(n1Rot[2]),
                                    om.MEulerRotation.kXYZ)

        shape = str(verts[0]).split(".")[0]
        obj2Transform = cmds.listRelatives(shape, parent=True, path=True, fullPath=True)[0]
        n2Rot = cmds.xform(obj2Transform, q=True, ws=True, ro=True)
        n2Angle = om.MEulerRotation(math.radians(n2Rot[0]),
                                    math.radians(n2Rot[1]),
                                    math.radians(n2Rot[2]),
                                    om.MEulerRotation.kXYZ)

        for vert in verts:
            refIndex = self.findNearestVertIndex(vert)
            vecData = cmds.polyNormalPerVertex(self.refVerts[refIndex], q=True, xyz=True)
            vec1 = om.MVector(vecData[0], vecData[1], vecData[2])
            vec1 = vec1.rotateBy(n1Angle)

            vecData = cmds.polyNormalPerVertex(vert, q=True, xyz=True)
            vec2 = om.MVector(vecData[0], vecData[1], vecData[2])
            vec2 = vec2.rotateBy(n2Angle)

            averageNormal = (vec1 + vec2) / 2.0

            n1New = averageNormal * getTransformMatrix(obj1Transform).inverse()
            cmds.polyNormalPerVertex(self.refVerts[refIndex], xyz=(n1New.x, n1New.y, n1New.z))

            n2New = averageNormal * getTransformMatrix(obj2Transform).inverse()
            cmds.polyNormalPerVertex(vert, xyz=(n2New.x, n2New.y, n2New.z))

        cmds.select(selection, r=True)


def getTransformMatrix(obj):
    data = cmds.xform(obj, m=True, q=True, ws=True)
    matrix = om.MMatrix()
    for i in range(len(data)):
        om.MScriptUtil.setDoubleArray(matrix[i / 4], i - 4 * (i / 4), data[i])
    return matrix


def main():
    ui = UI()