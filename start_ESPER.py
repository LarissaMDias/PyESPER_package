"""
Accessory file for example runs. 
"""
 
import numpy as np
from scipy.io import loadmat
from lir import lir

data = loadmat("data/GLODAPv2.2022_Merged_Master_File.mat") 

latitude_array = np.squeeze(data['G2latitude'][750:760])
latitude = latitude_array.tolist()
longitude_array = np.squeeze(data['G2longitude'][750:760])
longitude = longitude_array.tolist()
depth_array = np.squeeze(data['G2depth'][750:760])
depth = depth_array.tolist()
salinity_array = np.squeeze(data['G2salinity'][750:760])
salinity = salinity_array.tolist()
temperature_array = np.squeeze(data['G2temperature'][750:760])
temperature = temperature_array.tolist()
phosphate_array = np.squeeze(data['G2phosphate'][750:760])
phosphate = phosphate_array.tolist()
nitrate_array = np.squeeze(data['G2nitrate'][750:760])
nitrate = nitrate_array.tolist()
silicate_array = np.squeeze(data['G2silicate'][750:760])
silicate = silicate_array.tolist()
oxygen_array = np.squeeze(data['G2oxygen'][750:760])
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

EstDates_array = np.squeeze(data['G2year'][750:760])
EstDates = EstDates_array.tolist()

Path = '/Users/lara/Documents/Python/PyESPER'
             
lir(['TA', 'pH'], Path, OutputCoordinates, PredictorMeasurements, EstDates=EstDates, Equations=[1, 16])

