# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:29:44 2019

@author: KUKUMAR


--ambient       Ambient temperature as measured by a thermal sensor located closely to the stator.
--coolant       Coolant temperature. The motor is water cooled. Measurement is taken at outflow.
--u_d           Voltage d-component
--u_q           Voltage q-component
--motor_speed   Motor speed
torque          Torque induced by current.
i_d             Current d-component
i_q             Current q-component
--pm            Permanent Magnet surface temperature representing the rotor temperature. This was measured with an infrared thermography unit.
--stator_yoke     Stator yoke temperature measured with a thermal sensor.
--stator_tooth    Stator tooth temperature measured with a thermal sensor.
--stator_winding  Stator winding temperature measured with a thermal sensor.
profile_id        Each measurement session has a unique ID. Make sure not to try to estimate from one session onto the other as they are strongly independent.

-- How to proceed
    1. Check feature by feature and find out which one has the maximum impact on temperature.
    2. then figure the features which have the impact on the rise in temerature
            or rather remove the features which have least impact.
    3. USe the selected features to train the algorithm ad test accordingly
    

"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Dataset Electric Motor\pmsm_temperature_data.csv')
print(data.head(5))

#-- remove the not required values
data.drop(['torque','i_d','i_q','profile_id'],axis=1,inplace=True)
print(data.head(5))

#-- check for the columns null and not null 
print(data.info())
#print(data.isnull().sum())

#print(data[['ambient','coolant','u_d','i_d','motor_speed']])
#plt.hist(data.motor_speed)
#plt.hist(data.stator_winding)
#plt.show()

#print(data['stator_winding'].head(5))





