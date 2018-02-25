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
import arcpy
import sys
import os
#import os.path as path
mxd = arcpy.mapping.MapDocument(r".\mxdTemp\MappingEx.mxd")
#mxd = arcpy.mapping.MapDocument(r"D:\acgis\gis4207_Customization_I\day06\lab\DragosBandEmilieR\mxdTemp\MappingEx.mxd")

scriptPath = os.path.dirname(__file__)
os.chdir(scriptPath)
# print("Absolute path of the current script: "+ os.path.join(os.path.dirname(__file__)))

# Path three levels up from the current script (to get to broken links path):
three_up =  os.path.abspath(os.path.join(__file__ ,"../../.."))
# print("Path three levels up from the current script: "+ three_up)

# Path four levels up from the current script (to get to correct data link path):
four_up =  os.path.abspath(os.path.join(__file__ ,"../../../.."))
#print("Path four levels up from the current script: "+ four_up)

# List Broken DataSources links:
for lyr in arcpy.mapping.ListBrokenDataSources(mxd):
    print "Broken link before fixing path. Datasource %s does not exist" % lyr.dataSource

#findAndReplaceWorkspacePaths broken paths e.g. "D:\acgis\gis4207_Customization_I\day06\data" change to "D:\acgis\gis4207_Customization_I\data")
mxd.findAndReplaceWorkspacePaths(three_up +"\data", four_up + "\data")
# print "Broken links Path: " + three_up +"\data"+ "  replaced with correct path: "+ four_up + "\data"

# List again broken DataSources links (should not get broken links after fixing path):
for lyr in arcpy.mapping.ListBrokenDataSources(mxd):
    print "Datasource %s does not exist" % lyr.dataSource
else:
    print "No broken links after fixing path"

#mxd.saveACopy(r"D:\acgis\gis4207_Customization_I\day06\lab\DragosBandEmilieR\mxdTemp\MappingExNewLinks.mxd")
mxd.save()
del mxd
