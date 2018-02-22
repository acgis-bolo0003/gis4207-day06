#-------------------------------------------------------------------------------
# Name:        Mapping02.py
#
# Author:      Dragos_B and Emilie R
#
# Created:     21-02-2018
# Copyright:   (c) mie_r , Dragos_B 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

# MappingEx.mxd file is your exercise folder (e.g. under <dir>\day06\ if script located under <dir>\day06\lab\DragosBandEmilieR\)
inMXD = "CURRENT"
mxd = arcpy.mapping.MapDocument(inMXD)

for df in arcpy.mapping.ListDataFrames(mxd,"W*"):
 mxd.activeView = df.name

#mxd.save()
#del mxd

