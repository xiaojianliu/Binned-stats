#http://www.ngdc.noaa.gov/mgg/coast/
# coast line data extractor

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:27:09 2012

@author: vsheremet
"""
import numpy as np
#from pydap.client import open_url
import matplotlib.pyplot as plt
from SeaHorseLib import *
from datetime import *
#from scipy import interpolate
import sys
from SeaHorseTide import *
import shutil
import matplotlib.mlab as mlab
import matplotlib.cm as cm

"""
from netCDF4 import Dataset

# read in etopo5 topography/bathymetry.
url = 'http://ferret.pmel.noaa.gov/thredds/dodsC/data/PMEL/etopo5.nc'
etopodata = Dataset(url)

topoin = etopodata.variables['ROSE'][:]
lons = etopodata.variables['ETOPO05_X'][:]
lats = etopodata.variables['ETOPO05_Y'][:]
# shift data so lons go from -180 to 180 instead of 20 to 380.
topoin,lons = shiftgrid(180.,topoin,lons,start=False)
"""



"""
BATHY=np.genfromtxt('necscoast_noaa.dat',dtype=None,names=['coast_lon', 'coast_lat'])
coast_lon=BATHY['coast_lon']
coast_lat=BATHY['coast_lat']
"""

#BATHY=np.genfromtxt('coastlineNE.dat',names=['coast_lon', 'coast_lat'],dtype=None,comments='>')
#coast_lon=BATHY['coast_lon']
#coast_lat=BATHY['coast_lat']


# www.ngdc.noaa.gov
# world vector shoreline ascii
FNCL='necscoast_worldvec.dat'
# lon lat pairs
# segments separated by nans
"""
nan nan
-77.953942	34.000067
-77.953949	34.000000
nan nan
-77.941035	34.000067
-77.939568	34.001241
-77.939275	34.002121
-77.938688	34.003001
-77.938688	34.003881
"""
CL=np.genfromtxt(FNCL,names=['lon','lat'])


FN='binned_drifter.npz'
#FN='binned_model.npz'
Z=np.load(FN) 
xb=Z['xb']
yb=Z['yb']
ub_mean=Z['ub_mean']
ub_median=Z['ub_median']
ub_std=Z['ub_std']
ub_num=Z['ub_num']
vb_mean=Z['vb_mean']
vb_median=Z['vb_median']
vb_std=Z['vb_std']
vb_num=Z['vb_num']
Z.close()

#cmap = matplotlib.cm.jet
#cmap.set_bad('w',1.)
xxb,yyb = np.meshgrid(xb, yb)
cc=np.arange(-1.5,1.500001,0.05)
#cc=np.array([-1., -.75, -.5, -.25, -0.2, -.15, -.1, -0.05, 0., 0.05, .1, .15, .2, .25, .5, .75, 1.])

plt.figure()
ub = np.ma.array(ub_mean, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_mean, mask=np.isnan(vb_mean))
Q=plt.quiver(xxb,yyb,ub.T,vb.T,scale=5.)
qk=plt.quiverkey(Q,0.8,0.1,0.5, r'$50cm/s$', fontproperties={'weight': 'bold'})

plt.title(FN[:-4]+', mean')

#plt.plot(coast_lon,coast_lat,'b.')
plt.plot(CL['lon'],CL['lat'])
plt.axis([-80,-55,34,48])
plt.show()

plt.figure()
ub = np.ma.array(ub_std, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_std, mask=np.isnan(vb_mean))
Q=plt.quiver(xxb,yyb,ub.T,vb.T,scale=5.)
qk=plt.quiverkey(Q,0.8,0.1,0.5, r'$50cm/s$', fontproperties={'weight': 'bold'})

plt.title(FN[:-4]+', std')

#plt.plot(coast_lon,coast_lat,'b.')
plt.plot(CL['lon'],CL['lat'])
plt.axis([-80,-55,34,48])
plt.show()




FN='binned_model.npz'
Z=np.load(FN) 
xb=Z['xb']
yb=Z['yb']
ub_mean=Z['ub_mean']
ub_median=Z['ub_median']
ub_std=Z['ub_std']
ub_num=Z['ub_num']
vb_mean=Z['vb_mean']
vb_median=Z['vb_median']
vb_std=Z['vb_std']
vb_num=Z['vb_num']
Z.close()

#cmap = matplotlib.cm.jet
#cmap.set_bad('w',1.)
xxb,yyb = np.meshgrid(xb, yb)
cc=np.arange(-1.5,1.500001,0.05)
#cc=np.array([-1., -.75, -.5, -.25, -0.2, -.15, -.1, -0.05, 0., 0.05, .1, .15, .2, .25, .5, .75, 1.])


plt.figure()
ub = np.ma.array(ub_mean, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_mean, mask=np.isnan(vb_mean))
Q=plt.quiver(xxb,yyb,ub.T,vb.T,scale=5.)
qk=plt.quiverkey(Q,0.8,0.1,0.5, r'$50cm/s$', fontproperties={'weight': 'bold'})

plt.title(FN[:-4]+', mean')

#plt.plot(coast_lon,coast_lat,'b.')
plt.plot(CL['lon'],CL['lat'])

plt.axis([-80,-55,34,48])
plt.show()

plt.figure()
ub = np.ma.array(ub_std, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_std, mask=np.isnan(vb_mean))
Q=plt.quiver(xxb,yyb,ub.T,vb.T,scale=5.)
qk=plt.quiverkey(Q,0.8,0.1,0.5, r'$50cm/s$', fontproperties={'weight': 'bold'})

plt.title(FN[:-4]+', std')

#plt.plot(coast_lon,coast_lat,'b.')
plt.plot(CL['lon'],CL['lat'])
plt.axis([-80,-55,34,48])
plt.show()

