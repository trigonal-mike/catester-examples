# Berechnung des Datums des Ostersonntags mit der
# Gauss'schen Osterformel

import numpy as np

# if/else block only for automatic tesing
# student should write the code in the try block
# if __name__ == '__main__':
X = int(input("Jahr fuer die Berechnung des Osterfestes: "))
# else:
# X = 2024
#    print(f'Falsche Eingabe. Das Jahr {X} wird verwendet.')

# Gauss'sche Zyklenzahl
a = X % 19
b = X % 4
c = X % 7
k = X // 100
p = (8 * k + 13) // 25
q = k // 4
# Korr.: So- u. Mo-Gleichung
M = (15 + k - p - q) % 30
# Korr.: Sonnengleichung
N = (4 + k - q) % 7
# Mondentfernung
d = (19 * a + M) % 30
# Osterentfernung
e = (2 * b + 4 * c + 6 * d + N) % 7
Ostersonntag = 22 + d + e

if Ostersonntag <= 31:
    Monat = "Maerz"
else:
    Ostersonntag -= 31
    Monat = "April"

print(f"Der Ostersonntag ist im Jahr {X} am {Ostersonntag}. {Monat}")
