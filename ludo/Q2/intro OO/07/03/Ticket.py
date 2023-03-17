class Ticket:
    def __init__(self, numero, lignes: list[LigneTicket]):
        self.numero = numero
        self.lignes = lignes

    @property
    def total(self):
        total = 0

        for ligne in self.lignes:
            total += ligne.total
        return total     