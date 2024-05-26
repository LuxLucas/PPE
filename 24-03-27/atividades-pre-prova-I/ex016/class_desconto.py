class Desconto:
    def __init__(self):
        self.DescontoSalarialImpostoDeRenda = 0.11
        self.DescontoSalarialINSS = 0.08 
        self.DescontoSalarialSindicato = 0.05

    def calcular_desconto_total(self):
        DescontoTotal = []
        DescontoTotal.append(self.DescontoSalarialImpostoDeRenda)
        DescontoTotal.append(self.DescontoSalarialINSS)
        DescontoTotal.append(self.DescontoSalarialSindicato)
        return sum(DescontoTotal)
