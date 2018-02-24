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
#mxd = arcpy.mapping.MapDocument(r".\mxdTemp\MappingEx.mxd")
mxd = arcpy.mapping.MapDocument(r"D:\acgis\gis4207_Customization_I\day06\lab\DragosBandEmilieR\mxdTemp\MappingEx.mxd")

for lyr in arcpy.mapping.ListBrokenDataSources(mxd):
    print "Datasource %s does not exist" % lyr.dataSource

#mxd.findAndReplaceWorkspacePaths(r"..\..\data", r"..\..\..\Data")
mxd.findAndReplaceWorkspacePaths(r"D:\acgis\gis4207_Customization_I\day06\data", r"D:\acgis\gis4207_Customization_I\data")
print "Path replaced"

for lyr in arcpy.mapping.ListBrokenDataSources(mxd):
    print "Datasource %s does not exist" % lyr.dataSource
else:
    print "No broken links"

#mxd.saveACopy(r"D:\acgis\gis4207_Customization_I\day06\lab\DragosBandEmilieR\mxdTemp\MappingExNewLinks.mxd")
mxd.save()
del mxd
