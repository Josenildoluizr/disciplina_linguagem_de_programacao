class time_de_futebol():
    def __init__ (self, nome, cor_uniforme, vitorias_seguidas):
        self.nome = nome
        self.cor_uniforme = cor_uniforme 
        self.vitorias_seguidas = vitorias_seguidas
    
    def jogar_agressivo(self):
        print("O {} esta jogando AGRESSIVAMENTE! ".format(self.nome))
    
    def jogar_defensivo(self):
        print("O {} esta jogando DEFENSIVAMENTE! ".format(self.nome))

    def vitorias(self):
        print("O numero de vitorias do {} é {}!".format(self.nome, self.vitorias_seguidas))
        if self.vitorias_seguidas >= 5:
            print("O {} está em uma boa fase!".format(self.nome))
        else:
            print("O {} ainda está tentando emplacar sua sequência de vitorias!".format(self.nome))


