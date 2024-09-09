class Planet:
    def __init__(
        self, name, mass, diameter, orbital_period_around_sun, distance_from_sun
    ):
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.orbital_period_around_sun = orbital_period_around_sun
        self.distance_from_sun = distance_from_sun

    def calc_avg_density(self):
        volume = (
            (4 / 3) * 3.14159265359 * ((self.diameter / 2) ** 3)
        )  # assuming planets are spherical
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
    earth,
    mercury,
    venus,
    mars,
    jupiter,
    saturn,
    uranus,
    neptune,
    key=lambda x: x.calc_avg_density(),
)
print("Planet mit höchster Dichte:", planet_with_highest_density.name)

# Test: In Objekte einhängen und testen ob die Methoden funktionieren und die richtigen Wert zurückgeben
