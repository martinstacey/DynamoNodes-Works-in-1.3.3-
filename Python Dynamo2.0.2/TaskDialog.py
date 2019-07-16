# Enable Python support and load DesignScript library
import clr
import math
clr.AddReference('ProtoGeometry')
clr.AddReference("RevitAPIUI")
from Autodesk.DesignScript.Geometry import *
from Autodesk.Revit.UI import *

#INS
radi = IN[0]
xin = IN [1]
yin = IN [2]
numpoints = IN[3]
extr = IN[4]

angles = []
angles = range (0,360,numpoints)
for i, angle in enumerate(angles):
	angles[i] = math.radians(angle)
xPoints = []
for x in angles:
	xPoints.append(radi*math.cos(x)+xin)
yPoints = []
for y in angles:
	yPoints.append(radi*math.sin(y)+yin)
pointlist = []
for i, point in enumerate(xPoints):
	pointlist.append(Point.ByCoordinates(point,yPoints[i],0))
#Polycurve
LineList = PolyCurve.ByPoints(pointlist,True)
Surface = LineList.Patch()
#Extrusion
Extrude = Surface.Thicken(extr)
#Rotation X Axis
PointOrigin = Point.ByCoordinates(0,0,0)
PointDisplaceX = Point.ByCoordinates(1,0,0)
VectorRotateX = Vector.ByTwoPoints(PointOrigin,PointDisplaceX)
GeometryRotateX = Extrude.Rotate(PointOrigin,VectorRotateX,IN[5])

dialog = TaskDialog("Titulo") 
dialog.MainInstruction = "Instruccion"
dialog.MainContent = "Resultado"
dialog.CommonButtons = TaskDialogCommonButtons.Close;
dialog.DefaultButton = TaskDialogResult.Close;
dialog.Show()

OUT = GeometryRotateX