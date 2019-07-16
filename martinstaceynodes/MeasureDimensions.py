import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
from Revit.Elements import *
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

inNode0 = IN [0]
lineList = []
if isinstance(inNode0, list):
	lineList.extend(IN[0])
else:
	lineList.append(IN[0])
lineList = UnwrapElement(lineList)
lineListRevitType  = []

for l in lineList:
	lineListRevitType.append(l.ToRevitType(True)) #line se llamaba  

TransactionManager.Instance.EnsureInTransaction(doc)

detailCurveList  = []
line_List  = []
referencesList = []
dimensions = []
for i in range(len(lineList)):   #detail_curve
	detailCurveList.append(doc.Create.NewDetailCurve(doc.ActiveView, lineListRevitType[i]))
	line_List.append(UnwrapElement(detailCurveList[i]).GeometryCurve)
	referencesList.append(ReferenceArray())
	referencesList[i].Append(UnwrapElement(line_List[i]).GetEndPointReference(0))
	referencesList[i].Append(UnwrapElement(line_List[i]).GetEndPointReference(1))
	dimensions.append(doc.Create.NewDimension(doc.ActiveView, lineListRevitType[i], referencesList[i]))

TransactionManager.Instance.TransactionTaskDone()

OUT = dimensions