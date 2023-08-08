# PI-MLOPS-STEAM_SoyHenry
Proyecto Individual MLOPS
 # Proyecto de Predicción de Precios de Videojuegos en Steam
Bienvenido al proyecto de predicción de precios de videojuegos en Steam. En este proyecto, e desarrollado un modelo de machine learning capaz de predecir el precio de los videojuegos en la plataforma Steam. A lo largo de este README, proporcionare información sobre cómo aborde el proyecto y cómo puedes utilizar nuestra solución.

## Ciclo de Vida del Proyecto
mi enfoque para este proyecto sigue el ciclo de vida de un proyecto de machine learning, abordando desde la recolección y tratamiento de datos hasta el entrenamiento y mantenimiento del modelo.

## Rol a Desarrollar
En este proyecto, asumí el rol de Data Scientist en la plataforma de Steam.y el objetivo era crear un modelo de machine learning que prediga el precio de los videojuegos en la plataforma. Sin embargo, nos enfrentamos a desafíos de datos como datos anidados y falta de procesos automatizados para la actualización de productos.

## Propuesta de Trabajo
A continuación, detallamos los pasos clave que hemos seguido para abordar este proyecto:

## Transformaciones de Datos
Para este proyecto ,enfoque mis esfuerzos en leer los datos en el formato correcto y decidi crear para cada endpoint un archivo .csv que facilita y optimiza cada una de las consultas, Si bien no he realizado transformaciones exhaustivas en el conjunto de datos, puedo garantizar una buena calidad de los mismos.

## Desarrollo de la API
Cree una API utilizando el framework FastAPI para hacer que los datos estén disponibles. Implementado las siguientes funciones de consulta:

en el archivo main.py se pede ver cada una de las funciones y en el archivo ETL_juegos.ipynb estan las mismas funciones el cual tambien sirve como evidencia del funcionamiento 
genero(Año: str): Proporciona una lista con los 5 géneros más vendidos en un año específico.
juegos(Año: str): Devuelve una lista con los juegos lanzados en un año determinado.
specs(Año: str): Retorna una lista con los 5 specs que más se repiten en un año.
earlyacces(Año: str): Muestra la cantidad de juegos lanzados en un año con early access.
sentiment(Año: str): Basado en el año de lanzamiento, devuelve una lista con el análisis de sentimiento.
metascore(Año: str): Presenta los 5 juegos con mayor metascore en un año.
## Despliegue
tambien se implemento el despliegue de nuestra API utilizando el servicio Render, lo que nos permite acceder a la API desde la web de manera sencilla y eficiente.

## Análisis Exploratorio de Datos (EDA)
Antes de entrenar el modelo,  realicé un análisis exploratorio de los datos. Investigando las relaciones entre las variables, identificado outliers y patrones interesantes en los títulos de los juegos. En lugar de utilizar herramientas automáticas para EDA, he aplicado conceptos y técnicas para una comprensión más profunda de los datos.

## Modelo de Predicción
Finalmente, desarrolle un modelo de machine learning para predecir los precios de los videojuegos. considere características como género, año y metascore para construir un modelo sólido. La API permite realizar consultas para obtener predicciones de precios y evaluación del modelo.

