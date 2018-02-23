#-------------------------------------------------------------------------------
# Name:        Mapping02.py
#
# Author:      Dragos_B and Emilie R
#
# Created:     21-02-2018
# Copyright:   (c) mie_r , Dragos_B 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
mxd = arcpy.mapping.MapDocument("CURRENT")
for df in arcpy.mapping.ListDataFrames(mxd,"World"):
    mxd.activeView = df.name

del mxd

