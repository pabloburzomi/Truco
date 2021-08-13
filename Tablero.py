class Tablero:
  def __init__(self, punto_computadora, punto_humano):
    self.punto_computadora = punto_computadora
    self.punto_humano = punto_humano

  def puntos_computadora(self, puntos):
    self.punto_computadora += puntos
    return self.punto_computadora

  def puntos_humano(self, puntos):
    self.punto_humano += puntos
    return self.punto_humano

  def mostrar_tablero(self):
    return self.punto_humano, self.punto_computadora