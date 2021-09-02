# -*- coding: utf-8 -*-
"""
Created on Mon Aug 02 15:45:22 2021

@author: scheibe
"""

from netCDF4 import Dataset
import numpy as np
import numpy.ma as ma
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

BASEDIR = Path('C:/Users/scheibe/Desktop/Flood_defence_project/data/')

Hist_Extreme_Sea_Level  = Dataset(BASEDIR / Path(f'seaLevelAnom_marine-sim_rcp26_ann_2007-2100.nc'),'r')

# eewl- episodic extreme water level [m]
# esl - extreme sea level [m]
# ensmbl - Relative Sea Level Rise ensemble; 1: min, 2: mean, 3: max
# rp - return period [years]; start: 01-Dec-1969, end: 30-Nov-2004
# latitude - degrees_north
# longitude - degrees_east

latitude = pd.DataFrame(Hist_Extreme_Sea_Level.variables['latitude'][:]) # shape (135 1)
longitude = pd.DataFrame(Hist_Extreme_Sea_Level.variables['longitude'][:]) # shape (150, 1)
percentile = pd.DataFrame(Hist_Extreme_Sea_Level.variables['percentile'][:]) # shape (9,1)
time = pd.DataFrame(Hist_Extreme_Sea_Level.variables['time'][:]) # shape (94,1)

seaLevelAnom = pd.DataFrame(Hist_Extreme_Sea_Level.variables['seaLevelAnom'][:]) # 


df1 = pd.DataFrame(station_x_coordinate)
df1.insert(1, "station_y_coordinate", station_y_coordinate)

outfilepath = "{}/stations_x_y.csv".format(BASEDIR)
df1.to_csv(outfilepath)
print(outfilepath)

 # Delfzijl: lon 53.3264 corresponds to degree_east, lat 6.9331 corresponds to degree_north
 
#NDL	Den Helder	Dec1970-Dec2014	denhelder-hel-nl-rws	Helpdesk Water	52.965	4.7464
#NDL	Hoek van Holland	Dec1970-Dec2014	hoekvanholla-hvh-nl-rws	Helpdesk Water	51.9775	4.12
#NDL	Delfzijl	Dec1970-Dec2014	delfzijl-del-nl-rws	Helpdesk Water	53.3264	6.9331
 
#ISO3	Country Namelat_min	lat_max	, lon_min	lon_max
#NLD	
# Box: 3.278320,51.513716,7.046631,53.680801 ; http://bboxfinder.com/#51.513716,3.278320,53.680801,7.046631
 
#22031	6.936035(East)	53.327636 (North) ---> Delfzijl
#22036	7.214355	53.327636 ---> Emden
# 3832	5.134277	53.34228  ---> Wattenmeer
#22157	6.936035	53.32764 ---> ebenfalls Delfzijl

Delfzijl = AHHW[22031]
Emden = AHHW[22036]
Wattenmeer = AHHW[3832]

timescale = pd.date_range('1977', periods=29, freq='1AS') #https://riptutorial.com/pandas/example/6438/create-a-sample-dataframe-with-datetime

#matplotlib inline
#plt.style.use('seaborn-whitegrid')

plt.subplot(3, 1, 1) #, figsize=(15, 20))#, dpi=100)#, sharex=True))
plt.plot(timescale,Delfzijl, 'o-')
plt.title('Historical water level for Delfzijl, Emden & Wattenmeer (NDL)')
plt.ylabel('Water level [m]')

plt.subplot(3, 1, 2)
plt.plot( timescale,Emden,'.-')
plt.xlabel('Time')
plt.ylabel('Water level [m]')

plt.subplot(3, 1, 3)
plt.plot( timescale,Wattenmeer,'.-')
plt.xlabel('Time')
plt.ylabel('Water level [m]')
plt.tight_layout()  
#plt.show()

plt.savefig('{}/waterlevel_NDL_hist.pdf'.format(BASEDIR))

#####################################################################################################

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:59:03 2020

@author: scheibe
"""



from netCDF4 import Dataset
import numpy as np
import numpy.ma as ma
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import xarray as xr

BASEDIR = Path("C:/Users/scheibe/Desktop/Flood_defence_project/data/AR5/")

ENS_ts_RCP_45_85  = Dataset(BASEDIR / Path(f'ocean-only-ens-time-series-rcp45-rcp85.nc'),'r')
#rcp45_ens = pd.DataFrame(ENS_ts_RCP_45_85.variables['rcp45_ens'][:]) # 
rcp85_ens = pd.DataFrame(ENS_ts_RCP_45_85.variables['rcp85_ens'][:]) # 
time2 = pd.DataFrame(ENS_ts_RCP_45_85.variables['time2'][:]) # shape (3, 1)
time = pd.DataFrame(ENS_ts_RCP_45_85.variables['time'][:]) # shape (8, 1)
latitude = pd.DataFrame(ENS_ts_RCP_45_85.variables['lat'][:]) # shape (11014, 1)
longitude = pd.DataFrame(ENS_ts_RCP_45_85.variables['lon'][:]) # shape (11014, 1)

df1 = pd.DataFrame(longitude)
df1.insert(1, "lat", latitude)

outfilepath = "{}/lon_lat.csv".format(BASEDIR)
df1.to_csv(outfilepath)
print(outfilepath)

DS = xr.open_dataset('C:/Users/scheibe/Desktop/Flood_defence_project/data/AR5/ocean-only-ens-time-series-rcp45-rcp85.nc')
lat_DF = DS.lat.to_dataframe()
lat_DF.index[143]

lon_DF = DS.lon.to_dataframe()
lon_DF.index[6]

#####################################
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
# this file provides the annual maximum flood depth in each gridcell:
#dph_path = 'flddph_flood_2040_2050_IRL.nc'
# this file provides the annual maximum flooded fraction in each gridcell:
ds_path = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/AR5/ocean-only-ens-time-series-rcp45-rcp85.nc'
# open files
#flood_dph = xr.open_dataset(dph_path)
ds = xr.open_dataset(ds_path)
# save data
lon = ds.lon.data
lat = ds.lat.data
time = ds.time.data
time2 = ds.time2.data

# get only data for first year in file

ds_rcp45 = ds.rcp45_ens.data[18,6,143]
plt.plot(ds_rcp45)
ds_rcp85 = ds.rcp85_ens.data[18,6,143]
plt.plot(ds_rcp85)
