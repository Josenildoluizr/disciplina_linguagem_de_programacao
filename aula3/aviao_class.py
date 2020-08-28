class aviao():
    def __init__ (self, cor, modelo, compania):
        self.cor = cor
        self.modelo = modelo
        self.compania = compania

    def decolar(self):
        print("O avião da compania {} está DECOLANDO!".format(self.compania))
    
    def pousar(self):
        print("O avião da compania {} está POUSANDO!".format(self.compania))
    
    def cor_aviao(self):
        print("A cor do avião é: {} ".format(self.cor))

    def modelo_aviao(self):
        print("O modelo desse avião é: {} ".format(self.modelo))


  