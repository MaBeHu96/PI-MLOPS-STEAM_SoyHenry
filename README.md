# PI-MLOPS-STEAM_SoyHenry
Proyecto Individual MLOPS
 ## Proyecto de Predicción de Precios de Videojuegos en Steam
Bienvenido al proyecto de predicción de precios de videojuegos en Steam. En este proyecto, hemos desarrollado un modelo de machine learning capaz de predecir el precio de los videojuegos en la plataforma Steam. A lo largo de este README, te proporcionaremos información sobre cómo abordamos el proyecto y cómo puedes utilizar nuestra solución.

Ciclo de Vida del Proyecto
Nuestro enfoque para este proyecto sigue el ciclo de vida de un proyecto de machine learning, abordando desde la recolección y tratamiento de datos hasta el entrenamiento y mantenimiento del modelo.

Rol a Desarrollar
En este proyecto, asumimos el rol de Data Scientist en Steam. Nuestra misión es crear un modelo de machine learning que prediga el precio de los videojuegos en la plataforma. Sin embargo, nos enfrentamos a desafíos de datos como datos anidados y falta de procesos automatizados para la actualización de productos.

Propuesta de Trabajo
A continuación, detallamos los pasos clave que hemos seguido para abordar este proyecto:

Transformaciones de Datos
Para este MVP, hemos enfocado nuestros esfuerzos en leer los datos en el formato correcto. Si bien no hemos realizado transformaciones exhaustivas en el conjunto de datos, hemos asegurado que esté listo para su consumo.

Desarrollo de la API
Hemos creado una API utilizando el framework FastAPI para hacer que los datos estén disponibles. Hemos implementado las siguientes funciones de consulta:

genero(Año: str): Proporciona una lista con los 5 géneros más vendidos en un año específico.
juegos(Año: str): Devuelve una lista con los juegos lanzados en un año determinado.
specs(Año: str): Retorna una lista con los 5 specs que más se repiten en un año.
earlyacces(Año: str): Muestra la cantidad de juegos lanzados en un año con early access.
sentiment(Año: str): Basado en el año de lanzamiento, devuelve una lista con el análisis de sentimiento.
metascore(Año: str): Presenta los 5 juegos con mayor metascore en un año.
Despliegue
Hemos implementado el despliegue de nuestra API utilizando el servicio Render, lo que nos permite acceder a la API desde la web de manera sencilla y eficiente.

Análisis Exploratorio de Datos (EDA)
Antes de entrenar el modelo, hemos realizado un análisis exploratorio de los datos. Hemos investigado las relaciones entre las variables, identificado outliers y patrones interesantes en los títulos de los juegos. En lugar de utilizar herramientas automáticas para EDA, hemos aplicado conceptos y técnicas para una comprensión más profunda de los datos.

Modelo de Predicción
Finalmente, hemos desarrollado un modelo de machine learning para predecir los precios de los videojuegos. Hemos considerado características como género, año y metascore para construir un modelo sólido. Nuestra API permite realizar consultas para obtener predicciones de precios y evaluación del modelo.

Contribuciones
Este proyecto ha sido desarrollado por Mateo Betancourt H.
