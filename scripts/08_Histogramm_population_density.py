# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:15:25 2021

@author: Anne Scheibe

Subject: The script is used to perform figures for the output of the social behavior projections from 
script 02_full_run. 

"""

#social_behavior_projections/ID24_possible_height_increase_rcp85_perc100_history_new_constant_GDP_save_money_unit_2_main_2.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

parameters = ['W','D','M', 'L', 'H', 'F', 'actual_height_increase', 'capital_stock', 'desired_height_increase', 'possible_height_increase']
countries = ['NLD']#'NLD']# 'BGD']
rcps = ['26_perc100', '45_perc100','85_perc100',]#, , '26_perc99_5','45_perc99_5', '85_perc99_5'] '45_perc100','26_perc99_5', '85_perc99_5']#,

basedir = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/'

y_labels = {
    'M': 'Social memory [-]',
    'L': 'Losses [-]',
    'F': 'Relativ flood damage [-]',
    'H': 'Height of levees [m]',
    'D': 'Population density [-]',
    'W': 'Water level [m]',
    'actual_height_increase': 'Actual height increase [m]',
    'capital_stock': 'Capital stock',
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
    'desired_height_increase': 'Desired height increase ',
    'possible_height_increase': 'Possible height increase', 
}

country_names = {
        'NLD' : 'Netherlands',
        'BGD' : 'Bangladesh',
        }

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }


rcp_names = {
        '26_perc100':'RCP 2.6, percentile 100',
        '45_perc100':'RCP 4.5, percentile 100',
        '85_perc100':'RCP 8.5, percentile 100',
        '26_perc99_5':'RCP 2.6, percentile 99.5',
        '45_perc99_5':'RCP 4.5, percentile 99.5',
        '85_perc99_5':'RCP 8.5, percentile 99.5',
            }
 
####################################################################################
# Plot 
####################################################################################

for parameter in parameters:
    print(parameter)
    #for country in countries: 
    fig, ax = plt.subplots(1 , 3,  figsize=(15, 6), dpi=100, sharey=True)
    
#    fig.suptitle('{} - {}'.format(country_names[country],
#            value_names[parameter]), fontsize= 20) 
    fig.suptitle('{} - Maintainance costs 15.000.000,00'.format(value_names[parameter]), fontsize= 20) 

    for col, rcp in enumerate(rcps):
                   
        filepath = '{}output/projections/data/NLD/social_behavior_projections/ID24_{}_rcp{}_constant_unit_main_15_Mio.csv'.format(
                basedir, parameter, rcp)
        print(filepath)
        
#            #constant_GDP
#            filepath = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/05_Statstical_distributions/{}_{}_statistical_distrubution_rcp{}_history_new_constant_GDP.csv'.format(
#                    country, country, parameter, rcp)
      
        file_series = pd.read_csv(filepath, index_col=0)
    
        
        print(rcp)

#0	AR6-SSP1	#1e9583
#1	AR6-SSP2	#4576be
#2	AR6-SSP3	#f11111
#3	AR6-SSP4	#e78731
#4	AR6-SSP5	#8036a7  
        
        line_1 = file_series.loc[2099].hist(ax=ax[col], label = '2099', color='#8036a7', bins = 40, alpha=0.7, stacked=True)
        line_2 = file_series.loc[2080].hist(ax=ax[col], label = '2080', color='#e78731', bins = 40, alpha=0.6, stacked=True)
        line_3 = file_series.loc[2060].hist(ax=ax[col], label = '2060', color='#f11111', bins = 40, alpha=0.6, stacked=True)
        line_4 = file_series.loc[2040].hist(ax=ax[col], label = '2040', color='#4576be', bins = 40, alpha=0.6, stacked=True)
        line_5 = file_series.loc[2030].hist(ax=ax[col], label = '2030', color='#1e9583', bins = 40, alpha=0.6, stacked=True)
                        
        #Kernel density
#            sns.kdeplot(file_series.loc[2040], ax=ax[col], color='xkcd:seafoam', alpha=0.5)
#            sns.kdeplot(file_series.loc[2070], ax=ax[col], color='xkcd:azure', alpha=0.5)
#            sns.kdeplot(file_series.loc[2099], ax=ax[col], color='xkcd:coral', alpha=0.5)

    
        ax[col].set_ylabel('Frequency', fontsize=12)
#            ax[0, 0].set_ylabel('Frequency', fontsize=12)
#            ax[1, 0].set_ylabel('Frequency', fontsize=12)
#            ax[2, 0].set_ylabel('Frequency', fontsize=12)
#            ax[3, 0].set_ylabel('Frequency', fontsize=12)
#            #ax[row, col].set_xlim(0.,1.)
#            #ax[row, col].set_ylim(0., 1.)
        ax[col].set_yscale('log')
        ax[col].set_xlabel('Value of {}'.format(y_labels[parameter]), fontsize= 12)

        ax[col].set_title('{}'.format(rcp_names[rcp]), fontsize= 12)
        #ax[col].set_yscale('log')

        plt.tight_layout()  
        
        handles, labels = ax[col].get_legend_handles_labels()
        ax[col].legend(handles,labels, frameon=True, fontsize = 9, loc = 'upper right') #, edgecolor = 'k')
     
        plt.subplots_adjust(hspace=0.4, wspace=0.15, left= 0.125, 
                            top = 0.9, right = 0.9, bottom = 0.1)

        plt.savefig('{}output/projections/plots/NLD/histogramms/ID24_{}_histogramm_constant_GDP_unit_main_15_Mio.pdf'.format(
        basedir, parameter))

#    plt.savefig('C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/plots/{}/{}_histogramm_new_constant_GDP.pdf'.format(
#            country, parameter))
