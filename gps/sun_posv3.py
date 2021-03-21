from pyephem_sunpath.sunpath import sunpos
from datetime import datetime

thetime = datetime.now()
lat = 6.17980
lon = -75.58400
tz = -5

alt, azm = sunpos(thetime, lat, lon, tz, dst=False)
print("Altitud:", alt, ", Azimuth:", azm)
