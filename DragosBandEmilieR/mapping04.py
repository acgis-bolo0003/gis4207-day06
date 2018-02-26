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
import os
#mxd = arcpy.mapping.MapDocument("MappingEx.mxd")
mxd = arcpy.mapping.MapDocument("CURRENT")

# Path four levels up from the current script (to get to correct data link path):
#four_up =  os.path.abspath(os.path.join(__file__ ,"../../../.."))
#print("Path four levels up from the current script: "+ four_up)
#workspace_path = four_up + "\data\Canada\Canada.gdb"
#workspace_path = four_up + "\data"
#arcpy.env.workspace = workspace_path

dataframes = arcpy.mapping.ListDataFrames(mxd)
layers = arcpy.mapping.ListLayers(mxd)
fcList = arcpy.ListFeatureClasses()
print fcList
point_features = list()
for layer in layers:
    for feature in fcList:
        desc = arcpy.Describe(feature)
        if desc.shapeType == 'Point':
                point_features.append(feature)
                print("Point Layer before update " + layer.name + " is visible:       " + str(layer.visible))
                layer.visible = True
                #arcpy.mapping.UpdateLayer(df,layer, desc.shapeType,True)
                print("Point Layer after update " + layer.name + " is visible:       " + str(layer.visible))
        else:
                layer.visible = False
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
del mxd

