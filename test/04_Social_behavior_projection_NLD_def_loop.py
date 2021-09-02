"""
Created on Okt 2018

@author: Anne Scheibe

Subject: The script is used to calculate the social behavior and is called a socio-hydrological model.

Based on:
Di Baldassarre, G., Viglione, A., Carr, G., Kuil, L., Yan, K., Brandimarte, L., & Bloschl, G.
(2015). Debates-perspectives on socio-hydrology: Capturing feedbacks between physical
and social processes. Water Resources Research, 51 (6), 4770-4781.

Alessio Ciullo, Alberto Viglione, Attilio Castellarin, Massimiliano Crisci &
Giuliano Di Baldassarre (2017) Socio-hydrological modelling of flood-risk dynamics: comparing the
resilience of green and technological systems, Hydrological Sciences Journal, 62:6, 880-891, DOI:
10.1080/02626667.2016.1273527

"""

# last modification: 17.08.2021

import math
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

basedir = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/'

####################################################################################
# Definition of constants by Ciullo, A., Viglione, A., Castellarin, A., Crisci, M., & Di Baldassarre, G. (2017).
# Socio-hydrological modelling of flood-risk dynamics: comparing the resilience of green and technological systems.
# Hydrological sciences journal, 62(6), 880-891.
# Bangladesh-case-study
####################################################################################
F_initial = 0.0     # Initial value for relative flood damage F (Hydrology); output: range between 0 and 1
D_initial = 0.001   # Initial value for population density D (Demography); output: range between 0 and 1
#H_initial = 2.5     # At the beginning of the time series; Levee height in NLD is about 2.5m

H_initial = 4.5     # In 2018, see calibration (4.49 m)
M_initial = 0.0     # Initial value for societal memory of flood M (Society)

# Adjustment of 10.02.2020, after a phone call with Di Baldassarre from ...:
# The model is calibrated for fluvial flood, maximal_levee_height have to adapt it for coastal floods. Therefore, the constant Xi-H is set to zero. [formerly:xi_H = 0.2]
xi_H = 0.0  # Constant proportion of flood level enhancement due to presence of levees (Hydrology) - Di Baldassarre et al (2015)
rho_D = 0.003  # 0.03 Constant maximum relative growth rate (Demography) unit:none - Di Baldassarre et al (2015)
alpha_D = 5.0  # Constant ratio preparedness/ awareness (Demography) unit: none - Di Baldassarre et al (2015)
epsilon_T = 1.1  # Constant Safety factor for levee heightening (Technologogy) - unit: none - Di Baldassarre et al (2015)
kappa_T = 0  # 2e-05 Constant protection level decay rate (Technology) unit: none - Di Baldassarre et al (2015)
my_s = (
    0.06  # Constant memory loss rate (Society) unit: none - Di Baldassarre et al (2015)
)
alpha_H = 10.0  # Constant related to relationship between flood water levels to relative damage (Hydrology) unit: [m] - Di Baldassarre et al (2015)

delta_t = 1.0  # Size of time step --> important for defintion of "dimension of time"

####################################################################################
# Setting of constants
####################################################################################
levee_height_cost_correspond = (
    4.5  # [m]; The corresponding year is 2014 (World Bank report)
)

coastline = 451  # [km], data https://en.wikipedia.org/wiki/List_of_countries_by_length_of_coastline#cite_note-17
# Unit costs of sea dikes in M euros km-1 m-1, reference year 2014; source: Nicholls, R. J., Hinkel, J., Lincke, D.,  & van der Pol, T. (2019). Global investment costs for coastal defense through the 21st century. The World Bank.
unit_cost_low = 4900000.0
unit_cost_high = 13500000.0
unit_costs = unit_cost_high
#unit_maintainance_costs = unit_costs / 10 # used for Calibration
#unit_maintainance_costs = unit_cost_high # 1. run
#unit_maintainance_costs = 20000000.0 # 2. run
unit_maintainance_costs = 15000000.0 # 3. run

#constant_costs = True
constant_costs = False  # used for Calibration

####################################################################################
# Fuctions
####################################################################################

# originian calculation of unit costs
def unit_costs_height_increase(height):
    if constant_costs:
        return coastline * unit_costs / 2
    else:
        return coastline * unit_costs * height / levee_height_cost_correspond
    
    # unit_costs = [units_1, unit_2, unit_3]

