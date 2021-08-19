import random
from Verificador_Juego import *

class Computadora(Verificador_Juego):     
    def __init__(self,mano):
        self.mano = mano

    def mostrar_cartas(self):
        return self.mano           
    
    """ acepta_envido recibe cuantos puntos de envido tiene la IA,  recibe lo que canto la PERSONA, si hubiere cantado algo, y devuelve un canto de la IA o un "quiero - no quiero" """
    def acepta_envido(self, envido_ia, eleccion_persona): 

        retruco = random.randrange(3)   # Se puede hacer que mienta mas o menos con esta variable

        if eleccion_persona == 0:   #SI LA PERSONA CANTA ENVIDO

            if envido_ia >= 20 and envido_ia < 25:

                print("La computadora quiere el Envido")

                # Si hay azar
                if retruco == 2: return self.retruca_envido(eleccion_persona)

                return 1000 # Es un Quiero sin retrucar

            # Si el envido de la IA es mayor a 24 retruca
            elif envido_ia > 24: return self.retruca_envido(eleccion_persona)

            # Si el envido de la IA es menor a 20 puede mentir o no querer
            elif envido_ia < 20:

                if random.randrange(4) == 3 and envido_ia > 4:  # Hacemos mentir a la IA
                    # azar
                    if retruco == 2: return self.retruca_envido(eleccion_persona)

                else: return None # Devuelve un "No Quiero"

        elif eleccion_persona == 1:  # Si la persona canto Real Envido

            if envido_ia >= 25 and envido_ia < 29:

                print("La computadora quiere el Real Envido")

                # Si hay azar y si la persona elije Real Envido
                if retruco == 2: return self.retruca_envido(eleccion_persona)

                return 1000 # Para Definir Ganador

            elif envido_ia >= 29: return self.retruca_envido(eleccion_persona)
               
        elif eleccion_persona == 2: #Si la persona canto Falta Envido

            if envido_ia >= 29:

                print("La computadora quiere el Falta Envido")

                return True # Para Definir Ganador

            else: return None

        # Si la pesona Juega sin Cantar       
        elif eleccion_persona == 3: return 2000 
        # La Persona se arrepiente y no el 2do menú no quiere cantar

    """ canta_envido recibe cuantos puntos de envido tiene la IA y devuelve que canta, si quisiere cantar algo, o nada si no quisiere cantar """ 
    def canta_envido(self,envido_ia):

        if envido_ia >= 20 and envido_ia < 25:

            print("La computadora canta Envido")

            return 0

        elif envido_ia < 20:

            if random.randrange(4) == 3 and envido_ia > 4:  # Hacemos mentir a la IA

                print("Envidoo")
                return 0

            else: return None # Unica posiblididad que no quiera 

        elif envido_ia >= 25 and  envido_ia < 29:

            print("La computadora canta Real Envido")
            return 1

        elif envido_ia >= 29: # Si la IA tiene mas de 29 canta la Falta

            print("La computadora canta Falta Envido")
            return 2

    """ retruca_envido recibe lo que le canto la PERSONA y devuelve el retruque. (Este metodo es llamado solamente desde el método - acepta_envido - ) """
    def retruca_envido(self, eleccion_persona):

        if eleccion_persona == 0:

            print("Computadora: Real Envido")
            return 1

        elif eleccion_persona == 1:

            print("Computadora: Falta Envido")
            return 2

    def juega(self,en_juego,carta_persona, mano_persona,ganador_primera_mano):
    
        carta_ia = self.juega_truco(carta_persona)
        valor_carta_ia = self.verificar_truco(carta_ia)

        if carta_persona != None: valor_carta_persona = self.verificar_truco(carta_persona)

        else:

            canto_ia = en_juego
            return canto_ia, carta_ia
            
        if mano_persona != True or (mano_persona and ganador_primera_mano == None): #Si es la primera mano puede cantar aunque la persona no haya cantado

            if valor_carta_ia < valor_carta_persona: canto_ia = self.canta_truco(en_juego)

            elif valor_carta_ia > valor_carta_persona and ganador_primera_mano == "Computadora": canto_ia = self.canta_truco(en_juego)

            else: canto_ia = en_juego

        else: canto_ia = en_juego

        return canto_ia,carta_ia

    def aceptar_juego(self, canto_persona):

        valor_carta_total = 0

        for item in self.mano:  
            valor_carta = self.verificar_truco(item)
            valor_carta_total += valor_carta 

        if canto_persona == 1:

            if valor_carta_total <= 32:
                print("Computadora dice: Quiero")
                return True
            else:
                print("Computadora dice: No Quiero")
                return False
        elif canto_persona == 2:

            if valor_carta_total <= 28:
                print("Computadora dice: Quiero")
                return True
            else:
                print("Computadora dice: No Quiero")
                return False

        elif canto_persona == 3:
            
            if valor_carta_total <= 20:
                print("Computadora dice: Quiero")
                return True
            else:
                print("Computadora dice: No Quiero")
                return False

    def juega_truco(self, carta_persona):

        valor_mejor_carta_momentanea = 100
        peor_carta_momentanea = 0

        if carta_persona != None: valor_carta_persona = self.verificar_truco(carta_persona)
        else: valor_carta_persona = None

        for carta in self.mano:
            valor_carta_ia = self.verificar_truco(carta)

            if valor_carta_ia < valor_mejor_carta_momentanea: valor_mejor_carta_momentanea,mejor_carta_definitiva = valor_carta_ia, carta

        if valor_carta_persona == None: #Si le toca jugar a ia primero juega la mejor carta
            self.mano.remove(mejor_carta_definitiva)
            return mejor_carta_definitiva
        elif valor_mejor_carta_momentanea < valor_carta_persona: #Si la mejor carta ia es mejor que de la persona
            self.mano.remove(mejor_carta_definitiva)
            return mejor_carta_definitiva
        else:
            for carta in self.mano:

                valor_carta_ia = self.verificar_truco(carta)
                if valor_carta_ia > peor_carta_momentanea: peor_carta_momentanea, peor_carta_definitiva = valor_carta_ia, carta
          
            if peor_carta_momentanea >= valor_carta_persona:
                self.mano.remove(peor_carta_definitiva)
                return peor_carta_definitiva

    def canta_truco(self, en_juego):

        #menu_opciones = ["Truco","Quiero Retruco", "Quiero Vale Cuatro", ]
        computadora_canta = 223
        if en_juego == 0:
            computadora_canta = 1
            print("Computadora dice:Truco!")
        elif en_juego == 1:  
            computadora_canta = 2
            print("Computadora dice:Quiero Retruco!")
        elif en_juego == 2:
            computadora_canta = 3
            print("Computadora dice: Quiero Vale Cuatro!")
        return computadora_canta