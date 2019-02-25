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
    print(i )
    
    
 

