#-------------------------------------------------------------------------------
# Name:        Mapping04.py
# Purpose:    This script will go through all DataFrames and make all
# point layers visible(All polygon and line layers will not be visible)
#
# Author:      DragosB, EmilieR
#
# Created:     22-02-2018
# Copyright:   (c) DragosB, EmilieR, 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os

mxd = arcpy.mapping.MapDocument("MappingEx.mxd")
#mxd = arcpy.mapping.MapDocument("CURRENT")

for df in arcpy.mapping.ListDataFrames(mxd):
  for ly in arcpy.mapping.ListLayers(mxd, "", df):
     descly = arcpy.Describe(ly)
     geom = descly.ShapeType
     if geom =='point':
        ly.visible=='True'
     else:
        ly.visible=='False'

arcpy.RefreshActiveView()
arcpy.RefreshTOC()

mxd.save()
del mxd