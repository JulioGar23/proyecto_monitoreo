import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff 
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np

#Adquisición de datos de sensores por periodos de tiempo. 

def setup_sensormm(url):
    df = pd.read_csv(url)
    df.drop(columns=['entry_id', 'field1', 'field4', 'field5', 'field6'], inplace=True)
    df.rename(columns={'field2': 'Metano', 'field3': 'Monóxido'}, inplace=True)
    return df

def setup_sensorth(url):
    df = pd.read_csv(url)
    df.drop(columns=['entry_id', 'field4', 'field5', 'field6'], inplace=True)
    df.rename(columns={'field1': 'Humedad', 'field2': 'Temperatura', 'field3':'CO2'}, inplace=True)
    return df

#Datos Metano y Monóxido
sensormm_8_12_Feb = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-02-08offset=UTC-06:00&end=2024-02-12offset=UTC-06:00"
sensormm_12_16_Feb = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-02-12offset=UTC-06:00&end=2024-02-16offset=UTC-06:00"
sensormm_16_20_Feb = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-02-16offset=UTC-06:00&end=2024-02-20offset=UTC-06:00"
sensormm_20_24_Feb = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-02-20offset=UTC-06:00&end=2024-02-24offset=UTC-06:00"
sensormm_24_28_Feb = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-02-24offset=UTC-06:00&end=2024-02-28offset=UTC-06:00"
sensormm_28_2_Mar = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-02-28offset=UTC-06:00&end=2024-03-02offset=UTC-06:00"
sensormm_2_6_Mar = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-03-02offset=UTC-06:00&end=2024-03-06offset=UTC-06:00"
sensormm_6_10_Mar = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-03-06offset=UTC-06:00&end=2024-03-10offset=UTC-06:00"
sensormm_10_14_Mar = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-03-10offset=UTC-06:00&end=2024-03-14offset=UTC-06:00"
sensormm_14_18_Mar = "https://api.thingspeak.com/channels/2378137/feeds.csv?start=2024-03-14offset=UTC-06:00&end=2024-03-18offset=UTC-06:00"


#Datos Temperatura, Humedad y CO2
sensorth_8_12_Feb = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-02-08offset=UTC-06:00&end=2024-02-12offset=UTC-06:00"
sensorth_12_16_Feb = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-02-12offset=UTC-06:00&end=2024-02-16offset=UTC-06:00"
sensorth_16_20_Feb = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-02-16offset=UTC-06:00&end=2024-02-20offset=UTC-06:00"
sensorth_20_24_Feb = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-02-20offset=UTC-06:00&end=2024-02-24offset=UTC-06:00"
sensorth_24_28_Feb = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-02-24offset=UTC-06:00&end=2024-02-28offset=UTC-06:00"
sensorth_28_2_Mar = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-02-28offset=UTC-06:00&end=2024-03-02offset=UTC-06:00"
sensorth_2_6_Mar = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-03-02offset=UTC-06:00&end=2024-03-06offset=UTC-06:00"
sensorth_6_10_Mar = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-03-06offset=UTC-06:00&end=2024-03-10offset=UTC-06:00"
sensorth_10_14_Mar = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-03-10offset=UTC-06:00&end=2024-03-14offset=UTC-06:00"
sensorth_14_18_Mar = "https://api.thingspeak.com/channels/1935500/feeds.csv?start=2024-03-14offset=UTC-06:00&end=2024-03-18offset=UTC-06:00"


#Acondicionamiento de los datos.
datamm_1 = setup_sensormm(sensormm_8_12_Feb)
datamm_2 = setup_sensormm(sensormm_12_16_Feb)
datamm_3 = setup_sensormm(sensormm_16_20_Feb)
datamm_4 = setup_sensormm(sensormm_20_24_Feb)
datamm_5 = setup_sensormm(sensormm_24_28_Feb)
datamm_6 = setup_sensormm(sensormm_28_2_Mar)
datamm_7 = setup_sensormm(sensormm_2_6_Mar)
datamm_8 = setup_sensormm(sensormm_6_10_Mar)
datamm_9 = setup_sensormm(sensormm_10_14_Mar)
datamm_10 = setup_sensormm(sensormm_14_18_Mar)

datath_1 = setup_sensorth(sensorth_8_12_Feb)
datath_2 = setup_sensorth(sensorth_12_16_Feb)
datath_3 = setup_sensorth(sensorth_16_20_Feb)
datath_4 = setup_sensorth(sensorth_20_24_Feb)
datath_5 = setup_sensorth(sensorth_24_28_Feb)
datath_6 = setup_sensorth(sensorth_28_2_Mar)
datath_7 = setup_sensorth(sensorth_2_6_Mar)
datath_8 = setup_sensorth(sensorth_6_10_Mar)
datath_9 = setup_sensorth(sensorth_10_14_Mar)
datath_10 = setup_sensorth(sensorth_14_18_Mar)

#Unión
data_combined_mm = pd.concat([datamm_1, datamm_2, datamm_3, datamm_4, datamm_5, datamm_6, datamm_7, datamm_8, datamm_9, datamm_10])
data_combined_th = pd.concat([datath_1, datath_2, datath_3, datath_4, datath_5, datath_6, datath_7, datath_8, datath_9, datath_10])

# Ajuste de las fechas. 
# En los datos que se descargan del sitio, tienen una diferencia horaria de 6 horas.
data_combined_mm['created_at'] = pd.to_datetime(data_combined_mm['created_at'])- pd.Timedelta(hours=6)
data_combined_th['created_at'] = pd.to_datetime(data_combined_th['created_at'])- pd.Timedelta(hours=6)
data_combined_mm['created_at'] = data_combined_mm['created_at'].dt.strftime('%Y-%m-%d %H:%M')
data_combined_th['created_at'] = data_combined_th['created_at'].dt.strftime('%Y-%m-%d %H:%M')

#Verificación de la consistencia de datos.
data_combined_mm = data_combined_mm.sort_values(by='created_at')
data_combined_th = data_combined_th.sort_values(by='created_at')

print("Número de filas SIN ACONDICIONAMIENTO en data_combined_mm:")
print(len(data_combined_mm))
print("Número de filas SIN ACONDICIONAMIENTO en data_combined_mm:")
print(len(data_combined_th))

data_combined_mm = data_combined_mm.drop_duplicates(subset='created_at')
data_combined_th = data_combined_th.drop_duplicates(subset='created_at')
data_combined_mm.dropna(inplace=True)
data_combined_th.dropna(inplace=True)

print("Número de filas ACONDICIONADAS en data_combined_mm:")
print(len(data_combined_mm))
print("Número de filas ACONDICIONADAS en data_combined_th:")
print(len(data_combined_th))