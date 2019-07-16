# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN
ElementList = []
if isinstance(IN[0],list):
	ElementList.extend(IN[0])
else:
	ElementList.append(IN[0])

ElementList = UnwrapElement(ElementList)
ParametersListParam = []
for a in ElementList:
	ParametersListParam.append(a.Parameters)

ParametersList = []
while len(ParametersList) != len(ParametersListParam):
	ParametersList.append([])
for list in ParametersListParam:
	for item in list :
		ParametersList[ParametersListParam.index(list)].append (item.Definition.Name)

OUT = ParametersList
