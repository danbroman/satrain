###DOWNLOAD HOURLY NASA TRMM 3B42RT PRODUCT
##############################
##IMPORT MODULES
import datetime as dt #for getting current date/time
import pytz #for setting time zone
import urllib #for downloading file from url
import numpy as np #for array storage and manipulation
import numpy.ma as ma #for add'l array operations
import gzip #for reading gzip files
import os #for access to system commands
##############################
##USER INPUTS
rdhead = 'ftp://trmmopen.gsfc.nasa.gov/pub/merged/mergeIRMicro/'
rdid = '3B42RT.' #product id in url
rdext = '.bin.gz' #file extension in url
savdir = '/d2/dbroman/trmm/raw/' #dir to save raw file
savid = '3B42RTv7.'  #product id in raw file
savext = rdext #file extension in raw file ..set to same as id in url
dattyp = np.dtype('int16') 
hlag = 3 #hour lag on file access
##############################
hrstr = ['03', '06', '09', '12', '15', '18', '21', '00'] #st
hrvec = np.array([3, 6, 9, 12, 15, 18, 21, 0])
d = dt.datetime.now(tz = pytz.utc) - dt.timedelta(hours = hlag)
year = str(d.year)
month = str('%02d' % (int(d.month)))
day = str('%02d' % (int(d.day)))
hrnow = int(d.hour)
hour = hrstr[np.argmax(ma.masked_greater(hrvec - hrnow, 0))]
hoursav = str('%04d' % (int(hour) * 100))
url = rdhead + year + '/' + rdid + year + month + day + hour + '.7' + rdext
rawsav = savdir + savid + year + month + day + '.' + hoursav + rdext 
##############################
##DOWNLOAD FILE
if os.path.isfile(rawsav) is False: #checks if raw file exists
    try:
        urllib.urlretrieve(url, rawsav) #downloads file from url and saves to specified directory
    except (RuntimeError, TypeError, NameError, IOError):
        pass



    
