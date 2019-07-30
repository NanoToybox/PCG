import math
import numpy

Gamma = 0.80
IntensityMax = 255

# Taken from Earl F. Glynn's web page:
# http://www.efg2.com/Lab/ScienceAndEngineering/Spectra.htm" Spectra Lab Report

def waveLengthToRGB(Wavelength):
    factor=0
    Red=0
    Green=0
    Blue=0

    if((Wavelength >= 380) and (Wavelength<440)):
        Red = -(Wavelength - 440) / (440 - 380)
        Green = 0.0
        Blue = 1.0
    elif((Wavelength >= 440) and (Wavelength<490)):
        Red = 0.0
        Green = (Wavelength - 440) / (490 - 440)
        Blue = 1.0
    elif((Wavelength >= 490) and (Wavelength<510)):
        Red = 0.0
        Green = 1.0
        Blue = -(Wavelength - 510) / (510 - 490)
    elif((Wavelength >= 510) and (Wavelength<580)):
        Red = (Wavelength - 510) / (580 - 510)
        Green = 1.0
        Blue = 0.0
    elif((Wavelength >= 580) and (Wavelength<645)):
        Red = 1.0
        Green = -(Wavelength - 645) / (645 - 580)
        Blue = 0.0
    elif((Wavelength >= 645) and (Wavelength<781)):
        Red = 1.0
        Green = 0.0
        Blue = 0.0
    else:
        Red = 0.0
        Green = 0.0
        Blue = 0.0

    #Let the intensity fall off near the vision limits

    if((Wavelength >= 380) and (Wavelength<420)):
        factor = 0.3 + 0.7*(Wavelength - 380) / (420 - 380)
    elif((Wavelength >= 420) and (Wavelength<701)):
        factor = 1.0
    elif((Wavelength >= 701) and (Wavelength<781)):
        factor = 0.3 + 0.7*(780 - Wavelength) / (780 - 700)
    else:
        factor = 0.0

    rgb = [0,0,0,0]

    # Don't want 0^x = 1 for x <> 0
    rgb[0] = 0 if Red==0.0 else round(IntensityMax * math.pow(Red * factor, Gamma))
    rgb[1] = 0 if Green==0.0 else round(IntensityMax * math.pow(Green * factor, Gamma))
    rgb[2] = 0 if Blue==0.0 else round(IntensityMax * math.pow(Blue * factor, Gamma))
    rgb[3] = IntensityMax

    return rgb

def rgbToString(rgb):    #[0,255,255] to "#00FFFF"
    s = "#%0.2X" %rgb[0] + "%0.2X" %rgb[1] + "%0.2X" %rgb[2]
    return s
    
