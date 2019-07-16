# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

dataEnteringNode = IN
name = IN [0]

if name == None:
	name = "World"

OUT = "Hello " + name