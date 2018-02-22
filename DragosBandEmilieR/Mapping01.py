#-------------------------------------------------------------------------------
# Name:        Mapping01.py
# Purpose: a script to set the following MapDocument properties with specific values:
# title,author,credits,summary,description,tags
# Use MapDocument("MappingEx.mxd") and run from PyScripter.
#Call the save method on MapDocument to save changes to the mxd.
#
# Author:      mie_r, Dragos_B
#
# Created:     21-02-2018
# Copyright:   (c) mie_r , Dragos_B 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#import arcpy
import arcpy.mapping as mapping
import os

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)
# MappingEx.mxd file is your exercise folder (e.g. under <dir>\day06\ if script located under <dir>\day06\lab\DragosBandEmilieR\)
inMXD = r"..\..\MappingEx.mxd"

mxd = mapping.MapDocument(inMXD)
mxd.title = "arcpy.mapping module exercises"
mxd.author = "Dragos Bologa and Emilie Rabeau"
mxd.credits = "David Viljoen made me do it"
mxd.summary = "See Description"
mxd.description = "This document was used for practicing Python coding with the arcpy.mapping module."
mxd.tags = "arcpy.mapping,python,gis4207"
#mxd.saveACopy(r"D:\acgis\gis4207_Customization_I\day06\MappingEx_1.mxd")
mxd.save()
del mxd
