The raw data folder contains zip files and xml files for 14 occultation events. Each zip file  comprises the zipped data (two prd files, obs and xml file) and an info file. 

Details of each zipped data:

The LEVEL-0 RAW data of the RAMBHA DFRS contains a zip file and an INFO file. The zip file contains two .prd files for X and S frequencies, and .obs file and an xml file. 
The level-0 raw data file in the RDEF format. RDEF is realized with two types of files: an Observation File made of a sequence of ASCII text lines and a Product File made of a sequence of binary data records. The Observation File contains information about the radio occultation measurement session. The Product File contains data collected during the  radio occultation measurement session. The file name shall uniquely define the receiver used to record data, the frequency channel, the spacecraft, the station, the scan, the file type, and the nominal scan start time. Each file shall be named according to the following convention:

MMMMnNNNtTsSSSSrRRcCC-YYDDDHHMMSS.XXX
MMMM :The spacecraft ID of the mission 
n    :token to indicate that scan identifier follows
NNN  :scan number per session (three-digit integer) starting from 001
t    :token to indicate file type
T    :file type; I: Observation file and S: spacecraft scan, Q:quasar scanfor th      e product file. I is for obs file, S for prd files and Q is not used
s    :token to indicate that station identifier follows
SSSS :station identifier (four characters), which shall be the same as the receiving station name in the Observation File for the given station
r    :token to indicate that the receiver identifier follows
RR   :receiver identifier 
c    :token to indicate that channel identifier follows
CC   :Channel identifier 01: S frequency, 02: X frequency
-    :token to indicate that date follows
YY   :the last two digits of the year for nominal scan epoch
DDD  :The day of the year for nominal scan epoch
HHMMSS:The hour-minute-second for nominal scan epoch
.XXX :the file extension: .obs for an Observation File, .prd for a Product File.

Observation File
There shall be one Observation File for each tracking station and for each measurement session. The Observation File shall be made of a sequence of ASCII text lines. 
The Observation File shall contain:
a) a single Observation Header Section, followed by 
b) one or more Scan Sections , followed by 
c) an Ending Section.
 Each scan session specifies the nominal start time and stop time for the scan in YYYY -DDDThh:mm:ss format. 

zds_olrconfig.xml
This is the xml label file of the observational file. In this file start and stop time are in the  YYYY-MM-DDThh:mm:ss format.

Product file
The Product File shall consist of several Records , each one containing exactly one second of data and related information to correlate such second of data. Each record shall consist of data represented in binary format. It shall be made of two Sections
a) The Header Section 
b) The Data Section
Each Product File shall contain data for one scan, one channel , and one station. The length of the Header Section is fixed and the Header contains 23 parameters and two empty fields for future expansion.  The length of the Data Section is variable and shall be determined by the sample rate and sample size of the recorded data. The total length of the Data Section shall be fully determined by the information written in the Header Section. The sample size of the DFRS payload will be always 8 bits.

INFO files
The INFO or Information files are generated to ensure the integrity of the data after file transfer.
For each file, the INFO file provides the file-size. The INFO file format shall be same as the format followed for the DFRS files posted from IDSN32, and is given as follows: 

<StnID> <Generating-Host-ID> <File-Type> <Orbit/DOY> <Size> <File-Name>

in a single line. 

The fields shall be defined as follows:

StnID 		  :Station Identifier.  Use DS95 for IDSN32, DS96 for IDSN18
Generating Host ID:OLR1- Open Loop Receiver 1 
		   OLR2 – Open Loop Receiver 2
		   MET1 – Meteorological Data Receiver 1 of IDSN32
		   MET2 – Meteorological Data Receiver 2 of IDSN32
File Type	   :RDEF – for RDEF zip file; MET – Meteorological data file.
Orbit/DOY          :FOR OLRs Current orbit number – in 5 digits for RDEF file. Example: 00021
                    Set to 0 if not known.
                    For Meteo: YYDOY – where YY is Year and DOY is day of year
Size              :File size in bytes.
File-name         :The file-name. Give only the file-name portion (without the full directory path).


The INFO file shall be named with the “inf” extension. An INFO file shall contain the same name as the original file name, except that the last file-extension of the original file shall be replaced with the “inf” file extension.

The INFO file for an RDEF zip file:  CH2O_ORBIT_DFRS_DS95_2019_005_OLR1.zip
Shall be named: CH2O_DS95_ORBIT_2019_005.inf and may contain the following contents (in a single line):

DS95 OLR1 RDEF 00023 12345678901 CH2O__ORBIT_DFRS_DS95_2019_005_OLR1.zip

This info file corresponds to the CH2O__ORBIT_DFRS_DS95_2019_005_OLR1.zip file which is 12,345,678,901 bytes in size (approx. 12 GB). It is identified as an RDEF file for orbit 23, and generated by OLR1. 


