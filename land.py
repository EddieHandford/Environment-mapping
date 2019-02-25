# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:55:22 2019

@author: ED
"""
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

from netCDF4 import Dataset
nc = Dataset('land.nc' , 'r')


for i in nc.variables:
    print(i)
    
    
tas = nc.variables['tas'][:]
latitude_longitude = nc.variables['latitude_longitude'][:]
ensemble_member = nc.variables['ensemble_member'][:]
time = nc.variables['time'][:]
latitude = nc.variables['latitude'][:]
latitude_bnds = nc.variables['latitude_bnds'][:]
longitude = nc.variables['longitude'][:]
longitude_bnds = nc.variables['longitude_bnds'][:]
ensemble_member_id = nc.variables['ensemble_member_id'][:]
month_number = nc.variables['month_number'][:]
year = nc.variables['year'][:]
yyyymms = nc.variables['yyyymm'][:]


print(tas[0 , 0 ,0 ,0 ])




shuffle_tas = tas[0,:]
print(shuffle_tas[0 , : , :])
year_1900 = shuffle_tas[0,:,:]
print()






#print(shuffle_tas)

#tester= pd.DataFrame({ 'tas':tas[: , 1],                'year':year[:], 'time':time[:]              })