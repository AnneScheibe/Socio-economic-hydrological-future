"""
Created on Feb 2019

@author: Anne Scheibe

Subject: The script is used to perform a statistical summary for the social behavior projections from 
script 02_full_run. 

"""

import pandas as pd

basedir = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/'

parameters = ['W','D','M', 'L', 'H', 'F', 'actual_height_increase', 'capital_stock', 
              'desired_height_increase', 'possible_height_increase']

countries = ['NLD']#'NLD']#,'BGD']
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
        results = []
        for country in countries:
            for rcp in rcps:
                for parameter in parameters:
                    print(parameter)
        
        #           # constant_GDP
                    filepath = '{}output/projections/data/{}/05_Statstical_distributions/ID24_{}_statistical_distrubution_rcp{}constant_GDP_{}_{}_15_Mio.csv'.format(
                            basedir, country, parameter, rcp, unit_cost, main_cost)         
                    
                    df = pd.read_csv(filepath, index_col=0)
                    print(country, rcp, parameter)
                  
                    #print('2006',rcp, df['median'][2006])
                    print('2030',rcp, df['median'][2030])
                    print('2050',rcp, df['median'][2050])
                    print('2070',rcp, df['median'][2070])
                    print('2099',rcp, df['median'][2099])                
                    
                    summaries = []
                    for col in df.columns:
                        summaries.append(df[col].describe()[1:])
                    summary = pd.concat(summaries, axis=1)
                    summary = summary.T
                    summary['rcp'] = rcp
                    summary['parameter'] = parameter
                    results.append(summary)
        results = pd.concat(results)
        
        results.index.name = 'variable'
        results = results.reset_index()
        results = results.set_index(['parameter', 'rcp', 'variable'])
        results = results.sort_index()
        
        # constant GDP
        results.to_csv('{}output/projections/data/{}/06_Statstical_summary/ID24_statistical_distrubution_constant_GDP_{}_{}_15_Mio.csv'.format(
                basedir, country, unit_cost, main_cost))