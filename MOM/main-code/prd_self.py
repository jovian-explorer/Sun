#program to read binary file - generate Header file - of akatsuki.prd file and Calculate - Epxerimental doppler (4 values in 1 sec) 


import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

#------------------------------------------------
m = 9.1*10**(-31)
e = 1.6*10**(-19)
frec = 8410640000.0
k= 1
l_2= 1
alpha = 1.14*10**(-24)
#------------------------------------------------
#------------------------------------------------
#function to calculate moment :
#x = value whose moment calculate = frequency, 
#powerspec = powerspectrum / probability distribution func
#c = the point around which the moment is taken , as we are taking raw moment (c=0)
#n = order of moment/power of (x-c)**n


def powSpecmoment(freq, powSpec):
    n= powSpec.size 
    global maxpowindx, freq_arr, pow_spec
    maxpowindx = np.argmax(powSpec)                             #----> index of powSpec and corrosponding freq array , where fftAA(or power spec density) is maximum

#We take 32 data points +/- around peak(max spec power) to find moments. But if peak occurs at index<32 or index>(n-32), then take into account end and tail missing points

    if (maxpowindx<=32):
        freq_arr = freq[0:maxpowindx+32]  
        #arrary containing 32 point +- maximum index , it is assumed that signal is 4byte, anywhere b/n +-32 points
        pow_spec = powSpec[0:maxpowindx+32]
    elif (maxpowindx>=(n-32)):
        freq_arr = freq[maxpowindx-32:-1]                       #arrary containing 32 point - maximum index, and till last index 
        pow_spec = powSpec[maxpowindx-32:-1]
    else:
        freq_arr = freq[maxpowindx-32:maxpowindx+32]            #arrary containing 32 point +- maximum index 
        pow_spec = powSpec[maxpowindx-32:maxpowindx+32]    

#Now,do noise floor level (L) estimation and substracting it from total noisy signal power(pow_spec) to find, noiseless signal power - Using method mentioned in Hildebrand et. al
   
    sortpsd = np.sort(pow_spec)                                 #sort array in ascending order, calculate mean and variance of grps of element, if R=(var/mean)<1 , take it as noiselevel 

    noiselevelL = 0.0
    Lindx = 1
    sumP = 0.0                                                  #mean
    sumPQ = 0.0                                                 #stddev

    for k in range(len(sortpsd)):
        sumP = sumP+sortpsd[k]
        sumPQ = sumPQ +(sortpsd[k])**2
        R = (k*sumPQ - sumP*sumP)/(sumP*sumP)
        if R<1 :
            noiselevelL = sumP
            Lindx = k

    noise = noiselevelL/Lindx                                   #noise power
    unpow = pow_spec - noise                                    #noiseless signal power - substract noiselevel from spectrum 
    '''
	Now find index of peak value'l' in spectrum , find 'm'-minimum indx of positive point, and 'n'- maximum indx of positive point, corrosponding to valley point of detected peak doppler spectrum
	'''
    lindx = np.argmax(unpow)  					#indx of peak value
                                                                #dividing spectrum in two parts
    fhpower = unpow[0:lindx]					#first half-power spectrum, usually lindx=32
    shpower = unpow[lindx:] 					#second half-power spectrum
                                                                #now in this half spectrum, find 'm'(minimum indx of positive points,near bottom ofpeak) 
                                                                #for 'm' in first-half spectrum, 'm'= minimum indx of positive points = maximum indx of negative points
    fhIndxes = np.where(fhpower<0)
    if (np.size(fhIndxes)==0) : minIndx = 0                     #if minIndx array is empty ([]), its size is 0, i.e. all point are above zero in first half-spectrum, then start index from 0
    else : minIndx = np.max(fhIndxes)
    
    #for 'n' in second half of spectrum (maximum indx of positive points corrospoding to valley of peak) -= min indx of negative points , add lindx to find corrosponding indx in entire spectrum
    shIndxes= np.where(shpower<0) + lindx 
    if (np.size(shIndxes) == 0) : maxIndx = len(unpow)          #if maxIndx array is empty, i.e. all point are above zero in second half-spectrum, then max indx as final indx
    else : maxIndx = np.min(shIndxes)                           #now take points corrosponding to peak of noiseless power to calculate moment

    moPower = unpow[minIndx:maxIndx]
    moFreq = freq_arr[minIndx:maxIndx]
    zeroth_moment = np.sum(moPower)                             #zeroth moment =  total power = sum(powerspec)
    first_moment = np.sum(moPower*(moFreq)) / np.sum(moPower)   #first moment = doppler freq shift = np.sum(powerspec*(freq)) / np.sum(powerspec) 
    second_moment = np.sum(((moFreq-first_moment)**2)*moPower) / np.sum(moPower)
    RTEC = (second_moment/(alpha*(downconfreq)**(-1.2)))**(1/1.2)
    
    '''
    density = 
    plasma_frequency_model_1 = np.sqrt(4*np.pi*density*(e**2)/m)#Yamato et al. 2002
    plasma_frequency_model_2 = np.sqrt(density*(e**2)/(np.pi*m))#Richa di sent this. source unknown to me
    
    #refractive index equation taken from Hollweg et al. 1970
    refractive_index_model_1 = np.sqrt(1 - (plasma_frequency_model_1/frec)**2)
    refractive_index_model_2 = np.sqrt(1 - (plasma_frequency_model_2/frec)**2)
    
    #angular broadening taken from Hollweg et al. 1970
    angular_broadening_model_1 = 
    angular_broadening_model_2 =
    
    #Solar wind velocity taken from Bird et al. 1982
    solar_wind_velocity_model_1 = (5.77*frec*L)/(angular_broadening_model_1*k*l_2) 
    solar_wind_velocity_model_2 = (5.77*frec*L)/(angular_broadening_model_2*k*l_2)
    '''
    return [zeroth_moment,first_moment,second_moment,RTEC]#,density,plasma_frequency_model_1,plasma_frequency_model_2,refractive_index_model_1,refractive_index_model_2,angular_broadening_model_1,angular_broadening_model_2,solar_wind_velocity_model_1,solar_wind_velocity_model_2] 
    

