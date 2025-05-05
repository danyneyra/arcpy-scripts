import arcpy

input_excel = arcpy.GetParameterAsText(0)  # Input Excel file
output_shp = arcpy.GetParameterAsText(1)  # Output shapefile
sheet_name = "Hoja1"  # Nombre de la hoja de Excel

# Convertir Excel a Tabla
arcpy.ExcelToTable_conversion(
    input_excel,
    "temp01.dbf",
    sheet_name
)
# Convertir tabla Excel a capa de puntos
arcpy.management.XYTableToPoint(
    in_table="temp01.dbf",
    out_feature_class=output_shp,
    x_field="XCOORD",
    y_field="YCOORD",
    coordinate_system=arcpy.SpatialReference(32717)  # WGS 84 / UTM zona 17 Sur
)