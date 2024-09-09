import numpy as np

def secansh(x,x_0,s):
    """Funktion: secansh
    Aufruf: h = secansh(x,x_0,s)
    Berechnet fuer den Vektor x die Werte der normierten Secans Hyperbolicus
    Funktion mit dem Maximum bei x_0 und mit der Halbwertsbreite s
    Input:  Vektor x, Skalar x_0, Skalar s
    Output: Vektor h(x)"""
    return 1 / (np.pi * s * np.cosh(-(x - x_0) / s))
