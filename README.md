# Análisis Icfes
El siguiente proyecto presenta una propuesta de obtención, limpieza y visualización de datos para un dataset que contiene información sobre los resultados del las pruebas saber ICFES en colombia durante el periodo que comprendió entre 2014 a 2022 con más de 7 millones de registros. 

El conjunto de datos se puede obtener del siguiente link https://www.datos.gov.co/Educaci-n/Resultados-nicos-Saber-11/kgxf-xxbe/about_data

## Contenido del proyecto:
- obtencion_all_data.py: Script que obtiene la información desde la API y devuelve un CSV con toda la información.
- data_cleaning.py: Script que explora la limpieza de los datos para su uso posterior.
- index.html: Script donde se expone el dashboard de Power BI creado a partir de los datos limpios.
En la siguiente página se puede ver el dashboard https://gavalencim.github.io/ICFES_Analysis/

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
8. Carga de los datos "limpios" a un archivo de texto plato CSV.

Cabe aclarar que no se hizo una limpieza total para tener material a manipular en Power BI, que es nuestra herramienta de visualización.  

## Limpieza de datos con Power Query de Power BI
Luego de cargar el CSV de los datos limpios de Python a Power BI, se hicieron las siguientes modificaciones a los datos:
1. División sobre 10 de la columnas que contenían puntajes pues aparecían en rangos de miles y no cientos o decenas.
2. Filtrado sobre la columna de ubicación de colegio para sólo tener entradas cuya columna de ubicación del colegio tuviera el valor "RURAL" o "URBANO"
3. Remoción de errores en la columna de periodo.
4. Filtrado sobre la columna de bilinguismo del colegio para sólo tener entradas cuya columna de bilinguismo del colefio tuviera un valor de "True" o "False" o "No informa".
5. Filtrado de las columnas relacionadas al caracter del colegio, la cantidad de personas en el hogar y la cantidad de cuartos o habitaciones en el hogar para que no contuvieran valores nulos.
6. Filtrado de la columna de la edad para que no tener entradas con edades por debajo de loa 10 anios ni por encima de los 85.

Todas estas alteraciones se hicieron teniendo en cuenta la importacia y validez de los errores y datos de las columnas.

## Visualiación de datos con Power BI
La visualiazación consta de una hoja de índice, cuatro hojas de informe (Informe general, informe de perfil de los estudiantes, informe de contexto familiar e informe de características del colegio), y tres hjas de tootips para ahondar en la información de los informes presentados. El informe final se puede ver la siguiente página https://gavalencim.github.io/ICFES_Analysis/




