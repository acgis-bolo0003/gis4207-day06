#-------------------------------------------------------------------------------
# Name:        Mapping07.py
# Purpose: This script will write a script that will fix all of the broken
# data sources in the MapDocument(A copy of MappingEx.mxd will be placed in a
# sub-folder named 'mxdTemp' - one level below scripts folder!).
# Author:      Dragos_B and Emilie_R
#
# Created:     23-02-2018
# Copyright:   (c) Dragos_B, Emilie_R, 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#mxd = arcpy.mapping.MapDocument(r"D:\acgis\gis4207_Customization_I\day06\lab\DragosBandEmilieR\mxdTemp\MappingEx.mxd")
import arcpy
import sys
import os

mxd = arcpy.mapping.MapDocument(r"mxdTemp\MappingEx.mxd")


scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)
# print("Absolute path of the current script: "+ os.path.join(os.path.dirname(__file__)))


three_up =  os.path.abspath(os.path.join(__file__ ,"../../.."))
four_up =  os.path.abspath(os.path.join(__file__ ,"../../../.."))


# List Broken DataSources links:
for lyr in arcpy.mapping.ListBrokenDataSources(mxd):
    print "Broken link before fixing path. Datasource %s does not exist" % lyr.dataSource

mxd.findAndReplaceWorkspacePaths(three_up +"\data", four_up + "\data")

for lyr in arcpy.mapping.ListBrokenDataSources(mxd):
    print "Datasource %s does not exist" % lyr.dataSource
else:
    print "No broken links after fixing path"

mxd.save()
del mxd
