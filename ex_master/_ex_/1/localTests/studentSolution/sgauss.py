import numpy as np

def sgauss(x,x_0,s):
  """Funktion: sgauss
  Aufruf: g = sgauss(x,x_0,s)
  Berechnet fuer den Vektor x die Werte der Gaussfunktion mit dem Maximum
  bei x_0 und mit der Halbwertsbreite s
  Input:  Vektor x, Skalar x_0, Skalar s
  Output: Vektor g(x)"""
  return x**2 + x_0**2 + s**2
