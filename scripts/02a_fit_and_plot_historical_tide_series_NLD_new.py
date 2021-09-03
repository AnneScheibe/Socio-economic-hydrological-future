# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:53:10 2020

@author: scheibe
"""

from scipy.stats import gumbel_r
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tide_series_file_NLD = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/input_data/calibration/NLD/yearly_maxima/max_delf.csv'
tide_series_NLD = pd.read_csv(tide_series_file_NLD, sep=";", index_col=2)
tide_series_NLD = tide_series_NLD["DELFZIJL_HOOGSTE_HOOGWATER_PER_JAAR_IN_CM_plus_NAP"].values/100

mu_beta_from_hist_timeseries = gumbel_r.fit(tide_series_NLD)
print(mu_beta_from_hist_timeseries)
# olddata # mu, beta = 2.048638063558476, 0.4965320953010091 # location and scale for NLD from history time serie
mu, beta = 2.9374338664456046, 0.4832749358875801

fig, ax1 = plt.subplots()
x= np.linspace(0, 20, 300)
fig.suptitle('Netherlands: Fit by historical observations \n Histogram and probability density function', fontsize= 12)
color = 'tab:blue'
ax1.set_ylabel('Frequency', color=color)  # we already handled the x-label with ax1
plt.hist(tide_series_NLD, 30, density=True, label='histogram')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xlim(0,6)
ax1.set_ylim(ymin=0)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_xlabel('Water level [m]')
ax2.set_ylabel('Probability density', color=color)
#info: the Maximum should be approximately at loc
ax2.plot(x,gumbel_r.pdf(x, loc=mu, scale=beta),linewidth=2, color='r', label='probability density function')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(ymin=0)


fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.grid(True)
#plt.legend()
plt.savefig('C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/plots/NLD/NLD_Distribution_pfd_by_hist_time_series_new.pdf')

######################################################################################################
####   Draw samples from the distribution:
######################################################################################################
#mu, beta = 2.048638063558476, 0.4965320953010091 # location and scale for NLD from history time series
#
## Years for ISIMIP projections
#years = [2006, 2007,2008,2009,2010,
#         2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,
#         2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,
#         2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,
#         2071,2072,2073,2074,2075,2076,2077,2078,2079,2080,2081,2082,2083,2084,2085,2086,2087,2088,2089,2090,
#         2091,2092,2093,2094,2095,2096,2097,2098,2099]
#
#df = []
#np.random.seed(1) # Makes sure that always the same sample is drawn
#for i in range(len(years)):
#    
#    for j in range(10000):
#        print("run_id{}".format(j))
#        
#        a = np.random.gumbel(mu, beta, 1)
#        a = a[0]
#        print(a)
#    
#        df.append({"projected_waterlevel": a,
#                   "time": years[i],
#                   "run_id": j,})
#    
#    data = pd.DataFrame.from_records(df, index="time")
#    data = data.pivot(columns='run_id', values='projected_waterlevel')
#    #data.to_csv("{}output/projections/data/NDL_sampled_waterlevel_projections_without_slr.csv".format(basedir))
#    data.to_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/NLD/NLD_Sampled_waterlevel_projections_without_slr_from_history.csv")
#

