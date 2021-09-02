# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 08:58:01 2020

@author: scheibe

The script is used to read slr projections and water level projections for BGD and NDL and to sum up.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

basdir = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/'

####################################################################################
# Import data
####################################################################################

### DELFZIJL (NDL)
ID24_slr = pd.read_csv('{}output/projections/data/NLD/interpolated_slr_ID24.csv'.format(basdir), sep = ',', index_col = 0)
ID24_slr_26_pec99_5 = ID24_slr['26_perc_99_5'].values
ID24_slr_26_pec100 = ID24_slr['26_perc_100'].values
#NDL_slr_rcp_26 = pd.read_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/NLD/NLD_projections_MIROC5_rcp26_2006_2099.csv", sep = ',', index_col = 0)
#NDL_slr_rcp_60 = pd.read_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/NLD/NLD_projections_MIROC5_rcp60_2006_2099.csv", sep = ',', index_col = 0)



############## bis hier hin gekommen




NDL_waterlevel = pd.read_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/NLD/NDL_sampled_waterlevel_projections_without_slr_from_history_new.csv", sep = ',', index_col = 0)

run_id = list(np.arange(0,10001).astype(str))

df = np.zeros((94,10001))
line_counter=0
#for i in BGD_slr_rcp_26.index.values:#[:4].values:
for i in NDL_slr_rcp_26.index.values:#[:4].values:
    print(i)
    waterlevel_by_year = NDL_waterlevel.loc[NDL_waterlevel.index == i].values[0]
    slr_rcp26_by_year = NDL_slr_rcp_26.loc[NDL_slr_rcp_26.index == i, '95_percentile'].values[0]
    
#    waterlevel_by_year = BGD_waterlevel.loc[BGD_waterlevel.index == i].values[0]
#    slr_rcp26_by_year = BGD_slr_rcp_26.loc[BGD_slr_rcp_26.index == i, '95_percentile'].values[0]
    
    projected_waterlevel = waterlevel_by_year + slr_rcp26_by_year
    print(projected_waterlevel)
    df[line_counter,]=i
    df[line_counter,1:]=projected_waterlevel

    line_counter+=1

data= pd.DataFrame(data=df,columns=run_id) #, index_col=0)
data= data.rename(columns={'0':'time'})

data.to_csv("{}output/projections/data/NLD/NLD_Sampled_waterlevel_projections_rcp26_history_new.csv".format(basedir))
#data.to_csv("{}output/projections/data/NLD/NLD_Sampled_waterlevel_projections_rcp60_history_new.csv".format(basedir))

#data.to_csv("{}output/projections/data/BGD/BGD_Sampled_waterlevel_projections_rcp26_history.csv".format(basedir))
#data.to_csv("{}output/projections/data/BGD/BGD_Sampled_waterlevel_projections_rcp60_history.csv".format(basedir))





######################################################
### old version
#
#####################################################################################
## Import data
#####################################################################################
### CHITTAGONG (BGD)
#
##BGD_slr_rcp_26 = pd.read_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/BGD/BGD_projections_MIROC5_rcp26_2006_2099.csv", sep = ',', index_col = 0)
##BGD_slr_rcp_60 = pd.read_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/BGD/BGD_projections_MIROC5_rcp60_2006_2099.csv", sep = ',', index_col = 0)
##
##BGD_waterlevel = pd.read_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/BGD/BGD_Sampled_waterlevel_projections_without_slr_from_history.csv", sep = ',', index_col = 0)
#
#### DELFZIJL (NDL)
#NDL_slr_rcp_26 = pd.read_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/NLD/NLD_projections_MIROC5_rcp26_2006_2099.csv", sep = ',', index_col = 0)
#NDL_slr_rcp_60 = pd.read_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/NLD/NLD_projections_MIROC5_rcp60_2006_2099.csv", sep = ',', index_col = 0)
#
#NDL_waterlevel = pd.read_csv("C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/NLD/NDL_sampled_waterlevel_projections_without_slr_from_history_new.csv", sep = ',', index_col = 0)
#
#run_id = list(np.arange(0,10001).astype(str))
#
#df = np.zeros((94,10001))
#line_counter=0
##for i in BGD_slr_rcp_26.index.values:#[:4].values:
#for i in NDL_slr_rcp_26.index.values:#[:4].values:
#    print(i)
#    waterlevel_by_year = NDL_waterlevel.loc[NDL_waterlevel.index == i].values[0]
#    slr_rcp26_by_year = NDL_slr_rcp_26.loc[NDL_slr_rcp_26.index == i, '95_percentile'].values[0]
#    
##    waterlevel_by_year = BGD_waterlevel.loc[BGD_waterlevel.index == i].values[0]
##    slr_rcp26_by_year = BGD_slr_rcp_26.loc[BGD_slr_rcp_26.index == i, '95_percentile'].values[0]
#    
#    projected_waterlevel = waterlevel_by_year + slr_rcp26_by_year
#    print(projected_waterlevel)
#    df[line_counter,]=i
#    df[line_counter,1:]=projected_waterlevel
#
#    line_counter+=1
#
#data= pd.DataFrame(data=df,columns=run_id) #, index_col=0)
#data= data.rename(columns={'0':'time'})
#
#data.to_csv("{}output/projections/data/NLD/NLD_Sampled_waterlevel_projections_rcp26_history_new.csv".format(basedir))
##data.to_csv("{}output/projections/data/NLD/NLD_Sampled_waterlevel_projections_rcp60_history_new.csv".format(basedir))
#
##data.to_csv("{}output/projections/data/BGD/BGD_Sampled_waterlevel_projections_rcp26_history.csv".format(basedir))
##data.to_csv("{}output/projections/data/BGD/BGD_Sampled_waterlevel_projections_rcp60_history.csv".format(basedir))