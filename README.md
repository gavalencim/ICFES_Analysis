# Análisis Icfes
El siguiente proyecto presenta una propuesta de obtención, limpieza y visualización de datos para un dataset que contiene información sobre los resultados del las pruebas saber ICFES en colombia durante el periodo que comprendió entre 2014 a 2022. 

El conjunto de datos se puede obtener del siguiente link https://www.datos.gov.co/Educaci-n/Resultados-nicos-Saber-11/kgxf-xxbe/about_data

## Obtención de datos
A pesar de que los datos se pueden obtener en un formato de texto plano tipo CSV en el link proporcionado, para los propósitos de este proyecto se eligió usar la API correspondiente, que también se encuentra en el sitio web mencoinado anteriormente. 

API: https://www.datos.gov.co/resource/kgxf-xxbe.json

Para la obtención de los datos se usaron las siguiente librerías de Python:
import requests
import pandas as pd
import time

