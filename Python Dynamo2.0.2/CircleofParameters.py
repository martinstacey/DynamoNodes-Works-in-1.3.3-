# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
radi = IN[0]
xin = IN [1]
yin = IN [2]
numpoints = IN[3]

import math

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

PointList = []

for i, point in enumerate(xPoints):
	PointList.append(Point.ByCoordinates(point,yPoints[i],0))
	
OUT = PointList