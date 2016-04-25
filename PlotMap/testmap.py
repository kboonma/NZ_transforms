from mpl_toolkits.basemap import Basemap, shiftgrid, cm
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# # setup mercator map projection.
m = Basemap(llcrnrlon=155.,llcrnrlat=-50.,urcrnrlon=185.,urcrnrlat=-30.,\
             resolution='h',epsg=2113)

#m.drawcoastlines()
#m.drawcountries()
#m.fillcontinents()
# #m.drawmapboundary()
# #m.bluemarble()

m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True)

m.drawparallels(np.arange(-90,90,5),labels=[True,True,False,True],color='#262626')
m.drawmeridians(np.arange(-180,180,5),labels=[False,False,True,True], color='#262626')

m.drawmapscale(183, -50, 170., -40., 500, barstyle='fancy', units='km', \
	fontsize=9, yoffset=None, labelstyle='simple', fontcolor='w', fillcolor1='w',\
	 fillcolor2='k', ax=None, format='%d', zorder=None)

plt.tight_layout()
plt.show()




##################################################################
##### setup Lambert Conformal basemap.
# # set resolution=None to skip processing of boundary datasets.

# map = Basemap(width=10000000,height=12000000,projection='lcc',
#             resolution=None,lat_1=45.,lat_2=55,lat_0=-40,lon_0=173.)

# map.drawparallels(np.arange(-90,90,10),labels=[1,1,0,1])
# map.drawmeridians(np.arange(-180,180,10),labels=[1,1,0,1])
# map.etopo(scale=1)
# #map.bluemarble()
# #map.shadedrelief()
# plt.show()


