
'''
file to plot using the 'output_expdopp_4point.csv'
exp_dopp =  downconfreq + dopp_firstmoment - tfreq 
where treq = 8410932002.0000 #tfreq = transmitted freq given in .obs file of Akatsuki X Band 8.4 GHz


structure of the csv-  
i,timesec,power_total,downconfreq,dopp_firstmoment,exp_dopp, second_moment
'''

#importing libraries required
#-----------------------------------------------------------------------------------------------------------------
#importing libraries
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------------------------------------------
#importing data from my GitHub
url = '/home/dev/Sun/output_expdopp_4point.txt'
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', None)
dataset = pd.read_csv(url,delimiter = ',')
print(dataset.head(1))
#-----------------------------------------------------------------------------------------------------------------
# accessing the different columns of the csv dataset I made above
dataset.columns = ["i","timesec","power_total","downconfreq","dopp_firstmoment","exp_dopp","second_moment"]
#storing values for each column into a separate arrays

'''
Finding Moments of powSpec (Power spectral density distribution)- by defining "powSpecmoment" function - 
zeroth moment = power, 
first moment = doppler freq
second = width of freq spread 
downconfreq - RF_TO_IF downconv frequency as read from header file
final experimental/Observed doppler shift observed in received signal is (given by heterodyning principle)  
exp_dopp = Downconversion frequency + dopp_firstmoment_freq - transmitted freq
IV - write output in "output.txt" file containing :  time in seconds----power(first moment)-----measured dopp freq
'''
i = np.array(dataset.i)           		  	  # Values of iteration
timesec= np.array(dataset.timesec)               	  # Values of time in sec 6300.1, 6300.2
power_total= np.array(dataset.power_total)                # Values of zeroth moment 
downconfreq= np.array(dataset.downconfreq)                # Values of downconfreq
dopp_firstmoment= np.array(dataset.dopp_firstmoment)      # Values of first moment 
exp_dopp= np.array(dataset.exp_dopp)                	  # Values of exp_dopp
second_moment = np.array(dataset.second_moment)	          # Values of second_moment
#-----------------------------------------------------------------------------------------------------------------

#Plotting v_lsr vs T_B
fig = plt.figure()
#plt.scatter(v_lsr, T_B, s = 1,label = "?")
#plt.plot(timesec/60, exp_dopp/(10**6),label = "exp_dopp")
#plt.plot(timesec/60,dopp_firstmoment/(10**6),label ="dopp_firstmoment")
plt.plot(timesec/60,second_moment/(10**6),label = "second_moment")
#plt.plot(timesec/60,(dopp_firstmoment-exp_dopp)/(10**6),label ="dopp_diff")
#plt.plot(timesec,downconfreq/(10**9),label ="downconfreq")
plt.xlabel("Time(min)$\longrightarrow$")
plt.ylabel("Frequency(MHz)$\longrightarrow$")
plt.title("test_plot")
plt.legend(loc = 'best')
plt.tight_layout()
fig.savefig('trial.png')
plt.show()
#-----------------------------------------------------------------------------------------------------------------
