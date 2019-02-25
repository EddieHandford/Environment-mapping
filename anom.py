# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:55:22 2019

@author: ED
"""
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

from netCDF4 import Dataset
nc = Dataset('anom.nc' , 'r')


for i in nc.variables:
    print(i)
    
    
tasAnom = nc.variables['tasAnom'][:]
transverse_mercator = nc.variables['transverse_mercator'][:]
time = nc.variables['time'][:]
time_bnds = nc.variables['time_bnds'][:]
projection_y_coordinate = nc.variables['projection_y_coordinate'][:]
projection_y_coordinate_bnds = nc.variables['projection_y_coordinate_bnds'][:]
projection_x_coordinate = nc.variables['projection_x_coordinate'][:]
projection_x_coordinate_bnds = nc.variables['projection_x_coordinate_bnds'][:]
percentile = nc.variables['percentile'][:]
latitude = nc.variables['latitude'][:]
longitude = nc.variables['longitude'][:]
month_number = nc.variables['month_number'][:]
season = nc.variables['season'][:]
season_year = nc.variables['season_year'][:]
year = nc.variables['year'][:]

