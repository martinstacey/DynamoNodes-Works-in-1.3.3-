# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
datain = UnwrapElement(IN[0])

# Place your code below this line

# Assign your output to the OUT variable.
OUT = datain