# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

# Place your code below this line
elUW = UnwrapElement(IN[0])
#elementlist = elUW.Parameters
parametersList = []
for i in elUW.Parameters:
	parametersList.append(i)
	
OUT = parametersList