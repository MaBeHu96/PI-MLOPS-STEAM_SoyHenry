from fastapi import FastAPI
import pandas as pd
import ast

app = FastAPI(title="Proyecto MLOPS-STEAM")

## ruta local es : http://127.0.0.1:8000

#  Se ingresa un año y devuelve una lista con los 5 géneros más vendidos en el orden correspondiente.
@app.get("/genero/{year: str}")
def genero(year):
    # cargo el dataset y le aplico la librea ast par poder utilizar los datos de la columna 'genres' y poder hacer las consultas
    df_genero= pd.read_csv('Data/generos.csv')
    df_genero['genres'] = df_genero['genres'].apply(ast.literal_eval)

    if year == 9999:
        print ("NO SE TIENE UN REGISTRO PRECISO DE LA LISTA DE GENEROS  PARA EL AÑO INGRESADO, ES UNA RECOPILACION DE LOS POSIBLES GENEROS ")
    
    df_anio = df_genero[df_genero['release_year'] == year]
   
    if df_anio.empty:
        return {"VALUE_ERROR": "NO EXISTEN DATOS DISPONIBLES PARA EL AÑO INGRESADO"}
    
    count_genres = df_anio['genres'].explode().value_counts().to_dict()
    top_genres = dict(sorted(count_genres.items(), key=lambda item: item[1], reverse=True)[:5])
    
    return top_genres

#Se ingresa un año y devuelve un diicionario con la lista de juegos lanzados en el año.
@app.get("/juegos/{year: str}")
def juegos(year):
    df_juegos = pd.read_csv('Data/juegos.csv')

    if year == 9999:
        print ("NO SE TIENE UN REGISTRO PRECISO DE LA LISTA DE JUEGOS  PARA EL AÑO INGRESADO, ES UNA RECOPILACION DE LOS POSIBLES JUEGOS ")
    df_anio = df_juegos[df_juegos['release_year'] == year]
    
    if df_anio.empty:
        return {"VALUE_ERROR": "NO EXISTEN DATOS DISPONIBLES PARA EL AÑO INGRESADO"}
    
    df_anio['app_name'] = df_anio['app_name'].astype(str)
    juegos_lanzados = df_anio['app_name'].astype(str).tolist()
    cantidad_juegos = len(juegos_lanzados)
    
    return {"Año": year, "Cantidad de Juegos": cantidad_juegos, "Juegos Lanzados": juegos_lanzados}

#Se ingresa un año y devuelve una lista con los 5 specs que más se repiten en el mismo en el orden correspondiente.
@app.get("/specs/{year: str}")
def specs(year):
    #cargo el dataset y luego realizo la trnasformacion correspondiente para que el codigo me muestre las listas y no las cadenas de la columna 'specs'
    df_specs = pd.read_csv('Data/specs.csv')
    df_specs['specs'] = df_specs['specs'].apply(ast.literal_eval)

    if year == 9999:
        print ("NO SE TIENE UN REGISTRO PRECISO DE LA LISTA DE ESPECIFICACIONES  PARA EL AÑO INGRESADO, ES UNA RECOPILACION DE LAS POSIBLES ESPEIFICACIONES ")
    df_anio = df_specs[df_specs['release_year'] == year]
    
    if df_anio.empty:
        return {"VALUE_ERROR": "NO EXISTEN DATOS DISPONIBLES PARA EL AÑO INGRESADO"}
    
    count_specs = df_anio['specs'].explode().value_counts().to_dict()
    top_specs = dict(sorted(count_specs.items(), key=lambda item: item[1], reverse=True)[:5])
    
    return {'Año': year, 'Especificaciones': top_specs}


#Cantidad de juegos lanzados en un año con early access.
@app.get("/earlyacces/{year: str}")
def earlyacces(year):
    df_earlyacces = pd.read_csv('Data/earlyaccess.csv')
    if year == 9999:
        print ("NO SE TIENE UN REGISTRO PRECISO DE LA LISTA DE ACCESOS TEMPRANOS  PARA EL AÑO INGRESADO, ES UNA RECOPILACION DE LOS POSIBLES ACCESOS TEMPRANOS")
    filtro = (df_earlyacces['release_year'] == year) & (df_earlyacces['early_access'] == True)
    df_year_earlyacces = df_earlyacces[filtro]
    
    if df_year_earlyacces.empty:
        return{"VALUE_ERROR": "NO EXISTEN DATOS DISPONIBLES PARA EL AÑO INGRESADO, INTENTE CON OTRA FECHA"}
    
    count_earlyacces = df_year_earlyacces.shape[0]
    return {"Año": year, "Cantidad de Juegos lanzados con early access": count_earlyacces}


#Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.
@app.get("/sentiment/{year: str}")
def sentiment(year):
    df_sentiment = pd.read_csv('Data/sentiments.csv')
    if year == 9999:
        print ("NO SE TIENE UN REGISTRO PRECISO DE LA LISTA DE SENTIMIENTOS  PARA EL AÑO INGRESADO, ES UNA RECOPILACION DE LOS POSIBLES SENTIMIENTOS ")
    df_anio = df_sentiment[df_sentiment['release_year'] == year] 
    
    if df_anio.empty:
        return {"VALUE_ERROR": "NO EXISTEN DATOS DISPONIBLES PARA EL AÑO INGRESADO, INTENTE CON OTRA FECHA"}
    
    conteo_sentimientos = df_anio['sentiment'].value_counts().to_dict()
    return {'Año': year, 'Análisis de sentimiento': conteo_sentimientos}


#Top 5 juegos según año con mayor metascore.
@app.get("/metascore/{year: str}")
def metascore(year):
    df_metascore = pd.read_csv('Data/metascore.csv')
    
    if year == 9999:
        print ("NO SE TIENE UN REGISTRO CLARO DE LA LISTA DE JUEGOS ,NI SU AÑO DE LANZAMIENTO ")
    
    df_anio = df_metascore[df_metascore['release_year'] == year ]
    if df_anio['metascore'].notna().any():
        top_juegos = df_anio.nlargest(5, 'metascore')[['app_name', 'metascore']].to_dict('registros_records')
        return {'Año': year,'registros_records': top_juegos}
    
    else:
        return {"VALUE_ERROR": "NO EXISTEN REGISTROS DISPONIBLES PARA EL AÑO INGRESADO, INTENTE CON OTRA FECHA"} 

  