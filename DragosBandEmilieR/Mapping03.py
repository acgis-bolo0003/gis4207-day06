#-------------------------------------------------------------------------------
# Name:        Mapping03.py
# Purpose:     Print a report of the layer information, including x, y
# coordinates.
# Author:      Dragos_B and Emilie R
#
# Created:     21-02-2018
# Copyright:   (c) Dragos_B, Emilie_R, 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

# MappingEx.mxd file is your exercise folder (e.g. under <dir>\day06\ if script located under <dir>\day06\lab\DragosBandEmilieR\)

mxd = arcpy.mapping.MapDocument("MappingEx.mxd")

print ("{:22}{:19}{}".format("DataFrame", "Scale", "Extent"))

for df in arcpy.mapping.ListDataFrames(mxd):
    print ("{:15}{:15}{:15},{:4},{:4},{:4}\n".format(df.name, int(df.scale), int(df.extent.XMin), int(df.extent.YMin), int(df.extent.XMax), int(df.extent.YMax)))

del mxd