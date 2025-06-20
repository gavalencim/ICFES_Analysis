
import pandas as pd
import math
import numpy as np

input_file = "icfes_full_data.csv" # Archivo de entrada
output_file = "icfes_limpio.csv" # Archiva de salida


# CARGAR ARCHIVOS SUCIO
df = pd.read_csv(input_file) # Carga de archivos


# SELECCIONAR COLUMNAS
columns = ["periodo",
           "estu_tipodocumento",
           "cole_area_ubicacion",
           "cole_bilingue",
           "cole_calendario",
           "cole_caracter",
           "cole_genero",
           "cole_jornada",
           "cole_depto_ubicacion",
           "cole_mcpio_ubicacion",
           "cole_naturaleza",
           "cole_nombre_establecimiento",
           "cole_sede_principal",
           "estu_depto_presentacion",
           "estu_mcpio_presentacion",
           "estu_pais_reside",
           "estu_depto_reside",
           "estu_mcpio_reside",
           #"estu_estudiante",
           "estu_nacionalidad",
           "estu_fechanacimiento",
           "estu_genero",
           "estu_privado_libertad",
           "fami_cuartoshogar",
           "fami_educacionmadre",
           "fami_educacionpadre",
           "fami_estratovivienda",
           "fami_personashogar",
           "fami_tienecomputador",
           "fami_tieneinternet",
           "desemp_ingles",
           "punt_ingles",
           "punt_matematicas",
           "punt_sociales_ciudadanas",
           "punt_c_naturales",
           "punt_lectura_critica",
           "punt_global"
           ]

df = df[columns]


# AJUSTAR TIPOS DE DATOS 
    #   Datos numéricos
number_atribute = [
           "punt_ingles",
           "punt_matematicas",
           "punt_sociales_ciudadanas",
           "punt_c_naturales",
           "punt_lectura_critica",
           "punt_global"
           ]

for col in number_atribute: # Ciclo para tomar cada columna numérica (con puntajes) y volverla a número
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["estu_fechanacimiento"] = pd.to_datetime(df["estu_fechanacimiento"], errors="coerce") # Fecha de nacimiento ajustada como tipo de dato fecha

    #   Datos booleanos (Si o no)
df.loc[df["cole_bilingue"]=="N", "cole_bilingue"] = False # Cambio de datos negativos por False
df.loc[df["cole_bilingue"]=="S", "cole_bilingue"] = True # Cambio de datos positivos por True
df.loc[df["fami_tieneinternet"]=="No", "fami_tieneinternet"] = False # Cambio de datos negativos por False
df.loc[df["fami_tieneinternet"]=="Si", "fami_tieneinternet"] = True # Cambio de datos positivos por True
df.loc[df["fami_tienecomputador"]=="No", "fami_tienecomputador"] = False # Cambio de datos negativos por False
df.loc[df["fami_tienecomputador"]=="Si", "fami_tienecomputador"] = True # Cambio de datos positivos por True
df.loc[df["estu_privado_libertad"]=="N", "estu_privado_libertad"] = False # Cambio de datos negativos por False
df.loc[df["estu_privado_libertad"]=="S", "estu_privado_libertad"] = True # Cambio de datos positivos por True
df.loc[df["cole_sede_principal"]=="N", "cole_sede_principal"] = False # Cambio de datos negativos por False
df.loc[df["cole_sede_principal"]=="S", "cole_sede_principal"] = True # Cambio de datos positivos por True


    #   Datos de estrato (de cadena a numero)
df["fami_estratovivienda"] = df["fami_estratovivienda"].map({
    "Estrato 1": 1,
    "Estrato 2": 2,  
    "Estrato 3": 3,
    "Estrato 4": 4,
    "Estrato 5": 5,  
    "Estrato 6": 6
})

    #   Datos de personas en vivienda
df["fami_personashogar"] = df["fami_personashogar"].astype(str).str.strip().str.title() # Capitalizar los valores

df["fami_personashogar"] = df["fami_personashogar"].replace("Nan", np.nan) # Restaurar los NaN que fueron convertidos a "Nan" por el .astype(str)

# Función corregida
def clasificar_personas_hogar(valor):
    if pd.isna(valor):
        return np.nan  # deja el NaN sin modificar

    nombres_1_2 = ["Uno", "Dos"]
    nombres_3_4 = ["Tres", "Cuatro"]
    nombres_5_6 = ["Cinco", "Seis"]
    nombres_7_8 = ["Siete", "Ocho"]
    nombres_9_10 = ["Nueve", "Diez"]
    rangos_validos = ["1 A 2", "3 A 4", "5 A 6", "7 A 8", "9 A 10"]

    if valor in nombres_1_2:
        return "1 a 2"
    elif valor in nombres_3_4:
        return "3 a 4"
    elif valor in nombres_5_6:
        return "5 a 6"
    elif valor in nombres_7_8:
        return "7 a 8"
    elif valor in nombres_9_10:
        return "9 a 10"
    elif valor in rangos_validos:
        return valor  # ya está bien
    else:
        return "Más de 10"

# Aplicamos la función
df["fami_personashogar"] = df["fami_personashogar"].apply(clasificar_personas_hogar)


# DIVISIÓN DE COLUMNA PERIODO EN PERIODO Y ANIO
def cut_semester(periodo):
    periodo = periodo/10 # Divide el periodo por 10
    return math.trunc(periodo) # Quita los decimales (el periodo) para dejar solo el anio
def cut_year(periodo):
    return periodo%10 # Hace división por 10 del periodo y devuelve el residuo, o sea el periodo

df["anio"] = df["periodo"].apply(cut_semester) # Aplica la función para quitar el periodo a la nueva columna de anio
df["periodo"] = df["periodo"].apply(cut_year) # Aplica la función para quitar el anio a la columna de periodo


# MANEJO DE DATOS FALTANTES
#faltantes = df.isna().mean().sort_values(ascending=False) # Porcentaje de datos faltantes por columna
#print(faltantes * 100)
    #   No necesito datos sin puntaje global
df = df[df["punt_global"].notna()] # Elimina datos sin puntaje global

    #   Para datos faltantes de la fecha y la generación de edades:
df["edad"] = df["anio"] - df["estu_fechanacimiento"].dt.year # Genera una columna de la edad 
age_median = df["edad"].median() # Calcula la mediana porque es mas robusta para valores atípicos
df["edad"] = df["edad"].fillna(age_median) # Relleno los valores vacíos de la edad con la mediana de la edad
df["edad_estimada"] = df["estu_fechanacimiento"].isna() # Crea una nueva columna que marca las filas con edades estimadas

    #   Eliminar la columna de fecha de nacimiento
df = df.drop(columns=["estu_fechanacimiento"])

#faltantes = df.isna().mean().sort_values(ascending=False) # Porcentaje de datos faltantes por columna
#print(faltantes * 100)
    
    #   Relleno de datos faltantes
df["cole_bilingue"] = df["cole_bilingue"].fillna("No informa")
df["fami_educacionmadre"] = df["fami_educacionmadre"].fillna("No sabe")
df["fami_educacionpadre"] = df["fami_educacionpadre"].fillna("No sabe")
df["fami_estratovivienda"] = df["fami_estratovivienda"].fillna("No informa")

df.to_csv(output_file, index=False)
