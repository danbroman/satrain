###PROCESS LOCALLY DOWNLOADED FILES 
###FOR JAXA EORC GSMAP-RT PRODUCT
##############################
import sys
# print sys.path
print 'starting'
##IMPORT MODULES
import datetime as dt
import pytz
import urllib
import numpy as np
import numpy.ma as ma
import gzip
import os
##############################
##SET DIRECTORY PATH AND DATA LATENCY
rdhead = 'ftp://rainmap:Niskur+1404@hokusai.eorc.jaxa.jp/realtime/archive/'  
rdext = '.dat.gz'

savdirraw = '/d2/dbroman/gsmap-nrt/raw/'
savdirproc = '/d2/dbroman/gsmap-nrt/india/'
dattyp = np.dtype('<f4')
lonlen = 3600
latlen = 1200
lonvec = np.arange(0.05, 360, 0.1)
latvec = np.arange(-59.95, 60, 0.1)
hlag = 5
#INDIA SUBSET BOUNDS
latbounds = [22 , 32]
lonbounds = [73 , 98] 
latli = np.argmin(np.abs(latvec - latbounds[0]))
latui = np.argmin(np.abs(latvec - latbounds[1])) 
lonli = np.argmin(np.abs(lonvec - lonbounds[0]))
lonui = np.argmin(np.abs(lonvec - lonbounds[1]))
##############################
utc = pytz.utc
                #yyyy,m,d,h,m,s,ss
# ds = dt.datetime(2016,8,8,2,0,0,0, utc) #set start time
# d = dt.datetime(2016,8,8,21,0,0,0, utc) #set end time
d = dt.datetime.now(tz = utc) - dt.timedelta(hours = hlag)

# numhours = int((d-ds).total_seconds() / 60 / 60) + 2
numhours = 720
dlist = [d - dt.timedelta(hours = x) for x in range(0, numhours)]

for i in range(0, numhours-1):
    year = str(dlist[i].year)
    month = str('%02d' % (int(dlist[i].month)))
    day = str('%02d' % (int(dlist[i].day)))
    hour = str('%04d' % (int(dlist[i].hour) * 100))

    url = rdhead + year + '/' + month + '/' + day + '/' + 'gsmap_nrt.' + year + month + day + '.' + hour + rdext
    binsav = savdirraw + 'gsmap_nrt.' + year + month + day + '.' + hour + rdext 
    binsubsav = savdirproc + 'gsmap_nrt_indiasub.' + year + month + day + '.' + hour + '.bin'

    if os.path.isfile(binsubsav) is False:
        if os.path.isfile(binsav) is False:
            try:
                # urllib.urlretrieve(url, binsav)
                os.system('wget ' + url + ' -O ' + binsav)
            except (RuntimeError, TypeError, NameError, IOError):
                continue
        #OPEN FILE INTO NP ARRAY
        try:
            varin = gzip.open(binsav)
            var = np.frombuffer(varin.read(), dtype = dattyp).reshape(latlen, lonlen).swapaxes(0,1)
            var = np.fliplr(var)
    
            #SUBSET TO INDIA
            varsub = var[lonli:lonui, latli:latui]    
    
            #SAVE SUBSET FILE
            varsub.astype('int16').tofile(binsubsav)  
   
        except (RuntimeError, TypeError, NameError, IOError):
            continue
