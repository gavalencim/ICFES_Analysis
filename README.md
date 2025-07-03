# Análisis Icfes
El siguiente proyecto presenta una propuesta de obtención, limpieza y visualización de datos para un dataset que contiene información sobre los resultados del las pruebas saber ICFES en colombia durante el periodo que comprendió entre 2014 a 2022 con más de 7 millones de registros. 

El conjunto de datos se puede obtener del siguiente link https://www.datos.gov.co/Educaci-n/Resultados-nicos-Saber-11/kgxf-xxbe/about_data

## Contenido del proyecto:
- obtencion_all_data.py: Script que obtiene la información desde la API y devuelve un CSV con toda la información.
- data_cleaning.py: Script que explora la limpieza de los datos para su uso posterior.
- index.html: Script donde se expone el dashboard creado a partir de los datos limpios.

## Obtención de datos con Python
Para la obtención de los datos se hizo uso de la siguente API: https://www.datos.gov.co/resource/kgxf-xxbe.json proporcionada con la página web.
Dado que la cantidad de registros es bastante extensa, se hicieron varias solicitudes de 50000 registros de manera organizada hasta llegar a los 7109704 de registros. Los datos se cargaron a un archivo de texto plano CSV. 

## Limpieza de los datos con Python
Para la limpieza de datos se siguieron los siguientes pasos:
1. Selcción de columnas de CSV con todos los datos del punto anterior.
2. Ajuste de tipos de datos de las columnas seleccionadas:
   * Datos numéricos
   * Datos temporales (fechas)
   * Datos boolenanos
   * Reemplazo de datos (Estrato de cadena a número)
3. División de la columna de periodo entre periodo y anio.
4. Eliminación de registros sin puntaje global.
5. Generación de edades y eliminación de la columna de fecha de nacimiento.
6. Relleno de los registros sin edades con la mediana de la edades existentes.
7. Relleno de datos faltantes de ciertas columnas con "No sabe" o "No informa" para no perder información.

Cabe aclarar que no se hizo una limpieza total para tener material a manipular en Power BI, que es nuestra herramienta de visualización.  




