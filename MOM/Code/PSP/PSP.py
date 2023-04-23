#-----------------------------------------------------------------------------------------------------------------
#importing libraries
from __future__ import print_function, division
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import scipy.interpolate as interp
import argparse
import copy
import datetime
import math
from matplotlib.gridspec import GridSpec
global low, up
from astropy.io import fits as f
from astropy.table import Table as t
from astropy.utils.data import download_file
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from mpl_toolkits import mplot3d
from scipy.optimize import curve_fit
import scipy.optimize as so
import warnings
warnings.filterwarnings("ignore")
#-----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------
#importing data from my GitHub
url2 = '/home/dev/Downloads/keshav_1to15.csv'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
dataset2 = pd.read_csv(url2,delimiter = ',')
#print(dataset2.head(5))
dataset2.columns = ['n','EPOCH','RADIAL_DISTANCE','HGI_LAT','HGI_LONG','BR_(RTN)','BT_(RTN)','BN_(RTN)','VR','VT','VN','PROTON_SPEED','PROTON_DENS','PROTON_TEMP']
EPOCH = np.array(dataset2.EPOCH)
VR = np.array(dataset2.VR)
VT = np.array(dataset2.VT)
VN = np.array(dataset2.VN)
PROTON_SPEED = np.array(dataset2.PROTON_SPEED)	        
# -----------------------------------------------------------------------------------------------------------------
fig = plt.figure(figsize = (8,4) , dpi= 80) 

plt.plot(EPOCH,VR,label="VR")
plt.plot(EPOCH,VT,label="VT")
plt.plot(EPOCH,VN,label="VN")
#plt.plot(EPOCH,PROTON_SPEED,label="VP")

plt.legend(loc = 'best')
plt.tight_layout()
plt.show()
