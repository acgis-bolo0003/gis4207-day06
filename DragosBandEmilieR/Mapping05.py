#-------------------------------------------------------------------------------
# Name:        Mapping05.py
# Purpose:    This script will add Continents and World Cities layers to Canada
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

#mxd = arcpy.mapping.MapDocument("MappingEx.mxd")
mxd = arcpy.mapping.MapDocument("CURRENT")

# Path three levels up from the current script (to get to broken links path):
four_up =  os.path.abspath(os.path.join(__file__ ,"../../../.."))
#print("Path four levels up from the current script: "+ four_up)

df = arcpy.mapping.ListDataFrames(mxd,"Canada")[0]
addCLayer = arcpy.mapping.Layer(four_up + "\Data\World\Continents.lyr")
arcpy.mapping.AddLayer(df, addCLayer, "AUTO_ARRANGE")
##
# add World Cities.lyr and store it in addWLayer
addWLayer = arcpy.mapping.Layer(four_up + "\Data\World\World Cities.lyr")
arcpy.mapping.AddLayer(df, addWLayer, "AUTO_ARRANGE")

arcpy.RefreshActiveView()
arcpy.RefreshTOC()

#mxd.saveACopy(r"D:\acgis\gis4207_Customization_I\day06\lab\DragosBandEmilieR\MappingExNewLayers.mxd")
del mxd, addCLayer, addWLayer

#mxd.save()
#del mxd