class MixinInstancia:
    def instancia(self):
        print(hex(id(self)))


class MixinClase:
    def clase(self):
        print(type(self).__name__)


class A(MixinInstancia, MixinClase):
    pass


class B(MixinInstancia, MixinClase):
    pass


a = A()
a.instancia()
a.clase()

b = B()
b.instancia()
b.clase()