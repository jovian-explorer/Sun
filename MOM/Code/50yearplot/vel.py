#------------------------------------------------------------------------------------------------------------------
#importing libraries
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")
fig,ax = plt.subplots()
#fig,ax = plt.subplots(figsize = (20,40),dpi = 1200)
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
#**Parker_1958**
Parker_1958 = '/home/dev/Sun/velocity/curve_1.csv'
Parker = pd.read_csv(Parker_1958,delimiter = ',')
Parker.columns = ["x","y"]
RAD_Parker = np.array(Parker.x)
VEL_Parker = np.array(Parker.y)
plt.loglog(RAD_Parker,VEL_Parker,label = "Curve 1")
# -----------------------------------------------------------------------------------------------------------------
#**curve_2**
curve_2 = '/home/dev/Sun/velocity/curve_2.csv'
curve__2 = pd.read_csv(curve_2,delimiter = ',')
curve__2.columns = ["x","y"]
RAD_curve__2 = np.array(curve__2.x)
VEL_curve__2 = np.array(curve__2.y)
plt.loglog(RAD_curve__2,VEL_curve__2,label = "Curve 2")
# -----------------------------------------------------------------------------------------------------------------
#**Parker_1958**
curve__3 = '/home/dev/Sun/velocity/curve_3.csv'
curve_3 = pd.read_csv(curve__3,delimiter = ',')
curve_3.columns = ["x","y"]
RAD_curve_3 = np.array(curve_3.x)
VEL_curve_3 = np.array(curve_3.y)
plt.loglog(RAD_curve_3,VEL_curve_3,label = "Curve 3")
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
#**Ekers_Little_1971**
ekers_1971 = '/home/dev/Sun/velocity/ekers_little_1971.csv'
ekers = pd.read_csv(ekers_1971,delimiter = ',')
ekers.columns = ["x","y"]
RAD_ekers = np.array(ekers.x)
VEL_ekers = np.array(ekers.y)
plt.plot(RAD_ekers,VEL_ekers,'v',label="Ekers_Little_1971")
# -----------------------------------------------------------------------------------------------------------------
plt.scatter(1.7,24,label="Woo_1978")
# -----------------------------------------------------------------------------------------------------------------
#**BRADFORD & ROUTLEDGE 1980**
bradford_1980 = '/home/dev/Sun/velocity/bradford_routledge_1980.csv'
bradford = pd.read_csv(bradford_1980,delimiter = ',')
bradford.columns = ["x","y"]
RAD_bradford = np.array(bradford.x)
VEL_bradford = np.array(bradford.y)
plt.plot(RAD_bradford,VEL_bradford,'^',label="Bradford_Routledge_1980")
# -----------------------------------------------------------------------------------------------------------------
#**ARMSTRONG_WOO 1981**
armstrong_1981 = '/home/dev/Sun/velocity/armstrong_woo_1981.csv'
armstrong1 = pd.read_csv(armstrong_1981,delimiter = ',')
armstrong1.columns = ["x","y"]
RAD_armstrong_1981 = np.array(armstrong1.x)
VEL_armstrong_1981 = np.array(armstrong1.y)
plt.plot(RAD_armstrong_1981,VEL_armstrong_1981,'d',label="Armstrong_Woo_1981")
# -----------------------------------------------------------------------------------------------------------------
#**EFIMOV 1981**
efimov_1981 = '/home/dev/Sun/velocity/efimov_1981.csv'
efimov = pd.read_csv(efimov_1981,delimiter = ',')
efimov.columns = ["x","y"]
RAD_efimov = np.array(efimov.x)
VEL_efimov = np.array(efimov.y)
plt.plot(RAD_efimov,VEL_efimov,'s',label="Efimov_1981")
# -----------------------------------------------------------------------------------------------------------------
#**tyler_1981**
tyler_1981 = '/home/dev/Sun/velocity/tyler_1981.csv'
tyler = pd.read_csv(tyler_1981,delimiter = ',')
tyler.columns = ["x","y"]
RAD_tyler = np.array(tyler.x)
VEL_tyler = np.array(tyler.y)
plt.plot(RAD_tyler,VEL_tyler,'p',label="Tyler_1981")
# -----------------------------------------------------------------------------------------------------------------
#**scott_1983**
scott_1983 = '/home/dev/Sun/velocity/scott_1983.csv'
scott = pd.read_csv(scott_1983,delimiter = ',')
scott.columns = ["x","y"]
RAD_scott = np.array(scott.x)
VEL_scott = np.array(scott.y)
plt.plot(RAD_scott,VEL_scott,'*',label="Scott_1983")
# -----------------------------------------------------------------------------------------------------------------
#**BOURGOIS 1985**
bourgois_1985 = '/home/dev/Sun/velocity/bourgois_1985.csv'
bourgois = pd.read_csv(bourgois_1985,delimiter = ',')
bourgois.columns = ["x","y"]
RAD_bourgois = np.array(bourgois.x)
VEL_bourgois = np.array(bourgois.y)
plt.scatter(RAD_bourgois,VEL_bourgois,label="Bourgois_1985")
# -----------------------------------------------------------------------------------------------------------------
#**ARMSTRONG 1986**
armstrong_1986 = '/home/dev/Sun/velocity/armstrong_1986.csv'
armstrong = pd.read_csv(armstrong_1986,delimiter = ',')
armstrong.columns = ["x","y"]
RAD_armstrong_1986 = np.array(armstrong.x)
VEL_armstrong_1986 = np.array(armstrong.y)
plt.scatter(RAD_armstrong_1986,VEL_armstrong_1986,label="Armstrong_1986")
# -----------------------------------------------------------------------------------------------------------------
#**yabukov_1991**
yabukov_1991 = '/home/dev/Sun/velocity/yabukov_1991.csv'
data_yabukov_1991 = pd.read_csv(yabukov_1991,delimiter = ',')
data_yabukov_1991.columns = ["x","y"]
RAD_yabukov_1991 = np.array(data_yabukov_1991.x)
VEL_yabukov_1991 = np.array(data_yabukov_1991.y)
plt.scatter(RAD_yabukov_1991,VEL_yabukov_1991,label="Yabukov_1991")
# -----------------------------------------------------------------------------------------------------------------
#**efimov_1994**
efimov_1994 = '/home/dev/Sun/velocity/efimov_1994.csv'
data_efimov_1994 = pd.read_csv(efimov_1994,delimiter = ',')
data_efimov_1994.columns = ["x","y"]
RAD_efimov_1994 = np.array(data_efimov_1994.x)
VEL_efimov_1994 = np.array(data_efimov_1994.y)
plt.scatter(RAD_efimov_1994,VEL_efimov_1994,label="Efimov_1994")
# -----------------------------------------------------------------------------------------------------------------
#**efimov_2002**
efimov_2002 = '/home/dev/Sun/velocity/efimov_2002.csv'
data_efimov_2002 = pd.read_csv(efimov_2002,delimiter = ',')
data_efimov_2002.columns = ["x","y"]
RAD_efimov_2002 = np.array(data_efimov_2002.x)
VEL_efimov_2002 = np.array(data_efimov_2002.y)
plt.scatter(RAD_efimov_2002,VEL_efimov_2002,label="Efimov_2002")
# -----------------------------------------------------------------------------------------------------------------
#**efimov_2010**
efimov_2010 = '/home/dev/Sun/velocity/efimov_2010.csv'
data_efimov_2010 = pd.read_csv(efimov_2010,delimiter = ',')
data_efimov_2010.columns = ["x","y"]
RAD_efimov_2010 = np.array(data_efimov_2010.x)
VEL_efimov_2010 = np.array(data_efimov_2010.y)
plt.scatter(RAD_efimov_2010,VEL_efimov_2010,label="Efimov_2010")
# -----------------------------------------------------------------------------------------------------------------
#**Imamura_2014**
Imamura_2014 = '/home/dev/Sun/velocity/Imamura_2014.csv'
data_Imamura_2014 = pd.read_csv(Imamura_2014,delimiter = ',')
data_Imamura_2014.columns = ["x","y"]
RAD_Imamura_2014 = np.array(data_Imamura_2014.x)
VEL_Imamura_2014 = np.array(data_Imamura_2014.y)
plt.scatter(RAD_Imamura_2014,VEL_Imamura_2014,label="Imamura_2014")
# -----------------------------------------------------------------------------------------------------------------
#**deforest_2018**
deforest_2018 = '/home/dev/Sun/velocity/deforest_2018.csv'
data_deforest_2018 = pd.read_csv(deforest_2018,delimiter = ',')
data_deforest_2018.columns = ["x","y"]
RAD_deforest_2018 = np.array(data_deforest_2018.x)
VEL_deforest_2018 = np.array(data_deforest_2018.y)
plt.scatter(RAD_deforest_2018,VEL_deforest_2018,label="Deforest_2018")
# -----------------------------------------------------------------------------------------------------------------
#**efimov_2018**
efimov_2018 = '/home/dev/Sun/velocity/efimov_2018.csv'
data_efimov_2018 = pd.read_csv(efimov_2018,delimiter = ',')
data_efimov_2018.columns = ["x","y"]
RAD_efimov_2018 = np.array(data_efimov_2018.x)
VEL_efimov_2018 = np.array(data_efimov_2018.y)
plt.scatter(RAD_efimov_2018,VEL_efimov_2018,label="Efimov_2018")
# -----------------------------------------------------------------------------------------------------------------
#**wexler_2020**
wexler_2020 = '/home/dev/Sun/velocity/wexler_2020.csv'
data_wexler_2020 = pd.read_csv(wexler_2020,delimiter = ',')
data_wexler_2020.columns = ["x","y"]
RAD_wexler_2020 = np.array(data_wexler_2020.x)
VEL_wexler_2020 = np.array(data_wexler_2020.y)
plt.plot(RAD_wexler_2020,VEL_wexler_2020,'+',label="Wexler_2020")
# -----------------------------------------------------------------------------------------------------------------
#**PSP**
PSP_2022 = '/home/dev/Sun/velocity/PSP_2022.csv'
PSP = pd.read_csv(PSP_2022,delimiter = '\t')
PSP.columns = ["x","y"]
RAD_PSP = np.array(PSP.x)
VEL_PSP = np.array(PSP.y)
plt.plot(RAD_PSP*215,VEL_PSP,'x',label="PSP_2022")
# -----------------------------------------------------------------------------------------------------------------
#**Chiba Akatsuki 2022**
Chiba_Akatsuki_2022 = '/home/dev/Sun/velocity/Chiba_Akatsuki_2022.csv'
Chiba_Akatsuki = pd.read_csv(Chiba_Akatsuki_2022,delimiter = ',')
Chiba_Akatsuki.columns = ["x","y"]
RAD_Chiba_Akatsuki = np.array(Chiba_Akatsuki.x)
VEL_Chiba_Akatsuki = np.array(Chiba_Akatsuki.y)
plt.plot(RAD_Chiba_Akatsuki,VEL_Chiba_Akatsuki,'+',label="Chiba_Akatsuki_2022")
# -----------------------------------------------------------------------------------------------------------------
#**MOM**
rad_MOM_RS = (8.1,6.92,5.77,5.24,6.33,7.49)
rad_MOM_AU = (0.0376682,0.03218077,0.0268328,0.024368,0.0294370387,0.034831504)
MOM = (172.2372178,112.83713799,126.64897552,189.53094138,212.84972353,260.6076649290)
c = [0.25*172.2372178,0.25*112.83713799,0.25*126.64897552,0.25*189.53094138,0.25*212.84972353,0.25*260.6076649290]
#plt.plot(rad_MOM_RS,MOM,'kX',label="MOM_2021")
plt.plot(rad_MOM_RS,MOM,yerr = 0.25)
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#plt.scale("log")
plt.ylabel("SOLAR WIND VELOCITY $(km/s) \longrightarrow$")
plt.xlabel("SOLAR DISTANCE (in $R_{\odot}$) $\longrightarrow$ ")
#plt.legend(ncol = 4,loc='lower center',bbox_to_anchor=(0.5, -2))
plt.legend(bbox_to_anchor=(-0.2, 1.02, 1.2, .102), loc=3,ncol=3, mode="expand", borderaxespad=0.)
plt.tight_layout()
plt.ylim(20,1000)
plt.xlim(1,100)
ax.set_aspect('equal', adjustable='box')
ax.set_xticks([1,2,3,5,10,20,30,50,100])
ax.set_yticks([20,30,50,100,200,300,500,1000])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.show()
