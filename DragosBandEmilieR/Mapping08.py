#-------------------------------------------------------------------------------
# Name:        Mapping08.py
# Purpose: This script will save to pdf to a "temp" folder parallel with "lab".
# The Dataframe name is the base name for pdf, then append to a file called AllMaps.pdf
# Author:      Dragos_B and Emilie R
#
# Created:     21-02-2018
# Copyright:   (c) Dragos_B, Emilie_R, 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# pdfPath = r"D:\acgis\gis4207_Customization_I\day06\temp\AllMaps.pdf"

import arcpy
import os

pdfPath = r"..\..\temp\AllMaps.pdf"

if os.path.exists(pdfPath):
    os.remove(pdfPath)

pdfDoc = arcpy.mapping.PDFDocumentCreate(pdfPath)

mxd = arcpy.mapping.MapDocument("MappingEx.mxd")
for df in arcpy.mapping.ListDataFrames(mxd):
    arcpy.mapping.ExportToPDF(mxd, r"..\..\temp\\"+ df.name +".pdf", df)
    pdfDoc.appendPages(r"..\..\temp\\"+ df.name +".pdf")

pdfDoc.saveAndClose()

del pdfDoc
del mxd