class Planet:
    def __init__(self, name, mass, diameter, orbital_period_around_sun, distance_from_sun):
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.orbital_period_around_sun = orbital_period_around_sun
        self.distance_from_sun = distance_from_sun

    def calc_avg_density(self):
        volume = (4/3) * 3.14159265359 * ((self.diameter/2)
                                          ** 3)  # assuming planets are spherical
        density = self.mass / volume
        return density


# Planeten erstellen
earth = Planet("Erde", 5.972e24, 12742, 365.24, 149.6)
mercury = Planet("Merkur", 3.285e23, 4880, 87.97, 57.9)
venus = Planet("Venus", 4.867e24, 12104, 224.7, 108.2)
mars = Planet("Mars", 6.39e23, 6779, 686.98, 227.9)
jupiter = Planet("Jupiter", 1.898e27, 139822, 4332.59, 778.6)
saturn = Planet("Saturn", 5.683e26, 116464, 10759.22, 1433.5)
uranus = Planet("Uranus", 8.681e25, 50724, 30687.15, 2872.5)
neptune = Planet("Neptun", 1.024e26, 49244, 60190.03, 4495.1)

# Den Planeten mit der höchsten Dichte finden
planet_with_highest_density = max(
    earth, mercury, venus, mars, jupiter, saturn, uranus, neptune, key=lambda x: x.calc_avg_density())
print("Planet mit höchster Dichte:", planet_with_highest_density.name)

# Test: In Objekte einhängen und testen ob die Methoden funktionieren und die richtigen Wert zurückgeben
#$META title "Objektorientierte Programmierung in Python"
##$META studentSubmissionFiles ./planets_dict.py
##$META studentTemplates ./studentTemplates/planets_class.py
##$META studentTemplates ./studentTemplates/planets_dict.py

#$VARIABLETEST C1
#$PROPERTY entryPoint "planets_class.py"
##$PROPERTY setUpCode ["p10=Planet("Neueerde", 7.612e24, 15000, 745.1, 180.2)"]
#$PROPERTY setUpCode ["p10=Planet('Neueerde', 7.612e24, 15000, 745.1, 180.2)"]
#$TESTVAR p10.calc_avg_density()
#$TESTVAR p10.name
#$TESTVAR p10.mass
#$TESTVAR p10.diameter
#$TESTVAR p10.orbital_period_around_sun
#$TESTVAR p10.distance_from_sun


#$VARIABLETEST C2
#$PROPERTY entryPoint "planets_class.py"
#$TESTVAR earth
#$TESTVAR earth.calc_avg_density()
#$TESTVAR earth.name
#$TESTVAR earth.mass
#$TESTVAR earth.diameter
#$TESTVAR earth.orbital_period_around_sun
#$TESTVAR earth.distance_from_sun


#$VARIABLETEST dict_test
#$PROPERTY entryPoint "planets_dict.py"
#$TESTVAR planets
