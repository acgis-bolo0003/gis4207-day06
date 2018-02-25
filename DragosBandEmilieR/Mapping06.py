#-------------------------------------------------------------------------------
# Name:        Mapping06.py
# Purpose:    This script will remove Continents and World Cities layers to Canada
# DataFrames
# Author:      DragosB, EmilieR
#
# Created:     22-02-2018
# Copyright:   (c) DragosB, EmilieR, 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os
# get to data path using os.path up_three

#mxd = arcpy.mapping.MapDocument("MappingExNewLayers.mxd")
mxd = arcpy.mapping.MapDocument("CURRENT")

# Path three levels up from the current script (to get to broken links path):
four_up =  os.path.abspath(os.path.join(__file__ ,"../../../.."))
#print("Path four levels up from the current script: "+ four_up)

df = arcpy.mapping.ListDataFrames(mxd,"Canada")[0]
for lyr in arcpy.mapping.ListLayers(mxd,"", df):
    if lyr.name == "Continents":
        arcpy.mapping.RemoveLayer(df,lyr)
    if lyr.name == "World Cities":
        arcpy.mapping.RemoveLayer(df,lyr)

arcpy.RefreshActiveView()
arcpy.RefreshTOC()

#mxd.saveACopy(r"D:\acgis\gis4207_Customization_I\day06\lab\DragosBandEmilieR\MappingEx_RemoveLayers.mxd")
del mxd

