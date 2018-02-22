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
import arcpy
import os

def main():
    pass

visibilityFile = open(r'LayerVisibility.txt', 'r')

mxd = arcpy.mapping.MapDocument("CURRENT")
dataFrame = arcpy.mapping.ListDataFrames(mxd)


for data in dataFrame:
    layer = arcpy.mapping.ListLayers(data)
    for lyr in layer:
        visibilityFile.write("{:15}\t {:10}\t {:10}\n".format(data.name, lyr.name, lyr.visible))


acrpy.RefreshActiveView()
arcpy.RefreshTOC()

if __name__ == '__main__':
    main()