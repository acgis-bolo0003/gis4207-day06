#-------------------------------------------------------------------------------
# Name:        Mapping01.py
# Purpose: A script to set the following MapDocument properties with specific values:
# title,author,credits,summary,description,tags
# Use MapDocument("MappingEx.mxd") and run from PyScripter.
#Call the save method on MapDocument to save changes to the mxd.
#
# Author:      Emilie Rabeau, Dragos B
#
# Created:     21-02-2018
# Copyright:   (c) mie_r , Dragos_B 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy.mapping as mapping
import os

mxd = mapping.MapDocument(r"MappingEx.mxd")
mxd.title = "arcpy.mapping module exercises"
mxd.author = "Dragos Bologa and Emilie Rabeau"
mxd.credits = "David Viljoen made me do it"
mxd.summary = "See Description"
mxd.description = "This document was used for practicing Python coding with the arcpy.mapping module."
mxd.tags = "arcpy.mapping,python,gis4207"

mxd.save()

del mxd
