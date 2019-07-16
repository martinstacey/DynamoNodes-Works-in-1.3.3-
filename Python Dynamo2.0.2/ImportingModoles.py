import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

#Document Manager de Revit
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument
#REVIT API
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import FilteredElementCollector
#REVIT NODES
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

import sys
sys.path.append("C:\Program Files (x86)\IronPython 2.7\Lib")
import random

var1 = random.randint(0,200)



OUT = var1