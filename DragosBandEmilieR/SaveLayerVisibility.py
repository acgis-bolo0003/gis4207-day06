#-------------------------------------------------------------------------------
# Name:        SaveLayerVisibility
# Purpose:     Create a tab-delimited file with the data frame names, layer names
# and the visibility values in a boolean format.
#
# Author:      Emilie Rabeau
#
# Created:     22-02-2018
# Copyright:   (c) Emilie Rabeau 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os

visibilityFile = open(r'LayerVisibility.txt', 'w')

mxd = arcpy.mapping.MapDocument(r"MappingEx.mxd")
dataFrame = arcpy.mapping.ListDataFrames(mxd)


for data in dataFrame:
    layer = arcpy.mapping.ListLayers(data)
    for lyr in layer:
        visibilityFile.write("{}\t {}\t {}\n".format(data.name, lyr.name, lyr.visible))

visibilityFile.close()
