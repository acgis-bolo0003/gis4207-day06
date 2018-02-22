#-------------------------------------------------------------------------------
# Name:        Mapping02.py
#
# Author:      Dragos_B and Emilie R
#
# Created:     21-02-2018
# Copyright:   (c) mie_r , Dragos_B 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy.mapping as mapping
import os

scriptFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptFolder)
# MappingEx.mxd file is your exercise folder (e.g. under <dir>\day06\ if script located under <dir>\day06\lab\DragosBandEmilieR\)
inMDX = r"..\..\MappingEx.mxd"

mxd = mapping.MapDocument(inMDX)
#mxd = mapping.MapDocument("CURRENT")
#frames = mapping.ListDataFrames(mxd,"W*")
#for df in frames:
    #df.name="World"
    #mxd.activeView = df.name

mxd.activeView = "World"
#print mxd.activeView
