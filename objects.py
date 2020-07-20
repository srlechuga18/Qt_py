class Galleta:

    def __init__(self, sabor="dulce", chocolate=False):
        self.sabor = sabor
        self.chocolate = chocolate

    def chocolatear(self):
        self.chocolate = True

    def __str__(self):
        resumen = "Soy una galletita " + self.sabor
        if self.chocolate:
            resumen += "con chocolate"
        return resumen  # debe devolver una cadena


galleta = Galleta()
print(galleta)

resumen_galleta = galleta.__str__()
print(resumen_galleta)

resumen_galleta = str(galleta)
print(resumen_galleta)

galleta_dulce = Galleta()
print(galleta_dulce.sabor)

galleta_salada = Galleta()
galleta_salada.sabor = "salada"
print(galleta_salada.sabor)

galleta_picante = Galleta()
galleta_picante.sabor = "picante"
print(galleta_picante.sabor)