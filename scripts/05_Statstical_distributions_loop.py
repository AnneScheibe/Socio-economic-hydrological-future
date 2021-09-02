"""
Created on Nov 2020

@author: Anne Scheibe

Subject: The script is used to perform statistical calculations for the social behavior projections from 
script 04.  
For each RCP and per parameters a seperate dataframe is saved. 
This dataframe includes statistical quantities calculated for the total data length of 10,000 runs. 

"""
import pandas as pd

basedir = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/'

parameters = ['W','D','M', 'L', 'H', 'F', 'actual_height_increase', 'capital_stock', 
              'desired_height_increase', 'possible_height_increase']
countries = ['NLD']#,'BGD']
rcps = ['26_perc100','45_perc100', '85_perc100', ] # '26_perc99_5', '45_perc99_5', '85_perc99_5'


#maintainance_costs = ['main_1', 'main_2', 'main_3']
#unit_costs = ['unit_1','unit_2','unit_3']

maintainance_costs = ['main']
unit_costs = ['unit']

#####################################################################################
## 
#####################################################################################

for unit_cost in unit_costs:#[:1]:
    for main_cost in maintainance_costs:#[:1]:
        for country in countries:
            for rcp in rcps:#[:1]:
                for parameter in parameters:#[:1]:
                    print(parameter)
                                                                                
        #           # constant_GDP
                    filepath = '{}output/projections/data/{}/social_behavior_projections/ID24_{}_rcp{}_constant_{}_{}_15_Mio.csv'.format(
                            basedir, country, parameter, rcp, unit_cost, main_cost)                                                                                                                  
                                    
                    file_series = pd.read_csv(filepath, index_col=0)
                    print(country, rcp, parameter)
        
                    # two example time series are selected 
                    median_file_series = file_series.median()
                    selection_min  = (file_series.min() <= median_file_series.min())                   
                    #selection_min  = (file_series.min() <= median_file_series.median()) 
                    selection_max  = (file_series.max() >= median_file_series.mean()) 
                    #selection_max  = (file_series.max() >= median_file_series.median())
                                           
                    df = pd.DataFrame({
                        "min": file_series.min(axis=1),
                        "quant_005" : file_series.quantile(0.005, axis=1),
                        "mean" : file_series.mean(axis=1),
                        "median" : file_series.median(axis=1), 
                        "max" : file_series.max(axis=1),
                        "quant_995" : file_series.quantile(0.995, axis=1), 
                        "select_min" : file_series[selection_min[selection_min].index[1]],
                        "select_max" : file_series[selection_max[selection_max].index[2]] 
                    })
                            
                    #constant_GDP
                    outfilepath = '{}output/projections/data/{}/05_Statstical_distributions/ID24_{}_statistical_distrubution_rcp{}constant_GDP_{}_{}_15_Mio.csv'.format(
                            basedir, country, parameter, rcp, unit_cost, main_cost)
                                
                    df.to_csv(outfilepath)
                    print(outfilepath)
