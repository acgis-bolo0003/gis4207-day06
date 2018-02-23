#-------------------------------------------------------------------------------
# Name:        Loa dLayerVisibility
# Purpose:
#
# Author:      Emilie Rabeau
#
# Created:     22-02-2018
# Copyright:   (c) Emilie Rabeau 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
mxd = arcpy.mapping.MapDocument("CURRENT")
dataframes = arcpy.mapping.ListDataFrames(mxd)
layer = arcpy.mapping.ListLayers(mxd)

visibilityFile = open(r'LayerVisibility.txt', 'r')
content = visibilityFile.readlines()


for data in dataframes:
    for lyr in layer:
        for info in content:
            infoSplit = info.rstrip().split("\t")
            if data.name == infoSplit[0] and lyr.name == infoSplit[1]:
                lyr.visible = infoSplit[2]
                arcpy.RefreshActiveView()
                arcpy.RefreshTOC()

