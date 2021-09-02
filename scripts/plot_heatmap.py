"""
Created on Jan 2019

@author: Anne Scheibe

Subject: The script is used to perform heatmaps for the output of the social behavior projections from 
script 02_full_run. 

"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

#basedir = "C:/Users/scheibe/Desktop/master_thesis/new_modelruns/plot_output_2017/"

#parameters = ['M', 'H', 'L', 'F', 'D', 'W'] 
#societies = ['techno', 'green']

#mu_s_values = [0.015,0.03,0.06,0.12,0.24]
#alpha_Hs = [15,12,10,9,8,7,6,5,4.5]
#
#surges = ['stationary','non_stationary']
#rcps = ["26", "45", "60", "85"]

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
#    'desired_height_increase_delay': 'Desired height incerease (?) - delay', 
#    'possible_height_increase_delay': 'Possible height increase (?) - delay', 
#    'actual_height_increase_delay': 'Actual height increase (?) - delay',
}

society_names = {
        'techno' : 'Levee-building society',
        'green' : 'Levee-less society'}


basedir = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/'

parameters = ['W','D','M', 'L', 'H', 'F', 'actual_height_increase', 'capital_stock', 
              'desired_height_increase', 'possible_height_increase']
countries = ['NLD']#,'BGD']
rcps = ['45_perc100','85_perc100']#, '26_perc99_5', '45_perc99_5', '85_perc99_5'], '45_perc100', '26_perc100'


maintainance_costs = ['main_1', 'main_2', 'main_3']
unit_costs = ['unit_1','unit_2','unit_3']



rcp_names = {
        '26_perc100':'RCP 2.6, percentile 100',
        '45_perc100':'RCP 4.5, percentile 100',
        '85_perc100':'RCP 8.5, percentile 100',
        '26_perc99_5':'RCP 2.6, percentile 99.5',
        '45_perc99_5':'RCP 4.5, percentile 99.5',
        '85_perc99_5':'RCP 8.5, percentile 99.5',
            } 

####################################################################################
# SUPPLEMENT - single plot heatmap, mean of max values
####################################################################################
for parameter in parameters:
    for country in countries:
    #for society in societies: 
        
        fig, ax = plt.subplots(1 , 2, sharey=True) #  figsize=(15, 30), dpi=100,
        # [left, bottom, width, height] 
        cbar_ax = fig.add_axes([.90, .3, .03, .4], alpha=0.8) 
        
        for rcp_index, rcp in enumerate(rcps):
            #for surge_index, surge in enumerate(surges):
                
            out = np.zeros((len(unit_costs), len(maintainance_costs)))
            
            for row, unit_cost in enumerate(unit_costs):
                for col, maintainance_cost in enumerate(maintainance_costs):
                    
                    filepath = '{}projections/data/NLD/05_Statstical_distributions/ID24_{}_statistical_distrubution_rcp{}constant_GDP_{}_{}.csv'.format(
                            basedir, parameter, rcp, unit_cost, maintainance_cost)
                                           
                    df = pd.read_csv(filepath, index_col=0)
    
                    #max_df = df.max(axis=1)
                    #out[row, col] = df['quant_995'].max()
                    out[row, col] = df['max'].max()
                    #out[row, col] = df['median'].max()
                    
                    
            matrix = pd.DataFrame(out, index=unit_costs, columns=maintainance_costs)        
    
    
        #upper percentile
    
            fig.suptitle('Maximum of upper percentile - {}'.format(
                    value_names[parameter]), fontsize= 14)
            
            #midpoint = (matrix.values.max() - matrix.values.min()) / 2       
            
            sns.heatmap(matrix, ax=ax[rcp_index], 
                        cbar_ax = cbar_ax, cbar=True,
                        linewidths=0.1,
                        linecolor='gray',
                        rasterized=True,
                        alpha=0.8,
                        cmap="YlGnBu",
                        annot=True, annot_kws={"size": 10},
                       # fmt=".1f"
                        #center=midpoint
                        )
            
            
#            ax[rcp_index].set_xlabel(
#                    'unit costs', fontsize= 15)
#           
#            ax[rcp_index].set_ylabel(
#                    'maintainance costs', fontsize= 15)

            
            ax[rcp_index].set_title('{}'.format(
                    rcp_names[rcp]), fontsize= 10)
                            
            plt.tight_layout()  
           
            
            plt.subplots_adjust(
#                    hspace=0.2,     # 0.2 # the amount of height reserved for space between subplots,
#                                    # expressed as a fraction of the average axis height
#                    wspace=0.15,    # 0.2 # the amount of width reserved for space between subplots,
#                                    # expressed as a fraction of the average axis width
                    left= 0.12,    # 0.125 # the left side of the subplots of the figure
                    top = 0.8,     #0.95 # the top of the subplots of the figure
                    right = 0.85,    #0.9 # the right side of the subplots of the figure
                    bottom = 0.2    #0.1 # the bottom of the subplots of the figure
                    )
            
            plt.savefig(
                    '{}projections/plots/NLD/heatmaps/heatmap_{}_max_max_RCP45_85.pdf'.format(basedir,
                            parameter))
    