#def unit_costs_height_increase_1(height):
#    return coastline * unit_costs / 2

def unit_costs_height_increase_2(height):
    return coastline * unit_costs * height / levee_height_cost_correspond

#def unit_costs_height_increase_3(height):
#    return coastline * unit_costs * height / 2


def possible_investments_for_coastal_protection(GDP):
    return GDP * 0.02

## original calculation for maintainance_costs
#def maintainance_costs(height):
#    if constant_costs:
#        return coastline * unit_maintainance_costs
#    else:
#        return (
#            coastline * unit_maintainance_costs * height / levee_height_cost_correspond
#        )

#def maintainance_costs_1(height):
#    return coastline * unit_maintainance_costs

def maintainance_costs_2(height):
    return (
            coastline * unit_maintainance_costs * height / levee_height_cost_correspond
        )
#def maintainance_costs_3(height):
#    return (
#            coastline * unit_maintainance_costs * height / 2
#        )

####################################################################################
# Dynamic equations
####################################################################################

countries = ['NLD']
rcps = ['26_perc100', '45_perc100', '85_perc100']

#print('This is H initial', H_initial, 'and H before the loop', H)
for country in countries:
    
    # load CONSTANT GDP for NLD from 1850 to 2100
    GDP_series_file = "C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/input_data/projections/{}/Tidy_constant_GDP_from_2019_{}_1850_2100.csv".format(
             country, country)
    #print(GDP_series_file)
    GDP_series = pd.read_csv(GDP_series_file, sep=";", index_col="year")
    #reak   
    #GDP_series = GDP_series.sort_index().loc[2006:2099]
    GDP_series = GDP_series.sort_index().loc[2030:2099]
    GDP_series = GDP_series['currency_units_Euro']
    #print(GDP_series)
    time_range = GDP_series.index.values    

    for rcp in rcps:
        
        ## load tidal information - Distribution by historical time series
        tide_series_file = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/Sampled_waterlevel_projections_rcp{}_ID24.csv'.format(
                country, rcp)
        tide_series = pd.read_csv(tide_series_file, sep=",", index_col = "time")
        del tide_series['Unnamed: 0']
        
        #tide_series.iloc[:,:2] # just for testing
        
        #print(tide_series)
           
        output_D = np.zeros((len(time_range), len(tide_series.columns)))
        output_D = pd.DataFrame(output_D, index=time_range)
        
        output_M = np.zeros((len(time_range), len(tide_series.columns)))
        output_M = pd.DataFrame(output_M, index=time_range)
        
        output_L = np.zeros((len(time_range), len(tide_series.columns)))
        output_L = pd.DataFrame(output_L, index=time_range)
        
        output_H = np.zeros((len(time_range), len(tide_series.columns)))
        output_H = pd.DataFrame(output_H, index=time_range)
        
        output_W = np.zeros((len(time_range), len(tide_series.columns)))
        output_W = pd.DataFrame(output_W, index=time_range) 
        
        output_F = np.zeros((len(time_range), len(tide_series.columns)))
        output_F = pd.DataFrame(output_F, index=time_range)
        
        output_actual_height_increase = np.zeros((len(time_range), len(tide_series.columns)))
        output_actual_height_increase = pd.DataFrame(output_actual_height_increase, index=time_range)
        
        output_capital_stock = np.zeros((len(time_range), len(tide_series.columns)))
        output_capital_stock = pd.DataFrame(output_capital_stock, index=time_range)
        
        output_desired_height_increase = np.zeros((len(time_range), len(tide_series.columns)))
        output_desired_height_increase = pd.DataFrame(output_desired_height_increase, index=time_range)
        
        output_possible_height_increase = np.zeros((len(time_range), len(tide_series.columns)))
        output_possible_height_increase = pd.DataFrame(output_possible_height_increase, index=time_range) 

        cnt = 0  
        
        for run_id in tide_series.columns:
            #print('run-id is', run_id)
            capital_stock = 0
            H = H_initial
            D = D_initial
            M = M_initial
            
            
            if H_initial <= 0:
                print("Warning: 0 costs in beginning because of initial 0m levee height")
            
                print('This is H before time-loop:', H)
            
            for time in range(len(time_range)):
                #print('time:', time)
