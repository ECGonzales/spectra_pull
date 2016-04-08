from astrodbkit import astrodb  # do every session, loads packages- database
import matplotlib.pyplot as plt  # loads package to plot

db = astrodb.get_db('./BDNYC.db')  #loading the database
t = db.search("2322-6151","sources")  #search for source via shortname(RADEC), to get id number
spec = 'select * from spectra where id=518' #SQL query for the spectra
t1 = db.query(spec, fmt='dict') #execute sql query
w = t1[0]['wavelength'] #get the flux and wavelength to plot
f = t1[0] ['flux']
plt.plot(w,f)
plt.ylabel("Flux")
plt.xlabel('Wavelength in $\mu m$')
plt.title("Spectra 2322-6151")
#plt.axes([0,6,0.600,0.955])
plt.savefig('spectra2322-6151.png')

# db.inventory lets you see all the spectra for the object to plot put plot=true in the db.inventory(ID#, plot=true)