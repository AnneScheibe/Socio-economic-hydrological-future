# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:41:36 2021

@author: scheibe
"""

#https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
import numpy as np
from scipy import interpolate
import pandas as pd
import matplotlib.pyplot as plt


# CHARCHANGA [1496] (Bkgd: 0.93 +/- 3.07 mm/y)
# COX'S BAZAAR [1476] (Bkgd: -1.01 +/- 3.08 mm/y)
# DELFZIJL [24] (Bkgd: 0.18 +/- 0.18 mm/y)

# former interpolation in script: 'C:/Users/scheibe/Desktop/Flood_defence_project/data/historical_calibration/BGD/read_plot_tide_data.py'

####################################################################################
# Interpolation ID24
####################################################################################
#basdir = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/'
#
#slr_data = pd.read_csv('{}input_data/projections/SLR_ID24.csv'.format(basdir), sep = ';')#, index_col = 0)
#
#def fill_nan(A):
#    '''
#    interpolate to fill nan values
#    '''
#    inds = np.arange(A.shape[0])
#    good = np.where(np.isfinite(A))
#    f = interpolate.interp1d(inds[good], A[good],bounds_error=False)
#    B = np.where(np.isfinite(A),A,f(inds))
#    return B
#
#slr_data_85_perc_95 = fill_nan(slr_data['85_perc_95'].values)
#
#interplated_slr = pd.DataFrame(slr_data['year'].values)
#interplated_slr.columns = ['time']
#interplated_slr.insert(1, "85_perc_95", slr_data_85_perc_95)
#interplated_slr.set_index('time', inplace=True)
#
#slr_data_85_perc_99_5 = fill_nan(slr_data['85_perc_99_5'].values)
#interplated_slr.insert(1, '85_perc_99_5', slr_data_85_perc_99_5)
#slr_data_85_perc_100 = fill_nan(slr_data['85_perc_100'].values)
#interplated_slr.insert(1, '85_perc_100', slr_data_85_perc_100)
#
#slr_data_45_perc_95 = fill_nan(slr_data['45_perc_95'].values)
#interplated_slr.insert(1, '45_perc_95', slr_data_45_perc_95)
#slr_data_45_perc_99_5 = fill_nan(slr_data['45_perc_99_5'].values)
#interplated_slr.insert(1, '45_perc_99_5', slr_data_45_perc_99_5)
#slr_data_45_perc_100 = fill_nan(slr_data['45_perc_100'].values)
#interplated_slr.insert(1, '45_perc_100', slr_data_45_perc_100)
#
#slr_data_26_perc_95 = fill_nan(slr_data['26_perc_95'].values)
#interplated_slr.insert(1, '26_perc_95', slr_data_26_perc_95)
#slr_data_26_perc_99_5 = fill_nan(slr_data['26_perc_99_5'].values)
#interplated_slr.insert(1, '26_perc_99_5', slr_data_26_perc_99_5)
#slr_data_26_perc_100 = fill_nan(slr_data['26_perc_100'].values)
#interplated_slr.insert(1, '26_perc_100', slr_data_26_perc_100)
#
#
#outfilepath = "{}output/projections/data/NLD/interpolated_slr_ID24.csv".format(basdir)
#interplated_slr.to_csv(outfilepath)
#print(outfilepath)
#
#
## Plot of interpolation
## list of named colors: https://matplotlib.org/stable/gallery/color/named_colors.html
#
#time = interplated_slr.index.values
#rcp26_perc_99_5 = interplated_slr['26_perc_99_5'].values
#rcp26_perc_100 = interplated_slr['26_perc_100'].values
#rcp45_perc_99_5 = interplated_slr['45_perc_99_5'].values
#rcp45_perc_100 = interplated_slr['45_perc_100'].values
#rcp85_perc_99_5 = interplated_slr['85_perc_99_5'].values
#rcp85_perc_100 = interplated_slr['85_perc_100'].values
#
#
## plot lines
#plt.plot(time, rcp26_perc_99_5, label = "RCP2.6, percentile 99.5", color = 'greenyellow')
#plt.plot(time, rcp26_perc_100, label = "RCP2.6, percentile 100", color = 'forestgreen')
#
#plt.plot(time, rcp45_perc_99_5, label = "RCP4.5, percentile 99.5", color = 'dodgerblue')
#plt.plot(time, rcp45_perc_100, label = "RCP4.5, percentile 100", color = 'mediumblue')
#
#plt.plot(time, rcp85_perc_99_5, label = "RCP8.5, percentile 99.5", color = 'lightcoral')
#plt.plot(time, rcp85_perc_100, label = "RCP8.5, percentile 100", color = 'red')
## Set the x axis label of the current axis.
#plt.xlabel('Time')
## Set the y axis label of the current axis.
#plt.ylabel('Sealevel [cm]')
## Set a title of the current axes.
#plt.title('Sea-level for different RCPs for Delfzijl')
## show a legend on the plot
#plt.legend()
#plt.tight_layout()
## show plot
##plt.show()
#
## save plot
#plt.savefig('{}output/projections/plots/NLD/prjected_slr_ID24.pdf'.format(basdir))


####################################################################################
####################################################################################
# Interpolation ID24
####################################################################################
basdir = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/'

slr_data = pd.read_csv('{}input_data/projections/SLR_ID1476.csv'.format(basdir), sep = ';')#, index_col = 0)

def fill_nan(A):
    '''
    interpolate to fill nan values
    '''
    inds = np.arange(A.shape[0])
    good = np.where(np.isfinite(A))
    f = interpolate.interp1d(inds[good], A[good],bounds_error=False)
    B = np.where(np.isfinite(A),A,f(inds))
    return B

slr_data_85_perc_95 = fill_nan(slr_data['85_perc_95'].values)

interplated_slr = pd.DataFrame(slr_data['year'].values)
interplated_slr.columns = ['time']
interplated_slr.insert(1, "85_perc_95", slr_data_85_perc_95)
interplated_slr.set_index('time', inplace=True)

slr_data_85_perc_99_5 = fill_nan(slr_data['85_perc_99_5'].values)
interplated_slr.insert(1, '85_perc_99_5', slr_data_85_perc_99_5)
slr_data_85_perc_100 = fill_nan(slr_data['85_perc_100'].values)
interplated_slr.insert(1, '85_perc_100', slr_data_85_perc_100)

slr_data_45_perc_95 = fill_nan(slr_data['45_perc_95'].values)
interplated_slr.insert(1, '45_perc_95', slr_data_45_perc_95)
slr_data_45_perc_99_5 = fill_nan(slr_data['45_perc_99_5'].values)
interplated_slr.insert(1, '45_perc_99_5', slr_data_45_perc_99_5)
slr_data_45_perc_100 = fill_nan(slr_data['45_perc_100'].values)
interplated_slr.insert(1, '45_perc_100', slr_data_45_perc_100)

slr_data_26_perc_95 = fill_nan(slr_data['26_perc_95'].values)
interplated_slr.insert(1, '26_perc_95', slr_data_26_perc_95)
slr_data_26_perc_99_5 = fill_nan(slr_data['26_perc_99_5'].values)
interplated_slr.insert(1, '26_perc_99_5', slr_data_26_perc_99_5)
slr_data_26_perc_100 = fill_nan(slr_data['26_perc_100'].values)
interplated_slr.insert(1, '26_perc_100', slr_data_26_perc_100)


outfilepath = "{}output/projections/data/BGD/interpolated_slr_ID1476.csv".format(basdir)
interplated_slr.to_csv(outfilepath)
print(outfilepath)


# Plot of interpolation
# list of named colors: https://matplotlib.org/stable/gallery/color/named_colors.html

time = interplated_slr.index.values
rcp26_perc_99_5 = interplated_slr['26_perc_99_5'].values
rcp26_perc_100 = interplated_slr['26_perc_100'].values
rcp45_perc_99_5 = interplated_slr['45_perc_99_5'].values
rcp45_perc_100 = interplated_slr['45_perc_100'].values
rcp85_perc_99_5 = interplated_slr['85_perc_99_5'].values
rcp85_perc_100 = interplated_slr['85_perc_100'].values


# plot lines
plt.plot(time, rcp26_perc_99_5, label = "RCP2.6, percentile 99.5", color = 'greenyellow')
plt.plot(time, rcp26_perc_100, label = "RCP2.6, percentile 100", color = 'forestgreen')

plt.plot(time, rcp45_perc_99_5, label = "RCP4.5, percentile 99.5", color = 'dodgerblue')
plt.plot(time, rcp45_perc_100, label = "RCP4.5, percentile 100", color = 'mediumblue')

plt.plot(time, rcp85_perc_99_5, label = "RCP8.5, percentile 99.5", color = 'lightcoral')
plt.plot(time, rcp85_perc_100, label = "RCP8.5, percentile 100", color = 'red')
# Set the x axis label of the current axis.
plt.xlabel('Time')
# Set the y axis label of the current axis.
plt.ylabel('Sealevel [cm]')
# Set a title of the current axes.
plt.title('Sea-level for different RCPs for Cox\'s Bazaar')
# show a legend on the plot
plt.legend()
plt.tight_layout()
# show plot
#plt.show()

# save plot
plt.savefig('{}output/projections/plots/BGD/prjected_slr_ID1476.pdf'.format(basdir))