# getPTFSNcoords
you will need: 

1. a PTF finding chart reporting the coordinates of reference stars and SN-star offsets

2. an SDSS or otherwise high (decent) resolution image of the field in fits format

3. python, ds9 and sextractor installed

instructions:
1. run [sextractor](http://www.astromatic.net/software/sextractor) on a fits image which includes the SN site and the reference stars marked in the PTF finding chart
`sex frame-r-003103-6-0122.fits `
the default.sex included in this repo has good parameters for this purpose which usually pick up the host galaxy nucleus and the comparison stars as isolated sources. it also has a default output file name: PTFSNfinder.cat

2. turn the output catalog file (PTFSNfinder.cat) into a [ds9](http://ds9.si.edu/site/Home.html) region file
`python sexcat2ds9reg.py  PTFSNfinder.cat`
this creates a region file PTFSNfinder.cat.reg  
3. open the SDSS image with ds9 loading the region file and identify the stars in the PTF finder's chart
`$ds9 SDSS_SNfield.fits -regions load PTFSNfinder.cat.reg`
4. click on the galaxy nucleus and reference stars regions to extract the coordinates of the circle centered on each reference star and on the host galaxy nucleus. with the default.sex file in this repo the coordinates will be outputted in deg in scientific notation: for example the galaxy coordinates may be something like 1.7599781135e+02 5.5687552292e+01 (RA in deg, Dec in deg)
5. for each reference star in the PTF finders chart pass the coordinates of the galaxy nucleus and of the star, as reported by sextractor, and the separation SN-star (E->W positive, N->S positive in arcsec) as reported buy the PTF finding chart to sky_separation.py

you can call the code as

`python sky_separation.py`

and pass it arguments in pairs responding to code prompts: 

`python sky_separation.py`
make sure you inputted coords in degrees and offsets in arcsecs

>Galaxy coords from SDSS fits: (ra dec in degrees) 1.7601249246e+02 5.5689677613e+01
>Star coords from SDSS fits: (ra dec in degrees) 1.7600449712e+02 5.5620345751e+01
>SN star separation from PTF find-chart: 
> SN->star W positive, S positive (ra dec in arcsec) 16.54 254.51

which returns:

>Gal-star separation (arcsec) 250.122396052 PA 3.20662rad
>Gal-star RA Dec offset (arcsec) 16.2243800281 249.5947032
>SN-Gal offsets: 0.315619971923 4.9152968

or pass the arguments at once (or even only the first pair - Galaxy coords - or first and second - Galaxy coords and star coords and wait for the following prompts)

`python sky_separation.py 1.7601249246e+02 5.5689677613e+01  1.7600449712e+02 5.5620345751e+01 16.54 254.51`
>assuming you passed Gal coords in deg, star coord in deg from FITS, star coord in deg from FITS, SN-star separation from PTF >in arcsec

>SN star separation  [16.54, 254.51]
>Gal-star separation (arcsec) 250.122396052 PA 3.20662rad
>Gal-star RA Dec offset (arcsec) 16.2243800281 249.5947032
>SN-Gal offsets: 0.315619971923 4.9152968


reported is the SN-Gal offset in arcsec
