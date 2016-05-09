##Written by FBB for Keck Run June 2015, with inputs from DF's code##
##
#the idea is that you may have different star coords if you measured a FITS
#or get them from a finder's chart 
#(the PTF finder charts for example have reliable offsets 
# so you should input the star coords twice
# but no reliable coordinates in absolute sense
# --and have coords in seg only for the stars, 
# hence the ability to input them as segs--) 
##################################
##input: 
##################################
##you can call the code without inputs and answer the code's request for coords:# Gal coords in deg (RA Dec),
# reference  star  coords in deg (RA Dec),
# SN-star offset from a finder chart in arcsec (E-W,N-S)
#
# OR 
#


import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
from myastrotools import offsets, raseg2deg,decseg2deg
import sys


if len(sys.argv)==7:
    print "assuming you passed Gal coords in deg, star coord in deg from FITS, star coord in deg from FITS, SN-star separation from PTF in arcsec"
    

    print "" 
    #from fits file and sextractor
    ra_g,dec_g=float(sys.argv[1]),float(sys.argv[2])
    ra1,dec1=float(sys.argv[3]),float(sys.argv[4])
    
    
    #from PTF charts
    '''
    if ':' in sys.argv[7]:
        starcra,starcdec=raseg2deg(sys.argv[7]),decseg2deg(sys.argv[8])
    else:
        starcra,starcdec=float(sys.argv[7]),float(sys.argv[8])
    '''

    SNstarsep=[0,0]
    SNstarsep[0],SNstarsep[1]=(float(sys.argv[5])),(float(sys.argv[6]))    

    print "SN star separation ", SNstarsep

else:

    print "make sure you inputted coords in degrees and offsets in arcsecs"
    print ""
    galcoords=raw_input("Galaxy coords from SDSS fits: (ra dec in degrees) ")
    starcoords= raw_input("Star coords from SDSS fits: (ra dec in degrees) ")
    SNstar=raw_input("SN star separation from PTF find-chart: \n SN->star W positive, S positive (ra dec in arcsec) ")

    print "" 
    #from fits file and sextractor
    ra_g,dec_g=float(galcoords.split()[0]),float(galcoords.split()[1])
    ra1,dec1=float(starcoords.split()[0]),float(starcoords.split()[1])
    
    #from PTF charts
    SNstarsep=[0,0]
    SNstarsep[0],SNstarsep[1]=(float(SNstar.split()[0])),(float(SNstar.split()[1]))





c1 = SkyCoord(ra_g*u.degree, dec_g*u.degree, frame='fk5')
c2 = SkyCoord(ra1*u.degree, dec1*u.degree, frame='fk5')
pa=c1.position_angle(c2)
sep = c1.separation(c2)

print "Gal-star separation (arcsec)",sep.arcsec, "PA",pa
off=offsets([[ ra_g,dec_g ]],[[ ra1,dec1 ]])
print "Gal-star RA Dec offset (arcsec)", off[0]*3600.*np.abs(np.cos(dec_g*np.pi/180.)),off[1]*3600.

Galaxy= ra_g,dec_g
star=ra1,dec1



#i am leaving in simplifications that can be dropped for clarity

GaldRA=(SNstarsep[0]/3600.0/np.cos(Galaxy[1]/180.*np.pi)+star[0]-Galaxy[0])*np.cos(Galaxy[1]/180.*np.pi)*3600.

Galddec=(SNstarsep[1]/3600.0+star[1]-Galaxy[1])*3600

print "SN-Gal offsets:", GaldRA, Galddec

