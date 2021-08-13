from Tablero import *

class Juego(Tablero):
    def __init__(self):
        self.tablero = Tablero(0, 0)

    def mostrar_tablero(self):
        return self.tablero.mostrar_tablero()

    def puntos_computadora(self, puntos):
        self.tablero.puntos_computadora(puntos)

    def puntos_humano(self, puntos):
        self.tablero.puntos_humano(puntos)

    def envido_mano_persona(self, jugador_humano,jugador_ia, mano_humano):
 
        envido_ia = self.verificar_envido(jugador_ia.mostrar_cartas())
        envido_humano = self.verificar_envido(jugador_humano.mostrar_cartas())
        eleccion_persona = jugador_humano.canta_envido() 
        eleccion_computadora = jugador_ia.acepta_envido(envido_ia, eleccion_persona)

        if eleccion_computadora == None: # Si la computadora No Quiere
            print("Computadora: No Quiero")
            self.puntos_humano(1)

        elif eleccion_computadora == 1: # Si la computadora le retruca con un Real Envido
            acepta_persona = jugador_humano.acepta_envido(eleccion_computadora)
            if acepta_persona == None:
                print("Persona: No Quiero")
                self.puntos_computadora(2)
            elif acepta_persona == True or acepta_persona == 1000: #1000 DEFINE GANADOR (es un Quiero)
                puntos_en_juego = 3
                self.verificar_ganador_envido(envido_humano,envido_ia,mano_humano,puntos_en_juego)
            elif acepta_persona == 2:   #Falta Envido canta persona
                eleccion_computadora = jugador_ia.acepta_envido(envido_ia, acepta_persona)
                if eleccion_computadora == True:
                    puntos_en_juego = 4
                    self.verificar_ganador_envido(envido_humano,envido_ia,mano_humano,puntos_en_juego)
                else:
                    self.puntos_humano(3)
                    print("Computadora: No Quiero")
        elif eleccion_computadora == 2: # Si la computadora le retruca con Falta Envido
            acepta_persona = jugador_humano.acepta_envido(eleccion_computadora)
            if acepta_persona == 1000:
                puntos_en_juego = 4
                self.verificar_ganador_envido(envido_humano,envido_ia,mano_humano,puntos_en_juego)
            else:
                self.puntos_computadora(3)
                print("La persona No quiere")
        elif eleccion_computadora == 1000:
            puntos_en_juego = 2
            self.verificar_ganador_envido(envido_humano,envido_ia,mano_humano,puntos_en_juego)
        elif eleccion_computadora == 2000:
            pass
            #juega_persona = 3 # Para que entre en "Si la Persona juega sin cantar "
        else: # La IA juega Sin Retrucar
            puntos_en_juego = 2
            self.verificar_ganador_envido(envido_humano,envido_ia,mano_humano,puntos_en_juego)

    def envido_mano_computadora(self, jugador_humano,jugador_ia, mano_humano):
        menu_opciones = ["Envido", "Truco", "Flor","Jugar sin cantar","Mazo"]
        envido_ia = self.verificar_envido(jugador_ia.mostrar_cartas())
        envido_humano = self.verificar_envido(jugador_humano.mostrar_cartas())
        ia_canta = jugador_ia.canta_envido(envido_ia)

        if ia_canta != None: # La computadora canta algo
            acepta_persona = jugador_humano.acepta_envido(ia_canta)
            if acepta_persona == 1000: # Persona acepta sin retrucar
                puntos_en_juego = 2
                self.verificar_ganador_envido(envido_humano,envido_ia,mano_humano,puntos_en_juego)
            elif acepta_persona == 1: # Persona retruca con Real Envido
                acepta_ia = jugador_ia.acepta_envido(envido_ia, acepta_persona)
                if acepta_ia == 2: # IA vuelve a retrucar con Falta Envido
                    acepta_persona = jugador_humano.acepta_envido(acepta_ia)
                    if acepta_persona == 1000:    
                        puntos_en_juego = 4
                        self.verificar_ganador_envido(envido_humano,envido_ia,mano_humano,puntos_en_juego)
                    else: # Recibe None
                        self.puntos_computadora(3)
                        print("Persona: No Quiero")
                elif acepta_ia == None:
                    self.puntos_humano(2)
                    print("Computadora: No Quiero")
            elif acepta_persona == 2: # Persona retruca con Falta Envido
                ia_acepta = jugador_ia.acepta_envido(envido_ia, acepta_persona)
                if ia_acepta == 1000:
                    puntos_en_juego = 4
                    self.verificar_ganador_envido(envido_humano,envido_ia,mano_humano, puntos_en_juego)
                else: # Recibe None
                    self.puntos_humano(3)
                    print("Computadora: No Quiero")
            else: # Recibe None
                self.puntos_computadora(1)
                print("Persona: No Quiero")
        else:
            print("La computadora no canta. ")
            persona_canta = int(input(f"Elija: {menu_opciones}")) - 1  # La IA paso del envido y la Persona puede cantar o no
            if persona_canta == 0:
                #eleccion_persona = jugador_humano.canta_envido()
                ia_acepta = jugador_ia.acepta_envido(envido_ia, persona_canta)
                if ia_acepta == None:
                    self.puntos_humano(1)
                    print("Computadora: No Quiero")
                else:
                    print("Computadora: Quiero")
                    puntos_en_juego = 2
                    self.verificar_ganador_envido(envido_humano,envido_ia,mano_humano,puntos_en_juego)    

    def verificar_ganador_envido(self, envido_humano, envido_ia, mano_humano,puntos_en_juego):
        
        print(f"La computadora tiene {envido_ia}\nVos tenés: {envido_humano}")
        if envido_humano > envido_ia:
            print(f"Vos ganas! {puntos_en_juego} puntos")
            return self.puntos_humano(puntos_en_juego)
        elif envido_humano < envido_ia:
            print(f"La compu gana! {puntos_en_juego} puntos")
            return self.puntos_computadora(puntos_en_juego)
        else:
          print(f"Empate, se lleva {puntos_en_juego} puntos la mano.")
          if mano_humano == True:
                return self.puntos_humano(puntos_en_juego)
          else:
                return self.puntos_computadora(puntos_en_juego)

    def verificar_envido(self,mano):

        envido = 0
        dic_palos = {'Oro': [], 'Basto': [], 'Copa': [], 'Espada': []}
        lista_aux = []
        for palo, valor in mano:
            for palo_dic in dic_palos:
                if palo == palo_dic:
                    if valor >= 10:
                        dic_palos[palo_dic].append(0)
                    else:
                        dic_palos[palo_dic].append(valor)

        for item in dic_palos.values():
            if len(item) == 2:
                envido = sum(item) + 20
            elif len(item) == 3:
                item.sort()
                envido = item[2] + item[1] + 20
            else:
                for element in item:
                    lista_aux.append(element)
                    lista_aux.sort()
        if envido == 0:
            envido = lista_aux[len(lista_aux)-1]
        return envido

    def verificar_truco(self, carta):

        if carta[1] == 1:
            if carta[0] == 'Espada': return 1
            elif carta[0] == 'Basto': return 2
            else: return 7
        elif carta[1] == 2: return 6
        elif carta[1] == 3: return 5
        elif carta[1] == 4: return 14
        elif carta[1] == 5: return 13
        elif carta[1] == 6: return 12
        elif carta[1] == 7:
            if carta[0] == 'Espada': return 3
            elif carta[0] == 'Oro': return 4
            else: return 11
        elif carta[1] == 10: return 10
        elif carta[1] == 11: return 9
        else: return 8

    #Devuelve ganador
    def primer_mano(self, carta_humano, carta_ia, mano_humano):#mano_humano recibe quien es mano
        
        carta_persona = self.verificar_truco(carta_humano)
        carta_computadora = self.verificar_truco(carta_ia)

        if carta_persona < carta_computadora: return "Persona"
        elif carta_persona > carta_computadora: return "Computadora"
        else:
            if mano_humano == True: return "Persona"
            else: return "Computadora"
            
    #Devuelve ganador
    def segunda_mano(self, carta_humano, carta_ia, ganadas_persona):#ganadas_persona para definir quien gano primera mano y asi saber quien gana en caso de empate en 2da mano
        
        carta_persona = self.verificar_truco(carta_humano)
        carta_computadora = self.verificar_truco(carta_ia)
        
        if carta_persona < carta_computadora: return "Persona"
        elif carta_persona > carta_computadora: return "Computadora"
        else:
            if ganadas_persona == 1: return "Persona"
            else: return "Computadora"


    #Devuelve ganador
    def tercera_mano(self, carta_humano, carta_ia, ganador_primer_mano):#ganador_primer_mano por si hay empate
        
        carta_persona = self.verificar_truco(carta_humano)
        carta_computadora = self.verificar_truco(carta_ia)
        
        if carta_persona < carta_computadora: return "Persona"
        elif carta_persona > carta_computadora: return "Computadora"
        else:
            if ganador_primer_mano == "Persona": return "Persona"
            else: return "Computadora"