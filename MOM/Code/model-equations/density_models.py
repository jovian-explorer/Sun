import numpy as np
import matplotlib.pyplot as plt 
import warnings
warnings.filterwarnings("ignore")
plt.figure(figsize=(10,6)) #,dpi=1200
theta =90 # np.arange(0, 90, 0.0009)
r = np.arange(0.1,5.1,0.00005)

A = (((1.55* (10**14)) / r**6)  + (3.44*(10**11)))* (((np.cos(theta*np.pi))**2 * (1/64)*(np.sin(theta))**2)**(-1/2))   # Tyler et al. 1977
B = (((2.39* (10**14)) / r**6)  + (1.67*(10**12)/ (r**(2.3))))*(10**(-0.9*theta*np.pi/90))                             # Beman et al. 1977
C = (1.58* 10**17)/((r-1)**2)                                                                                          # Cairns et al. 2009
D = 14.2*(10**10)*(10**(4.32/r))                                                                                       # Newkirk et al. 1961
E = (10**14)*((2.99/(r**16))+(1.55/(r**6)))                                                                            # Allen-Baubach et al. 1947
F = (10**12)*((65/(r**5.94))+(0.768/((r-1)**2.25)))                                                                    # Wexler et al. 2019
G = ((8* 10**13)/(r**6))+((4.1* 10**12)/(r**4))+((3.3* 10**11)/(r**2))                                                 # LeBlanc et al. 1998 
H = (10**12)*((30/r**6)+(1/r**2.2))                                             # HELIOS 2                             # Patzold et al. 1987
I = (10**12)*((100/r**6)+(0.5/r**2.1))                                          # HELIOS 2                             # Esposito et al. 1980
J = (10**12)*((1.32/r**2.7)+(0.23/r**2.04))                                     # VIKING                               # Muhleman et al 1981



plt.plot(r,A/10**16, label ="Tyler et al. 1977")
plt.plot(r,B/10**16, label = "Beman et al. 1977")
# plt.plot(r,C/10**16, label = "Cairns et al. 2009")
plt.plot(r,D/10**16, label = "Newkirk et al. 1961")
plt.plot(r,E/10**16, label = "Allen-Baubach 1947")
plt.plot(r,F/10**16, label = "Wexler et al. 2019")
plt.plot(r,G/10**16, label = "LeBlanc et al. 1998")
plt.plot(r,H/10**16, label = "Patzold et al. 1987")
plt.plot(r,I/10**16, label = "Esposito et al. 1980")
plt.plot(r,J/10**16, label = "Muhleman et al. 1981")


plt.yscale('log')
plt.title("Electron Density in IPS")
# plt.gca().set_aspect('equal', adjustable='box')
plt.legend(loc='best')
plt.ylim(10**(-8),10**15)
plt.ylabel("$N_T(r) \longrightarrow$")
plt.xlabel("Distance b/w Sun and probe (in AU) ")
plt.show()
