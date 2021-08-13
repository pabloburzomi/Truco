import random
import time

from Juego import *
from Tablero import *
from Mazo import *
from Humano import *
from Computadora import *

def main():
    

    ptos_para_ganar = 10
    mazo = Mazo()
    counter = random.randrange(2)

    # Para ver quien arranca la partida
    if counter % 2 == 0: print("Saliste sorteado para empezar la partida\n")
    else: print("Salio sorteada la computadora para empezar la partida\n")
   
    menu_opciones = ["Envido", "Truco", "Flor","Jugar sin cantar","Mazo"]
    #menu_opciones_truco = ["Truco", "Jugar sin cantar", "Mazo"]

    while juego.mostrar_tablero()[0] < ptos_para_ganar and juego.mostrar_tablero()[1] < ptos_para_ganar:

        mazo.mezclar_mazo()
        cartas_humano = mazo.repartir_cartas()
        cartas_ia = mazo.repartir_cartas()
        print("Repartiendo cartas...")
        time.sleep(2)
        #Los Jugadores
        jugador_humano = Humano(cartas_humano)
        jugador_ia = Computadora(cartas_ia)
        print(f"Tus cartas son {jugador_humano.mostrar_cartas()} - Las cartas de la computadora son {cartas_ia}")
        print(f"El juego queda: {juego.mostrar_tablero()}")
        mano_humano = False

        if counter % 2 == 0:   # ES MANO LA PERSONA
            print("Es mano la persona")
            mano_humano = True
            juega_persona = int(input(f"Elija: {menu_opciones}")) - 1

            if juega_persona == 0:  # SI LA PERSONA JUEGA CON EL MENU DE ENVIDO
                juego.envido_mano_persona(jugador_humano,jugador_ia, mano_humano)

            manos = 0
            mano_del_juego_persona = True
            ganador_mano = None
            turno_cantar_persona = True
            en_juego = 0
            ganador_primera_mano = None
            ganadas_persona = 0
            ganadas_computadora = 0

            while manos < 3:

                if ganadas_persona < 2 and ganadas_computadora < 2:
                    
                    print(f"****************  Mano {manos + 1} *********************")

                    if turno_cantar_persona == True:
                        print("Te toca cantar...")
                    else:
                        print("Le toca cantar a la computadora")

                    if ganador_mano == "Persona" or ganador_mano == None:
                        canto_persona = None
                        carta_persona = None
                        print("Le toca jugar a la persona")

                        juego_persona = jugador_humano.juega(en_juego,turno_cantar_persona)
                        canto_persona = juego_persona[0]
                        carta_persona = juego_persona[1]

                        if canto_persona != en_juego and canto_persona != None:
                            acepta_ia = jugador_ia.aceptar_juego(canto_persona)                    
                            if acepta_ia == True:
                                en_juego = canto_persona
                                turno_cantar_persona = False
                            else:
                                ganadas_persona += 2
                        
                        print(f"Persona juega: {carta_persona}")
                        
                        juego_ia = jugador_ia.juega(en_juego,carta_persona, turno_cantar_persona,ganador_primera_mano)
                        canto_ia = juego_ia[0]
                        carta_ia = juego_ia[1]
                        if (canto_ia != en_juego and canto_ia != None) or (canto_persona == 0 and manos == 0):
                            acepta_persona = jugador_humano.aceptar_juego()
                            if acepta_persona == True:
                                en_juego = canto_ia
                                turno_cantar_persona = True
                            else:
                                ganadas_computadora += 2
                        print(f"Computadora juega: {carta_ia}")

                        ganador_mano = juego.primer_mano(carta_persona,carta_ia,mano_del_juego_persona)

                        if ganador_mano == "Persona":
                            ganadas_persona += 1
                        elif ganador_mano == "Computadora":
                            ganadas_computadora +=1

                    elif ganador_mano == "Computadora":
                        canto_persona = None
                        carta_persona = None
                        print("Le toca jugar a la computadora")

                        juego_ia = jugador_ia.juega(canto_persona,carta_persona, turno_cantar_persona,ganador_primera_mano)
                        canto_ia = juego_ia[0]
                        carta_ia = juego_ia[1]

                        if canto_ia != en_juego and canto_ia != None:
                            acepta_persona = jugador_humano.aceptar_juego()
                            if acepta_persona == True:
                                en_juego = canto_ia
                                turno_cantar_persona = True
                            else:
                                ganadas_computadora += 2
                        print(f"Computadora juega: {carta_ia}")

                        juego_persona = jugador_humano.juega(en_juego,turno_cantar_persona)
                        canto_persona = juego_persona[0]
                        carta_persona = juego_persona[1]
                        if canto_persona != en_juego and canto_persona != None:
                            acepta_ia = jugador_ia.aceptar_juego(canto_persona)                    
                            if acepta_ia == True:
                                en_juego = canto_persona
                                turno_cantar_persona = False
                            else:
                                ganadas_persona += 2
                            en_juego = canto_persona
                            turno_cantar_persona = False
                        print(f"Persona canta: {canto_persona}")
                        print(f"Persona juega: {carta_persona}")

                        ganador_mano = juego.primer_mano(carta_persona,carta_ia,mano_del_juego_persona)
                
                        if ganador_mano == "Persona":
                            ganadas_persona += 1
                        elif ganador_mano == "Computadora":
                            ganadas_computadora +=1

                    if manos == 0:
                        print(f"ganador de la primera mano: {ganador_mano}")
                        ganador_primera_mano = ganador_mano
                    elif manos == 1:
                        print(f"ganador de la segunda mano: {ganador_mano}")
                        ganador_primera_mano = ganador_mano
                    else:
                        if ganadas_persona < 2 or ganadas_computadora < 2:
                            print(f"ganador de la tercer mano: {ganador_mano}")
                            ganador_primera_mano = ganador_mano

                else:

                    if ganadas_persona < ganadas_computadora:
                        print(f"GANADOR DEL TRUCO: ¡Computadora!")
                    else:
                        print(f"GANADOR DEL TRUCO: ¡Persona!")

                manos += 1
            
            print(f"El juego queda: {juego.mostrar_tablero()}")
            counter += 1

        else: # Es mano la IA

            print("Es mano la computadora")
            juego.envido_mano_computadora(jugador_humano,jugador_ia, mano_humano)

            manos = 0
            mano_del_juego_persona = False
            ganador_mano = None
            
            turno_cantar_persona = False
            en_juego = 0
            ganador_primera_mano = None
            ganadas_persona = 0
            ganadas_computadora = 0

            while manos < 3:

                if ganadas_persona < 2 and ganadas_computadora < 2:

                    print(f"****************  Mano {manos + 1} *********************")

                    if turno_cantar_persona == True:
                        print("Te toca cantar...")
                    else:
                        print("Le toca cantar a la computadora")

                    if ganador_mano == "Computadora" or ganador_mano == None:
                        canto_persona = None
                        carta_persona = None

                        print("Le toca jugar a la computadora")
                        juego_ia = jugador_ia.juega(canto_persona,carta_persona, turno_cantar_persona,ganador_primera_mano)
                        canto_ia = juego_ia[0]
                        carta_ia = juego_ia[1]
                    
                        if canto_ia != en_juego and canto_ia != None:
                            acepta_persona = jugador_humano.aceptar_juego()
                            if acepta_persona == True:
                                en_juego = canto_ia
                                turno_cantar_persona = True
                            else:
                                ganadas_computadora += 2
                        print(f"Computadora juega: {carta_ia}")

                        juego_persona = jugador_humano.juega(en_juego,turno_cantar_persona)
                        canto_persona = juego_persona[0]
                        carta_persona = juego_persona[1]

                        print(f"En juego: {en_juego}, persona canta: {canto_persona}, turno persona: {turno_cantar_persona}")

                        if canto_persona != en_juego and canto_persona != None:
                            acepta_ia = jugador_ia.aceptar_juego(canto_persona)                    
                            if acepta_ia == True:
                                en_juego = canto_persona
                                turno_cantar_persona = False
                            else:
                                ganadas_persona += 2
                            en_juego = canto_persona
                            turno_cantar_persona = False
                        print(f"Persona canta: {canto_persona}")
                        print(f"Persona juega: {carta_persona}")

                        ganador_mano = juego.primer_mano(carta_persona,carta_ia,mano_del_juego_persona)

                        if ganador_mano == "Persona":
                            ganadas_persona += 1
                        elif ganador_mano == "Computadora":
                            ganadas_computadora +=1
                    
                    elif ganador_mano == "Persona":
                        canto_persona = None
                        carta_persona = None

                        print("Le toca jugar a la persona")
                        juego_persona = jugador_humano.juega(en_juego,turno_cantar_persona)
                        canto_persona = juego_persona[0]
                        carta_persona = juego_persona[1]

                        if canto_persona != en_juego and canto_persona != None:
                            acepta_ia = jugador_ia.aceptar_juego(canto_persona)                    
                            if acepta_ia == True:
                                en_juego = canto_persona
                                turno_cantar_persona = False
                            else:
                                ganadas_persona += 2                       
                        print(f"Persona juega: {carta_persona}")
                        
                        juego_ia = jugador_ia.juega(en_juego,carta_persona, turno_cantar_persona,ganador_primera_mano)
                        canto_ia = juego_ia[0]
                        carta_ia = juego_ia[1]
                        if (canto_ia != en_juego and canto_ia != None) or (canto_persona == 0 and manos == 0):
                            acepta_persona = jugador_humano.aceptar_juego()
                            if acepta_persona == True:
                                en_juego = canto_ia
                                turno_cantar_persona = True
                            else:
                                ganadas_computadora += 2

                        print(f"Computadora juega: {carta_ia}")

                        ganador_mano = juego.primer_mano(carta_persona,carta_ia,mano_del_juego_persona)

                        if ganador_mano == "Persona":
                            ganadas_persona += 1
                        elif ganador_mano == "Computadora":
                            ganadas_computadora +=1

                    if manos == 0:
                        print(f"ganador de la primera mano: {ganador_mano}")
                        ganador_primera_mano = ganador_mano
                    elif manos == 1:
                        print(f"ganador de la segunda mano: {ganador_mano}")
                        ganador_primera_mano = ganador_mano
                    else:
                        if ganadas_persona < 2 or ganadas_computadora < 2:
                            print(f"ganador de la tercer mano: {ganador_mano}")
                            ganador_primera_mano = ganador_mano

                else:
                    if ganadas_persona < ganadas_computadora:
                        print(f"GANADOR DEL TRUCO: ¡Computadora!")
                    else:
                        print(f"GANADOR DEL TRUCO: ¡Persona!")

                manos += 1    
        
            print(f"El juego queda: {juego.mostrar_tablero()}")                    
            counter += 1

juego = Juego()
main()