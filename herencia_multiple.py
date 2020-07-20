class A():
    def hola(self):
        print("Hola heredado de la clase A")

    def adios(self):
        print("Adiós heredado de la clase A")

class B():
    def hola(self):
        print("Hola heredado de la clase B")

    def adios(self):
        print("Adiós heredado de la clase B")

class C(A,B):

    def hola(self):
        print("Hola de la propia clase C")
        super().hola()

    def adios(self):
        B.adios(self)

c = C()
c.hola()
c.adios()  # No podemos heredar de B aunque queramos