#---------------------------------



f = open('/home/dev/Sun/akatsuki_product_file.prd',"rb")

i=1

#start reading the Binary file -Header + data
while True:

    
    byte = np.fromfile (f, dtype = '|S4' , count = 1 , sep = '')

    if not byte.size>0:  #at EOF byte is empty, then while loop will break and reading stops 
        break
    """
    if not byte:
	DeprecationWarning: The truth value of an empty array is ambiguous.
	Returning False, but in future this will result in an error.
	Use `array.size > 0` to check that an array is not empty.
	"""

    rec_len = np.fromfile (f, dtype = '<i4' , count = 1 , sep = '' )

    rec_ver = np.fromfile (f, dtype = '<i2' , count = 1 , sep = '')

    stat_id = np.fromfile (f, dtype = '<i2' , count = 1 , sep = '')

    spcr_id = np.fromfile (f, dtype = '<i2' , count = 1 , sep = '')

    sam_size = np.fromfile (f, dtype = '<i2' , count = 1 , sep = '')

    sam_rate = np.fromfile (f, dtype = '<i4' , count = 1 , sep = '')

    val_flag = np.fromfile (f, dtype = '<i2' , count = 1 , sep = '')

    agn_flag = np.fromfile (f, dtype = '<i2' , count = 1 , sep = '')

    rf_to_if = np.fromfile (f, dtype = '<f8' , count = 1 , sep = '')

    if_to_ch = np.fromfile (f, dtype = '<f8' , count = 1 , sep = '')

    tt_year = np.fromfile (f, dtype = '<i2' , count = 1 , sep = '')

    tt_doy = np.fromfile (f, dtype = '<i2' , count = 1 , sep = '')

    tt_sec = np.fromfile (f, dtype = '<i4' , count = 1 , sep = '')

    tt_picosec = np.fromfile (f, dtype = '<f8' , count = 1 , sep = '')

    ch_ph = np.fromfile (f, dtype = '<f8' , count = 1 , sep = '')

    ch_py_0 = np.fromfile (f, dtype = '<f8' , count = 1 , sep = '')

    ch_py_1 = np.fromfile (f, dtype = '<f8' , count = 1 , sep = '')

    ch_py_2 = np.fromfile (f, dtype = '<f8' , count = 1 , sep = '')

    ch_py_3 = np.fromfile (f, dtype = '<f8' , count = 1 , sep = '')

    empt_fe = np.fromfile (f, dtype = '|S1' , count = 36 , sep = '')

    empt_iau = np.fromfile (f, dtype = '|S1' , count = 40 , sep = '')  

    end_label = np.fromfile (f, dtype = '<i4' , count = 1 , sep = '')  
    #dtype = '<i2' = int16 , signed interger 16 bits (2 bytes) , dt = np.dtype('<i2') --> dt.name --> int16
    #read data 
    #data  = np.fromfile (f, dtype = '<i1' , count = 400000, sep = '')  
    #this contains I-Q channel data, where I-1byte each=200000 points per sec (sample rate= 200000) , stored as I-Q-I-Q-I----- 
    #pointer = f.tell()  # f.tell() --> 	Returns the current byte position of the file pointer.
    #--> 400176 , ie. 1st second data containing sample rate = 20000 points in one sec is read, along with its header 

