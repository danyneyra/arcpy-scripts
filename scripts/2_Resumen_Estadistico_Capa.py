import arcpy
import statistics

def crear_campo_si_no_existe(feature_layer, campo, tipo):
    """Crea un campo si no existe en el Feature Layer."""
    if campo.upper() not in field_names:
        arcpy.AddMessage(f"Creando campo '{campo}'...")
        arcpy.management.AddField(feature_layer, campo, tipo)

def calcular_valores(feature_layer, campos_mes, campo_resultado, funcion_calculo):
    """Aplica una función de cálculo a los valores de los campos de meses y actualiza el campo resultado."""
    campos_calculo = campos_mes + [campo_resultado]
    with arcpy.da.UpdateCursor(feature_layer, campos_calculo) as cursor:
        for row in cursor:
            valores = row[:len(campos_mes)]
            row[len(campos_mes)] = funcion_calculo(valores)
            cursor.updateRow(row)

def calcular_total(valores):
    return sum(valores)

def calcular_media(valores):
    return sum(valores) / len(valores) if valores else 0

def calcular_min(valores):
    return min(valores) if valores else 0

def calcular_max(valores):
    return max(valores) if valores else 0

def calcular_rango(valores):
    return calcular_max(valores) - calcular_min(valores)

def calcular_desviacion(valores):
    return statistics.stdev(valores) if len(valores) > 1 else 0

def calcular_cv(valores):
    media = calcular_media(valores)
    desviacion = calcular_desviacion(valores)
    return (desviacion / media) * 100 if media != 0 else 0

def calcular_error_tipico(valores):
    n = len(valores)
    return (calcular_desviacion(valores) / (n ** 0.5)) if n > 1 else 0

# Entrada de parámetros
feature_layer = arcpy.GetParameterAsText(0)
procesos = arcpy.GetParameterAsText(1).split(";") if arcpy.GetParameterAsText(1) else []

# Lista de nombres de meses válidos
meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

# Obtener campos existentes
fields = arcpy.ListFields(feature_layer)
field_names = [f.name.upper() for f in fields]
campos_mes = [f.name for f in fields if f.name.upper() in meses]

if not campos_mes:
    arcpy.AddError("No se encontraron campos de meses en el Feature Layer.")
else:
    # Procesos
    if "Total" in procesos:
        crear_campo_si_no_existe(feature_layer, "TOTAL", "DOUBLE")
        calcular_valores(feature_layer, campos_mes, "TOTAL", calcular_total)
        arcpy.AddMessage("Total calculado correctamente.")

    if "Media" in procesos:
        crear_campo_si_no_existe(feature_layer, "MEDIA", "DOUBLE")
        calcular_valores(feature_layer, campos_mes, "MEDIA", calcular_media)
        arcpy.AddMessage("Media calculada correctamente.")

    if "Min/Max/Rango" in procesos:
        crear_campo_si_no_existe(feature_layer, "Min", "DOUBLE")
        crear_campo_si_no_existe(feature_layer, "Max", "DOUBLE")
        crear_campo_si_no_existe(feature_layer, "Rango", "DOUBLE")
        calcular_valores(feature_layer, campos_mes, "Min", calcular_min)
        calcular_valores(feature_layer, campos_mes, "Max", calcular_max)
        calcular_valores(feature_layer, campos_mes, "Rango", calcular_rango)
        arcpy.AddMessage("Min, Max y Rango calculados correctamente.")

    if "DS" in procesos:
        crear_campo_si_no_existe(feature_layer, "DS", "DOUBLE")
        calcular_valores(feature_layer, campos_mes, "DS", calcular_desviacion)
        arcpy.AddMessage("Desviación estándar calculada correctamente.")

    if "CV" in procesos:
        crear_campo_si_no_existe(feature_layer, "CV", "DOUBLE")
        calcular_valores(feature_layer, campos_mes, "CV", calcular_cv)
        arcpy.AddMessage("Coeficiente de variación calculado correctamente.")

    if "Error_Tipico" in procesos:
        crear_campo_si_no_existe(feature_layer, "Error_Ti", "DOUBLE")
        calcular_valores(feature_layer, campos_mes, "Error_Ti", calcular_error_tipico)
        arcpy.AddMessage("Error típico calculado correctamente.")

arcpy.AddMessage("Proceso finalizado con éxito.")
