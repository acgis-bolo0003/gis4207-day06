#-------------------------------------------------------------------------------
# Name:        Mapping03.py
#
# Author:      Dragos_B and Emilie R
#
# Created:     21-02-2018
# Copyright:   (c) mie_r , Dragos_B 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

# MappingEx.mxd file is your exercise folder (e.g. under <dir>\day06\ if script located under <dir>\day06\lab\DragosBandEmilieR\)
inMXD = r"..\..\MappingEx.mxd"
mxd = arcpy.mapping.MapDocument(inMXD)

print ("{:22}{:19}{}".format("DataFrame", "Scale", "Extent"))

for df in arcpy.mapping.ListDataFrames(mxd):
    print ("{:15}{:15}{:15},{:4},{:4},{:4}\n".format(df.name, int(df.scale), int(df.extent.XMin), int(df.extent.YMin), int(df.extent.XMax), int(df.extent.YMax)))

del mxd