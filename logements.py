class Logement:
    # Constructor
    def __init__(self, nombre_parkings, surface_totale):
        self.nombre_parkings = nombre_parkings
        self.surface_totale = surface_totale
    # __add__ method 
    def __add__(self, surface_habitable, surface_jardin):
        return Logement(self.surface_totale + surface_habitable.surface_totale + surface_jardin.surface_totale)
    
    # function to calculate the surface of the garden = surface totale + all surface > 100
    def surface_jardin(self):
        if self.surface_totale > 100:
            return self.surface_totale - 100
        else:
            return 0
    

    # __str_ method
    def __str__(self):
        # comparaison of surfaces
        if self.surface_totale > 100:
            # then the logement has a garden and we need to add the surface of the garden
            return f"Surface totale: {self.surface_totale}, Nombre de parkings: {self.nombre_parkings}, Surface jardin: {self.surface_jardin()}"
        else:
            # then the logement has no garden
            return f"Surface totale: {self.surface_totale}, Nombre de parkings: {self.nombre_parkings}"

# Exemple d'instanciation
logement1 = Logement(2, 120)
logement2 = Logement(1, 80)
logement3 = Logement(1, 50)
logement4 = Logement(1, 150)
logement5 = Logement(1, 200)

