from Verificador_Juego import *

class Humano(Verificador_Juego):

    def __init__(self,mano):
        self.mano = mano
        self.puntos = 0
    
    def mostrar_cartas(self):
        return self.mano

    """ acepta_envido recibe lo que canto la IA, si hubiere cantado algo, y devuelve un canto de la persona o un "quiero - no quiero" """
    def acepta_envido(self, juego_ia):
        
        acepta = int(input("Acepta? 1 si, 2 no"))

        if acepta == 1: #Si la persona acepta lo que la IA le canta

            # Si la IA le canto Falta Envido
            if juego_ia == 2:  return 1000 # Devuelve un QUIERO sin cantar

            else:   # Si la IA quiere retrucarle el envido

                print("Persona: Quiero!")
                retruca_persona = self.retruca_envido(juego_ia)

                # Persona retruca con Real Envido
                if retruca_persona == 1: return 1 
                # Persona retruca con Falta Envido
                elif retruca_persona == 2: return 2 
                # Persona quiere sin cantar
                elif retruca_persona == 3: return 1000 # Es un QUIERO sin cantar

        else: return None # Devuelve un "No Quiero"

    def canta_envido(self):

        menu_opciones = ["Envido", "Real Envido", "Falta Envido", "Jugar Sin Cantar"]
        eleccion_persona = int(input(f"Elija: {menu_opciones}")) - 1
        print(f"Persona: {menu_opciones[eleccion_persona]}")
        return eleccion_persona

    """ retruca_envido recibe que le retruco la IA y devuelve el retruque que quiere la persona. (Este método es llamado solamente desde el método -acepta_envido- ) """
    def retruca_envido(self, retruco_ia):

        if retruco_ia == 0: # Si la IA le canto Envido

            menu_opciones = ["Real Envido", "Falta Envido", "Jugar Sin Cantar"]
            eleccion_persona = int(input(f"Elija: {menu_opciones}")) #CON LA OPCION INGRESADA SINCRONIZA CON EL MENU COMPLETO
            print(f"Persona: {menu_opciones[eleccion_persona - 1]}")

            return eleccion_persona

        if retruco_ia == 1: # Si la IA le canto REAL ENVIDO
            menu_opciones = ["Falta Envido", "Jugar Sin Cantar"]
            eleccion_persona = int(input(f"Elija: {menu_opciones}"))  
            print(f"Persona: {menu_opciones[eleccion_persona - 1]}")

            return eleccion_persona + 1 #CON LA OPCION INGRESADA SINCRONIZA CON EL MENU COMPLETO 

    def juega(self, en_juego,mano_persona):


        if mano_persona: canto_persona = self.canta_truco(en_juego)
        else: canto_persona = None

        carta_persona = self.juega_truco()

        return canto_persona,carta_persona

    def aceptar_juego(self):

        menu_opciones_truco = ["Quiero", "No Quiero"]
        acepta_persona = int(input(f"{menu_opciones_truco}"))

        if acepta_persona == 1: acepta_persona = True
        elif acepta_persona == 2: acepta_persona = None

        return acepta_persona

    def canta_truco(self, juego):

        menu_opciones_truco = ["Truco","Quiero Retruco", "Quiero Vale Cuatro", "Jugar sin cantar","Mazo" ]

        if juego == 0:

            menu_opciones_truco.remove("Quiero Retruco")
            menu_opciones_truco.remove("Quiero Vale Cuatro")
            persona_canta = int(input(f"{menu_opciones_truco}"))

            if persona_canta == 2: persona_canta = 0 # jugar sin cantar
            elif persona_canta == 3: persona_canta = None #no quiero 

        elif juego == 1:

            menu_opciones_truco.remove("Truco")
            menu_opciones_truco.remove( "Quiero Vale Cuatro")
            persona_canta = int(input(f"{menu_opciones_truco}"))
            
            if persona_canta == 1: persona_canta = 2 #truco
            elif persona_canta == 2: persona_canta = 0 #jugar sin cantar
            elif persona_canta == 3: persona_canta = None #no quiero

        elif juego == 2:

            menu_opciones_truco.remove("Truco")
            menu_opciones_truco.remove("Quiero Retruco")
            persona_canta = int(input(f"{menu_opciones_truco}"))

            if persona_canta == 1: persona_canta = 3
            elif persona_canta == 2: persona_canta = 0 #jugar sin cantar
            elif persona_canta == 3: persona_canta = None #no quiero

        elif juego == 3:

            menu_opciones_truco = ["Quiero", "No Quiero"]
            persona_canta = int(input(f"{menu_opciones_truco}")) - 1

            if persona_canta == 1: persona_canta = None

        return persona_canta

    def juega_truco(self):

        carta = int(input(f"Que carta desea jugar: {self.mano}")) - 1
        carta_persona = self.mano[carta]
        self.mano.remove(carta_persona)

        return carta_persona