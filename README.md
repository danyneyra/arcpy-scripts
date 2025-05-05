# 🧰 Repositorio de Scripts ArcPy para Toolboxes

Este repositorio contiene una colección de scripts desarrollados en **Python con ArcPy**, diseñados para ser utilizados como herramientas personalizadas (*toolboxes*) dentro de entornos de **ArcGIS Desktop/Pro**.

## 📁 Estructura del Repositorio
```plaintext
📦 Arcpy-Toolboxes
scripts/
├── herramienta_1.py
├── herramienta_2.py
├── ...
toolboxes/
├── herramientas.tbx
docs/
├── ejemplos/
├── imágenes/
```

- `scripts/`: Contiene los scripts `.py` individuales que implementan la lógica de cada herramienta.
- `toolboxes/`: Almacena los archivos `.atbx` o `.pyt` configurados para usar los scripts.
- `docs/`: Documentación complementaria, ejemplos de uso y capturas de pantalla.

## 🧪 Requisitos

- Python 3.x (versión compatible con ArcGIS)
- ArcPy (instalado con ArcGIS Desktop o ArcGIS Pro)
- ArcGIS Desktop o Pro instalado y licenciado correctamente

## 🚀 Cómo Usar

1. Clona este repositorio o descarga los scripts individualmente:
   ```bash
   git clone https://github.com/danyneyra/arcpy-toolboxes.git

2. En ArcGIS, abre la toolbox .tbx o crea una nueva y vincula uno de los scripts desde scripts/.

3. Configura los parámetros desde el GUI o edita el script para personalizar su comportamiento.

4. Ejecuta la herramienta como cualquier otra de ArcGIS.

## 🛠️ Scripts Incluidos

| Nombre                             | Descripción breve                                                                 |
|------------------------------------|------------------------------------------------------------------------------------|
| `1_Cargar_Coordenadas_Excel.py`    | Permite cargar coordenadas de un archivo de Excel                                 |
| `2_Resumen_Estadistico_Capa.py`    | Permite realizar cálculos de datos mensuales como Total, Media, Min, Máx, Desviación estándar, Error Típico |


## 📚 Ejemplos de Uso
Consulta la carpeta docs/ejemplos para ver capturas de pantalla y ejemplos prácticos de cómo usar cada herramienta.