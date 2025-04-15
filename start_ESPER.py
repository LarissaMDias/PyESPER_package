"""
Accessory file for example runs. Downloads GLODAP file for test runs.
"""
 
import numpy as np
from scipy.io import loadmat
from lir import lir

data = loadmat("GLODAPv2.2022_Merged_Master_File.mat") 

latitude_array = np.squeeze(data['G2latitude'][500:1000])
latitude = latitude_array.tolist()
longitude_array = np.squeeze(data['G2longitude'][500:1000])
longitude = longitude_array.tolist()
depth_array = np.squeeze(data['G2depth'][500:1000])
depth = depth_array.tolist()
salinity_array = np.squeeze(data['G2salinity'][500:1000])
salinity = salinity_array.tolist()
temperature_array = np.squeeze(data['G2temperature'][500:1000])
temperature = temperature_array.tolist()
phosphate_array = np.squeeze(data['G2phosphate'][500:1000])
phosphate = phosphate_array.tolist()
nitrate_array = np.squeeze(data['G2nitrate'][500:1000])
nitrate = nitrate_array.tolist()
silicate_array = np.squeeze(data['G2silicate'][500:1000])
silicate = silicate_array.tolist()
oxygen_array = np.squeeze(data['G2oxygen'][500:1000])
oxygen = oxygen_array.tolist()

OutputCoordinates = {}
PredictorMeasurements = {}

OutputCoordinates.update({"longitude": longitude, 
                          "latitude": latitude, 
                          "depth": depth})

PredictorMeasurements.update({"salinity": salinity, 
                              "temperature": temperature, 
                              "phosphate": phosphate, 
                              "nitrate": nitrate, 
                              "silicate": silicate, 
                              "oxygen": oxygen
                             })

MeasUncerts = {'sal_u': [0.001], 'temp_u': [0.3], 'phosphate_u': [0.14], 'nitrate_u':[0.5], 'silicate_u': [0.03], 'oxygen_u': [0.025]}

EstDates_array = np.squeeze(data['G2year'][500:1000])
EstDates = EstDates_array.tolist()

Path = '/Users/larissadias/Documents/Python/PyESPER'
             
lir(['DIC'], Path, OutputCoordinates, PredictorMeasurements, EstDates=EstDates, Equations=[1])

