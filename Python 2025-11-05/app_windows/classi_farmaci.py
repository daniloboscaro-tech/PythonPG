class farmaco:
    def __init__(self, peso, eta, dose):
        self.peso = peso
        self.eta = eta
        self.dose = dose

    def calc_Youg(self):
        return round((self.eta / (self.eta + 12)) * self.dose)

    def calc_Clark(self):
        return round((self.peso / 70) * self.dose)

