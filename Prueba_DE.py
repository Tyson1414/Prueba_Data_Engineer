import requests
import json
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
"""
Según la documentación de Socrata Open Data API cada conjunto de datos se representa por un identificador único
de ocho caracteres alfanuméricos divididos en dos frases de cuatro caracteres cada una, separadas por un guion.
La url + el unique id y sin la extensión .json nos lleva a una página web con la descripción de los datos
"""

resource = "https://datos.gov.co/resource/"
parameter = "7cci-nqqb.json"
url = resource + parameter

# Realiza la solicitud GET al enlace y guarda la respuesta en la variable data, luego lo convertimos en un dataframe
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
print(df)