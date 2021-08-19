import random

class Mazo:

  def __init__(self):

    self.mazo = []
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ["Espada", "Basto", "Oro", "Copa"]

    for valor in valores:
      for palo in palos:
        tupla = palo, valor
        self.mazo.append(tupla)

  def mezclar_mazo(self):
    self.mazo_copia = self.mazo[:]
    random.shuffle(self.mazo_copia)

  def repartir_cartas(self):

    self.mano = []

    for i in range(3):
      
      self.mano.append(self.mazo_copia[i])
      self.mazo_copia.remove(self.mazo_copia[i])

    return self.mano