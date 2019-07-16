import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
#The inputs to this node will be stored as a list in the IN variables.

import math
import clr
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import *
#Points Creation

import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel


dataEnteringNode = IN
angles = []


angles = range(0, 360, 10)
for index, angle in enumerate(angles):
	angles[index] =  math.radians(angle)

xPoints = []

for x in angles:
	xPoints.append(IN[0]*math.cos(x))
	
	
yPoints = []

for x in angles:
	yPoints.append(IN[0]*math.sin(x))
	

pointlist = []

for index, point in enumerate(xPoints):
	pointlist.append(Point.ByCoordinates(point,yPoints[index],0))


#Policurve creation
	
Linelist = PolyCurve.ByPoints(pointlist, True)	

#Surface creation

Surface = Linelist.Patch()

#Extrusion creation

Extrude = Surface.Thicken(IN[0])


#Rotation

PointOrigin = Point.ByCoordinates(0,0,0)

#Rotation Axis x

PointDesplaceX = Point.ByCoordinates(1,0,0)

VectorRoateX = Vector.ByTwoPoints(PointOrigin, PointDesplaceX)

GeometryRotateX = Extrude.Rotate(PointOrigin, VectorRoateX, IN[1])

#Rotation Axis Y

PointDesplaceY = Point.ByCoordinates(0,1,0)

VectorRoateY = Vector.ByTwoPoints(PointOrigin, PointDesplaceY)

GeometryRotateY = GeometryRotateX.Rotate(PointOrigin, VectorRoateY, IN[2])

#Rotation Axis Z

PointDesplaceZ = Point.ByCoordinates(0,0,1)

VectorRoateZ = Vector.ByTwoPoints(PointOrigin, PointDesplaceZ)

GeometryRotateZ = GeometryRotateY.Rotate(PointOrigin, VectorRoateZ, IN[3])


SurfaceVolumne = str(round(Surface.Area,2))
TotalVolume = str(round(Extrude.Volume,2))

dialog = TaskDialog("Metric")
dialog.MainInstruction = "Values"
dialog.MainContent = "Surface:     " + SurfaceVolumne + "\n" + "Volume:      "+ TotalVolume

dialog.CommonButtons = TaskDialogCommonButtons.Ok;
dialog.DefaultButton = TaskDialogResult.Ok;


if Surface.Area > 500 :
	dialog.MainInstruction = "WARNING VALUE > 500"
	dialog.MainIcon = TaskDialogIcon.TaskDialogIconWarning;
	dialog.Show()
elif IN[4] == True :
	dialog.Show()
else :
	pass

filepath = IN[5]

ex = Excel.ApplicationClass()
ex.Visible - False
ex.DisplayAlerts = False

workbook = ex.Workbooks.Open(filepath)
worksheet = workbook.Worksheets[1]

column = 2
activecell = worksheet.Cells[column,2]

while activecell.Text != "":
	if activecell.Text !="":
		column = column+1
		activecell = worksheet.Cells[column,2]


activecell.Value2 = Surface.Area
worksheet.SaveAs(unicode(filepath))
Close = workbook.Close(True)
ex.Quit()

#Assign your output to the OUT variable.
OUT =  GeometryRotateZ