# II - write header in output 'Header.txt' file 

    fout = open("header_4point.txt", 'a+')                     #header of output file
    fout.write('Record level = '+str(byte[0])+'\n') 
    fout.write('Record lenghth = '+str(rec_len[0])+'\n')   
    fout.write('Record version ID = '+str(rec_ver[0])+'\n')   
    fout.write('Station ID = '+str(stat_id[0])+'\n') 
    fout.write('Spacecraft ID = '+str(spcr_id[0])+'\n')    
    fout.write('Sample size =    '+str(sam_size[0])+'\n')
    fout.write('Sample rate =    '+str(sam_rate[0])+'\n')
    fout.write('Validity flag =  '+str(val_flag[0])+'\n')    
    fout.write('Agency flag =    '+str(agn_flag[0])+'\n')
    fout.write('RF_TO_IF downconv = '+str(rf_to_if[0])+'\n') 
    fout.write('If_To_Channel Downconv = '+ str(if_to_ch[0])+'\n')
    fout.write('Time tag year = '+str(tt_year[0])+'\n')    
    fout.write('Tlime Tag Doy = '+str(tt_doy[0])+'\n')   
    fout.write('Time Tag Second of Day = '+str(tt_sec[0])+'\n')    
    fout.write('Timetag picoseconds of the second = '+str(tt_picosec[0])+'\n') 
    fout.write('Channel Accumulted Phase = '+str(ch_ph[0])+'\n') 
    fout.write('Channel Phase polynomial coefficient_0 = '+str(ch_py_0[0])+'\n')
    fout.write('Channel Phase polynomial coefficient_1 = '+str(ch_py_1[0])+'\n')
    fout.write('Channel Phase polynomial coefficient_2 = '+str(ch_py_2[0])+'\n')
    fout.write('Channel Phase polynomial coefficient_3 = '+str(ch_py_3[0])+'\n')  
    fout.write('Empty Fields F_S = '+str(empt_fe[0])+'\n')  
    fout.write('Empty Fields I_A = '+str(empt_iau[0])+'\n')  
    fout.write('End Label = '+str(end_label[0])+'\n')
    fout.write('-------------------------------------------------'+'\n') 



