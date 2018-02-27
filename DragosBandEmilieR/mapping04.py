#-------------------------------------------------------------------------------
# Name:        Mapping04.py
# Purpose:    This script will go through all DataFrames and make all
# point layers visible(All polygon and line layers will not be visible)
#
# Author:      DragosB, EmilieR
#
# Created:     26-02-2018
# Copyright:   (c) DragosB, EmilieR, 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

mxd = arcpy.mapping.MapDocument("CURRENT")

for df in arcpy.mapping.ListDataFrames(mxd):
  for ly in arcpy.mapping.ListLayers(mxd, "", df):
    if ly.isFeatureLayer:
       descly=arcpy.Describe(ly)
       if descly.ShapeType == 'Point':
         ly.visible = 'True'
       else:
         ly.visible = 'False'


arcpy.RefreshActiveView()
arcpy.RefreshTOC()

del mxd