"""
Created on 24.08.2021

@author: Anne Scheibe

Subject: The script is used to perform figures for the output of the social behavior projections from 
script 05_Statistical_distrubution_loop.py 

"""

import pandas as pd
import matplotlib.pyplot as plt

basedir = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/'

parameters = ['W',
              'D',
              'M', 
              'L', 
              'H', 
              'F', 
              'actual_height_increase', 
              'capital_stock', 
              'desired_height_increase', 
              'possible_height_increase',
              ]

country = ['NLD',
           ]#, 'BGD']

rcps = ['26_perc100','45_perc100', '85_perc100', ] # '26_perc99_5', '45_perc99_5', '85_perc99_5'

#maintainance_costs = ['main_1', 'main_2', 'main_3']
#unit_costs = ['unit_1','unit_2','unit_3']

maintainance_costs = ['main']
unit_costs = ['unit']


y_labels = {
    'M': 'Social memory [-]',
    'L': 'Losses [-]',
    'F': 'Relativ flood damage [-]',
    'H': 'Height of levees [m]',
    'D': 'Population density [%]',
    'W': 'Water level [m]',
    'actual_height_increase': 'Actual height increase [m]',
    'capital_stock': 'Capital stock [-]',
    'desired_height_increase': 'Desired height increase [m]',
    'possible_height_increase': 'Possible height increase [m]',  
}

value_names = {
    'M': 'Social memory (M)',
    'L': 'Losses (L)',
    'F': 'Relativ flood damage (F)',
    'H': 'Height of levees (H)',
    'D': 'Population density (D)',
    'W': 'Water level (W)',
    'actual_height_increase': 'Actual height increase',
    'capital_stock': 'Capital stock',
    'desired_height_increase': 'Desired height increase',
    'possible_height_increase': 'Possible height increase', 
}

country_names = {
        'NLD' : 'Netherlands',
        'BGD' : 'Bangladesh',
        }

rcp_names = {
        '26_perc100':'RCP 2.6, percentile 100',
        '45_perc100':'RCP 4.5, percentile 100',
        '85_perc100':'RCP 8.5, percentile 100',
        '26_perc99_5':'RCP 2.6, percentile 99.5',
        '45_perc99_5':'RCP 4.5, percentile 99.5',
        '85_perc99_5':'RCP 8.5, percentile 99.5',
            }
 
#unit_cost_names = {
#        'unit_1': 'Unit costs 1 (coastline * unit_costs / 2)',
#        'unit_2': 'Unit costs 2* (unit_costs * height / levee_height_cost_correspond)',
#        'unit_3': 'Unit costs 3 (unit_costs * height / 2)',
#            }
#
#main_cost_names = {
#        'main_1': 'Maintainance costs 1 (coastline * unit_maintainance_costs)',
#        'main_2': 'Maintainance costs 2* (coastline * unit_maintainance_costs * height / levee_height_cost_correspond)',
#        'main_3': 'Maintainance costs 3 (coastline * unit_maintainance_costs * height / 2)',
#            }

unit_cost_names = {
        'unit': 'Unit costs 13.500.000,00',
            }

main_cost_names = {
        'main': 'Maintainance costs 20.000.000,00',
        }
####################################################################################
# Plot 
####################################################################################
for parameter in parameters:#[:1]:
    print(parameter)

    for unit_cost in unit_costs:#[:1]:
        print(unit_cost)
        for main_cost in maintainance_costs:#[:1]:
            print(main_cost)
            fig, ax = plt.subplots(1 , 3,  figsize=(15, 6), dpi=100, sharey=True)
            
            fig.suptitle('{} \n {} \n and {}'.format(
                    value_names[parameter],
                    unit_cost_names[unit_cost], 
                    main_cost_names[main_cost]),fontsize= 16) 
                       
            for col, rcp in enumerate(rcps):
                          
                filepath = '{}output/projections/data/NLD/05_Statstical_distributions/ID24_{}_statistical_distrubution_rcp{}constant_GDP_{}_{}_20_Mio.csv'.format(
                            basedir,parameter, rcp, unit_cost, main_cost)
                
                file_series = pd.read_csv(filepath, index_col=0)
                #print(rcp, surge)
 
                #   max      mean    median       min  quant_005  quant_995
                #The gray stripe shows data from the 99,5 % quantiel to the 0,05% quantiel. 
                ax[col].fill_between(file_series.index, 
                                 file_series['quant_005'], 
                                 file_series['quant_995'], 
                                 color='lightgray')
                
                #plots the selected quantiel, in this case 0.995 % quantiel 
                ax[col].plot(file_series.index,
                        file_series['median'],
                        color='black',
                        linewidth=3)
    
                # select time series with extreme values, in that case values 
                # that are higher than mean_tide_series.max()  -> this selection 
                # returned a boolean             
                ax[col].plot(file_series.index,
                        file_series['select_max'],
                        color='xkcd:coral',
                         alpha=0.8,
                         linewidth=2)
                
                ax[col].plot(file_series.index,
                  file_series['select_min'],
                  color='xkcd:azure',
                           alpha=0.8,
                           linewidth=2
                  )
             
                ax[col].set_ylabel(y_labels[parameter], fontsize=12)
                #ax.set_xlim(2017.,2100.)
                #ax.set_ylim(0.35, 0.45)
                ax[col].set_xlabel('Time', fontsize= 12)
                #ax[0, 1].set_xlabel('Time', fontsize= 12)
                
                ax[col].set_title('{}'.format(
                            rcp_names[rcp]), fontsize= 12)
                              
                plt.tight_layout()  

                #constant_GDP
                plt.savefig('{}output/projections/plots/NLD/07b_probability_distribution/ID24_{}_constant_GDP_{}_{}_20_Mio.pdf'.format(
                        basedir, parameter, unit_cost, main_cost))