#III - analysis Data : data array has I-Q channel read as two separate array 

    tfreq = 8410932002.0000                                    #tfreq = transmitted freq = 8410932002.0000 Hz given in .obs file of Akatsuki X Band 8.4 GHz
    downconfreq = rf_to_if[0]                                  # RF_TO_IF downconv frequency as read from header file 8410640000.0

    data=np.fromfile(f,dtype ='<i1',count = 400000, sep = '')  #this contains I-Q channel data ,alternatively as I-Q-I-Q......
                                                               # data is 1D array (400000,) to store I-Q channel values separately. 
                                                               #Slice the 1D-data array list[start:stop:step] : I-values at even idices- data[::2], Q-values at odd indices [1::2]  
    I_data = data[::2]                                         #slice I-data at even indices
    Q_data = data[1::2]                                        # slice Q-data at odd indices 

    AA = I_data + 1j * Q_data                                  #creating complex number array AA = I+j*Q  ---> amplitude

                                                               #find FFT transform of AA(amplitude), using numpy.fft.fft() 

    n = np.size(AA)                                            #---> n = 200000 = total size of AA data = window length of fft 

                                                               #this is one second data , now we want doppler at intervals of 0.25 sec,divide 1 sec data into intervals at 0.25 sec, i.e. 4 intervals
    interval = 0.25                                            #sec , divide one sec data into 4 parts (start value is included and endvalue is not)--> s=np.linspace(0,1,4,endpoint=False)-->[0., 0.25, 0.5 , 0.75]
    
    section = int(1/interval)                                  #1 sec divided into 4 sections = 4 point interval 
    windwsize = int(n/section)                                 #size of window of data  = for 10 sections, total n = 200000 data points, willbe divided in windwsize = n/section = 200000
                                                               #now slice total Amplitude data into single section of windowsize and calculate moments, and then slide the window
    
    start = 0
    end = windwsize
    
    for j in range(section):
        AA1 =  AA[start:end]                                    #AA1 - sliced data to 0.1 sec interval, i.e. 20000 data points , now calculate its fft and moment

        fftAA1 = np.fft.fft(AA1,n)/n                            #----> calculate FFT of AA amplitude (normalized value),NOTE - numpy.fft.fft()gives value of fft, but it is not normalized to normalize it, divide by total n, here windowsize for fft  = n = total 200000 , assuming zero padding 
        fftAA1_abs = abs(fftAA1)                                #---> absolute value of fftAA fft of amplitude 

        sample_rate = sam_rate[0]                               #----> sampling rate read from header
        d = 1/sample_rate                                       #-----> sample spacing = d = 1/sample_rate

        freq = np.fft.fftfreq(n,d)                              #----> corresponding frequency bins for fftAA

        powSpec= (fftAA1_abs)**2                                #power spectral density = square of amplitude of fft 
    
        '''
        Finding Moments of powSpec (Power spectral density distribution)- by defining "powSpecmoment" function - 
        zeroth moment = power, 
        first moment = doppler freq, 
        second = width of freq spread
        '''
        momentout = powSpecmoment(freq, powSpec) 		#powSpecmoment(frequency, powSpec)
        power_total = momentout[0] 				#zeroth moment 
        dopp_firstmoment = momentout[1]  			#first moment
        second_moment = momentout[2]                            #second moment
        RTEC=momentout[3]                                       #radial total electron content
        '''
        density=momentout[4]                                    #number Density
        plasma_frequency_model_1=momentout[5]                   #plasma_frequency_model_1
        plasma_frequency_model_2=momentout[6]                   #plasma_frequency_model_2
        refractive_index_model_1=momentout[7]                   #refractive_index_model_1
        refractive_index_model_2=momentout[8]                   #refractive_index_model_2
        angular_broadening_model_1=momentout[9]                 #angular_broadening_model_1
        angular_broadening_model_2=momentout[10]                #angular_broadening_model_2
        solar_wind_velocity_model_1=momentout[11]               #solar_wind_velocity_model_1
        solar_wind_velocity_model_2=momentout[11]               #solar_wind_velocity_model_2
        '''
        
        '''
	final experimental/Observed doppler shift observed in received signal is (given by heterodyning principle)  
	Observed Doppler = Down conversion Frequency + FFT value (Doppler) – Transmitted frequency 
	exp_dopp = Downconversion frequency + dopp_firstmoment_freq - transmitted freq
        IV - write output in "output.txt" file containging :  time in seconds----power(first moment)-----measured dopp freq
        '''

        exp_dopp =  downconfreq + dopp_firstmoment - tfreq 
        timesec = tt_sec[0]+j*interval                           #time in sec 6300.1, 6300.2
        
        foutput = open("output_expdopp_4point.txt", "a+")
        foutput.writelines(str(i)+','+str(timesec)+','+str(power_total)+','+ str(downconfreq) +','+ str(dopp_firstmoment) + ','+ str(exp_dopp) + ','+str(second_moment) + ','+ str(RTEC)+'\n')  #','+ str(density)+','+ str(plasma_frequency_model_1)+','+ str(plasma_frequency_model_2)+','+ str(refractive_index_model_1)+','+ str(refractive_index_model_2)+','+ str(angular_broadening_model_1)+','+ str(angular_broadening_model_2)+','+ str(solar_wind_velocity_model_1)+','+ str(solar_wind_velocity_model_2)+'\n')
        start = end
        end = start+windwsize

        #o.1 sec loop ends
    print (i)
    i=i+1 

# repeat the while loop of reader  again, till EOF (End of Binary file) is reached

f.close()                                                        #close akt.prd file
fout.close()                                                     #close header file
foutput.close()                                                  #close output file
