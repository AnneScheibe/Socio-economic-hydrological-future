# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 08:58:01 2020

@author: scheibe

The script is used to read slr projections and water level projections for BGD and NDL and to sum up.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

basedir = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/'

####################################################################################
# Import data
####################################################################################

### DELFZIJL (NDL)
#load slr for ID24 (calculated by interplation of 2 values)
ID24_slr = pd.read_csv('{}output/projections/data/NLD/interpolated_slr_ID24.csv'.format(basedir), sep = ',', index_col = 0)
# selection of years; divide by 100 to make units equal (cm vs. m) 
ID24_slr_26_pec99_5 = ID24_slr['26_perc_99_5'].loc[2030:2099] / 100
ID24_slr_26_pec100 = ID24_slr['26_perc_100'].loc[2030:2099] / 100

ID24_slr_45_pec99_5 = ID24_slr['45_perc_99_5'].loc[2030:2099] / 100
ID24_slr_45_pec100 = ID24_slr['45_perc_100'].loc[2030:2099] / 100

ID24_slr_85_pec99_5 = ID24_slr['85_perc_99_5'].loc[2030:2099] / 100
ID24_slr_85_pec100 = ID24_slr['85_perc_100'].loc[2030:2099] / 100

#load waterlevel without slr (calaculated by historical time series and GUM pdf)
NDL_waterlevel = pd.read_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/NLD/NDL_sampled_waterlevel_projections_without_slr_from_history_new.csv", sep = ',', index_col = 0)
NDL_waterlevel = NDL_waterlevel.loc[2030:2099]

run_id = list(np.arange(0,10001).astype(str))

df = np.zeros((70,10001)) # jetzt sind weniger jahre für die matrix bereit
#df = np.zeros((94,10001)) # das war vorher die größe der matrix
line_counter=0

for i in ID24_slr_26_pec100.index.values:
    print(i)
    waterlevel_by_year = NDL_waterlevel.loc[NDL_waterlevel.index == i].values[0]
    slr_rcp26_by_year = ID24_slr_26_pec100.loc[ID24_slr_26_pec100.index == i].values[0]

    projected_waterlevel = waterlevel_by_year + slr_rcp26_by_year
    print(projected_waterlevel)
    df[line_counter,]=i
    df[line_counter,1:]=projected_waterlevel

    line_counter+=1

data= pd.DataFrame(data=df,columns=run_id) #, index_col=0)
data= data.rename(columns={'0':'time'})

data.to_csv("{}output/projections/data/NLD/Sampled_waterlevel_projections_rcp26_perc100_ID24.csv".format(basedir))
