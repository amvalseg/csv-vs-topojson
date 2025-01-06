# Herramienta de Comparación entre CSV y TopoJSON  

¡Hola! 👋  
Este script en Python está diseñado para ayudarte a comparar datos de un archivo CSV con un archivo TopoJSON. Identifica elementos coincidentes y no coincidentes entre campos específicos de ambos archivos y proporciona resultados detallados para su análisis.  

## Funcionalidades 👌  
- Comparar campos en el archivo CSV con propiedades en el archivo TopoJSON.  
- Generar información sobre valores coincidentes y no coincidentes.  
- Producir un resumen de valores únicos y coincidencias para facilitar el análisis.  

## Requisitos ✅  
- Python 3.6 o superior.  
- Librerías:  
   - pandas  
   - json (librería estándar de Python)  

## Cómo usarlo 🤔  

### 1. Editar el script  

##### Rutas de archivos:  
Actualiza las variables `csv_file` y `json_file` con las rutas de tus archivos CSV y TopoJSON (Líneas 119 y 120):  

    csv_file = r"ruta_a_tu_archivo_csv.csv"  
    json_file = r"ruta_a_tu_archivo_topojson.json"  

##### Columnas del CSV:  
Reemplaza los nombres de columnas de ejemplo en el script (`column_1`, `column_2`, etc.) por los nombres reales de las columnas en tu archivo CSV que deseas comparar (Línea 30):  

    # Extraer las columnas correspondientes del CSV (Reemplazar 'column_1', 'column_2', 'column_3', 'column_4' por las columnas que necesitas trabajar)  
    
        csv_field_1 = csv_data['column_1'].unique()  
        csv_field_2 = csv_data['column_2'].unique()  
        csv_field_3 = csv_data['column_3'].unique()  
        csv_field_4 = csv_data['column_4'].unique()  
    

##### Propiedades del JSON:  
Actualiza `json_prop1` y `json_prop2` con los nombres de las propiedades en el archivo TopoJSON que deseas comparar (Línea 24):  

        # Iterar sobre las geometrías dentro del campo 'objects' del JSON  
       
    for geometry in topojson_data['objects']['world.geo']['geometries']:  
            if 'properties' in geometry:  
                json_ids.append(geometry['properties'].get('json_prop1', None))  
                json_names.append(geometry['properties'].get('json_prop2', None))  

Es posible que también tengas que modificar los valores bajo `['objects']['world.geo']['geometries']` en función de cómo se llamen en tu archivo TopoJSON.  

### 2. Ejecutar el script ⚙️  
Guarda los cambios realizados en el script y ejecútalo en un entorno de Python:  

El script mostrará:  
- Recuento de valores únicos en cada columna.  
- Número de coincidencias y no coincidencias entre los campos.  
- Listas de valores no coincidentes para un análisis más profundo.  

## Ejemplo de uso 💡  
Puedes encontrar un ejemplo de implementación de este código en `/example`.  

Ahí encontrarás el archivo CSV, el archivo TopoJSON y el script adaptado.  

------------  

#### 👐 Espero que este script te ayude a ahorrar tiempo a la hora de trabajar con mapas y datos.  

------------  