##              # mit sparen: +=; ohne sparen: =
                capital_stock += possible_investments_for_coastal_protection(
                    GDP_series.values[time]
                ) - maintainance_costs_2(H)

                W = tide_series[run_id].values[time]
                #break
                #print('D', D)
                print('run_id:', run_id, 'time:', time, 'rcp:', rcp)
          
                # if water level (+ flood enhancement due to levee) exeeds levee height...
                if W + xi_H * H > H:
                    # ... then there is a damage > 0
                    F = 1 - math.exp(-(W + xi_H * H) / alpha_H)
                    desired_height_increase = epsilon_T * (W + xi_H * H - H)
                else:
                    # ... otherwise there is no damage
                    F = 0
                    desired_height_increase = 0
                 
                #print('This is H in the last loop, before calculating it', H)
                possible_height_increase = max(0, capital_stock / unit_costs_height_increase_2(H))
                actual_height_increase = min(desired_height_increase, possible_height_increase)
                capital_stock -= actual_height_increase * unit_costs_height_increase_2(H)
                H += delta_t * (actual_height_increase - kappa_T * H)
                
                L = F * D
                D += delta_t * rho_D * (1 - D * (1 + delta_t * alpha_D * M)) - delta_t * L
                M += delta_t * (L - my_s * M)

                #capital_stock = capital_stock / possible_investments_for_coastal_protection(GDP_series.values[-1])
                
                #print('D', D)
                #print('run_id', run_id)
                #print( 'This is H at the end of the loop:', H)
                output_W.iloc[time,cnt] = W
                output_D.iloc[time,cnt] = D
                output_M.iloc[time,cnt] = M
                output_L.iloc[time,cnt] = L
                output_H.iloc[time,cnt] = H
                output_F.iloc[time,cnt] = F
                output_actual_height_increase.iloc[time,cnt] = actual_height_increase
                output_capital_stock.iloc[time,cnt] = capital_stock
                output_desired_height_increase.iloc[time,cnt] = desired_height_increase
                output_possible_height_increase.iloc[time,cnt] = possible_height_increase

            cnt+=1
 
        
        #save with constant GDP
        output_D_filename = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/social_behavior_projections/ID24_D_rcp{}_constant_unit_main_15_Mio.csv'.format(country, rcp)
        output_D.to_csv(output_D_filename, header=True)
                    
        output_M_filename = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/social_behavior_projections/ID24_M_rcp{}_constant_unit_main_15_Mio.csv'.format(country, rcp)
        output_M.to_csv(output_M_filename, header=True)
                    
        output_L_filename = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/social_behavior_projections/ID24_L_rcp{}_constant_unit_main_15_Mio.csv'.format(country, rcp)
        output_L.to_csv(output_L_filename, header=True)
                    
        output_H_filename = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/social_behavior_projections/ID24_H_rcp{}_constant_unit_main_15_Mio.csv'.format(country, rcp)
        output_H.to_csv(output_H_filename, header=True)
                    
        output_W_filename = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/social_behavior_projections/ID24_W_rcp{}_constant_unit_main_15_Mio.csv'.format(country, rcp)
        output_W.to_csv(output_W_filename, header=True)
                    
        output_F_filename = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/social_behavior_projections/ID24_F_rcp{}_constant_unit_main_15_Mio.csv'.format( country, rcp)
        output_F.to_csv(output_F_filename, header=True)
        
        output_actual_height_increase_filename = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/social_behavior_projections/ID24_actual_height_increase_rcp{}_constant_unit_main_15_Mio.csv'.format(country, rcp)
        output_actual_height_increase.to_csv(output_actual_height_increase_filename, header=True)
                    
        output_capital_stock_filename = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/social_behavior_projections/ID24_capital_stock_rcp{}_constant_unit_main_15_Mio.csv'.format(country, rcp)
        output_capital_stock.to_csv(output_capital_stock_filename, header=True)
                    
        output_desired_height_increase_filename = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/social_behavior_projections/ID24_desired_height_increase_rcp{}_constant_unit_main_15_Mio.csv'.format(country, rcp)
        output_desired_height_increase.to_csv(output_desired_height_increase_filename, header=True)
                    
        output_possible_height_increase_filename = 'C:/Users/scheibe/Desktop/Flood_defence_project/data/Git_folder_flood_defence_project/output/projections/data/{}/social_behavior_projections/ID24_possible_height_increase_rcp{}_constant_unit_main_15_Mio.csv'.format(country, rcp)
        output_possible_height_increase.to_csv(output_possible_height_increase_filename, header=True)
        