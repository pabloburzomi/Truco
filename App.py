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
    print("Saliste sorteado para empezar la partida\n" if counter % 2 == 0 else "Salio sorteada la computadora para empezar la partida\n")
   
    menu_opciones = ["Envido", "Truco", "Flor","Jugar sin cantar","Mazo"]

    while juego.mostrar_tablero()[0] < ptos_para_ganar and juego.mostrar_tablero()[1] < ptos_para_ganar:

        mazo.mezclar_mazo()
        cartas_humano = mazo.repartir_cartas()
        cartas_ia = mazo.repartir_cartas()
        print("Repartiendo cartas...\n\n")
        time.sleep(2)
        #Los Jugadores
        jugador_humano = Humano(cartas_humano)
        jugador_ia = Computadora(cartas_ia)
        """ print(f"Tus cartas son {jugador_humano.mostrar_cartas()} - Las cartas de la computadora son {cartas_ia}")
        print(f"El juego queda: {juego.mostrar_tablero()}") """
        mano_humano = False

        if counter % 2 == 0:   # ES MANO LA PERSONA
            print("Es mano la persona")
            juega_persona = int(input(f"Elija: {menu_opciones}")) - 1

            # SI LA PERSONA JUEGA CON EL MENU DE ENVIDO
            if juega_persona == 0:  juego.envido_mano_persona(jugador_humano,jugador_ia, mano_humano)

            mano_humano, mano_del_juego_persona, turno_cantar_persona = True, True, True
            ganador_mano, ganador_primera_mano = None, None
            manos, en_juego, ganadas_persona, ganadas_computadora = 0, 0, 0, 0

            while manos < 3:

                if ganadas_persona < 2 and ganadas_computadora < 2:
                    
                    print(f"****************  Mano {manos + 1} *********************")

                    print("Te toca cantar..." if turno_cantar_persona else "Le toca cantar a la computadora")
                    
                    if ganador_mano == "Persona" or ganador_mano == None:
                        canto_persona,carta_persona = None,None
                        print("Le toca jugar a la persona")
                        canto_persona,carta_persona = jugador_humano.juega(en_juego,turno_cantar_persona)

                        if canto_persona != en_juego and canto_persona != None:                    
                            if jugador_ia.aceptar_juego(canto_persona): en_juego,turno_cantar_persona = canto_persona,False
                            else: ganadas_persona += 2
                        
                        print(f"Persona juega: {carta_persona}")
                        
                        canto_ia,carta_ia = jugador_ia.juega(en_juego,carta_persona, turno_cantar_persona,ganador_primera_mano)
                        if (canto_ia != en_juego and canto_ia != None) or (canto_persona == 0 and manos == 0):
                            if jugador_humano.aceptar_juego(): en_juego,turno_cantar_persona = canto_ia,True
                            else: ganadas_computadora += 2

                            print(f"Computadora juega: {carta_ia}")

                        ganador_mano = juego.primer_mano(carta_persona,carta_ia,mano_del_juego_persona)
                        if ganador_mano == "Persona": ganadas_persona += 1
                        else: ganadas_computadora +=1

                    elif ganador_mano == "Computadora":
                        canto_persona,carta_persona = None,None
                        print("Le toca jugar a la computadora")
                        canto_ia, carta_ia= jugador_ia.juega(canto_persona,carta_persona, turno_cantar_persona,ganador_primera_mano)

                        if canto_ia != en_juego and canto_ia != None:
                            if jugador_humano.aceptar_juego(): en_juego , turno_cantar_persona = canto_ia, True
                            else:  ganadas_computadora += 2

                        print(f"Computadora juega: {carta_ia}")

                        canto_persona, carta_persona = jugador_humano.juega(en_juego,turno_cantar_persona)
                        if canto_persona != en_juego and canto_persona != None:
                            if jugador_ia.aceptar_juego(canto_persona): en_juego, turno_cantar_persona = canto_persona, False
                            else: ganadas_persona += 2

                        print(f"Persona canta: {canto_persona}")
                        print(f"Persona juega: {carta_persona}")

                        ganador_mano = juego.primer_mano(carta_persona,carta_ia,mano_del_juego_persona)

                        # DE ACA EN ADELANTE SE PUEDEN HACER 3 METODOS CON CADA TROZO DE CODIGO hASTA QUE ES MANO LA IA

                        if ganador_mano == "Persona": ganadas_persona += 1
                        else: ganadas_computadora += 1

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

                    if ganadas_persona < ganadas_computadora: print(f"GANADOR DEL TRUCO: ¡Computadora!")
                    else: print(f"GANADOR DEL TRUCO: ¡Persona!")

                manos += 1
            
            print(f"El juego queda: {juego.mostrar_tablero()}")
            counter += 1

        else: # Es mano la IA

            print("Es mano la computadora")
            juego.envido_mano_computadora(jugador_humano,jugador_ia, mano_humano)

            manos, en_juego, ganadas_persona,  ganadas_computadora = 0, 0, 0, 0
            mano_del_juego_persona, turno_cantar_persona = False, False
            ganador_mano, ganador_primera_mano = None, None

            while manos < 3:

                if ganadas_persona < 2 and ganadas_computadora < 2:

                    print(f"****************  Mano {manos + 1} *********************")

                    print("Te toca cantar..." if turno_cantar_persona else "Le toca cantar a la computadora")

                    if ganador_mano == "Computadora" or ganador_mano == None:
                        canto_persona, carta_persona = None, None

                        print("Le toca jugar a la computadora")
                        canto_ia, carta_ia = jugador_ia.juega(canto_persona,carta_persona, turno_cantar_persona,ganador_primera_mano)

                        if canto_ia != en_juego and canto_ia != None:
                            if jugador_humano.aceptar_juego(): en_juego,turno_cantar_persona = canto_ia, True
                            else: ganadas_computadora += 2
                        print(f"Computadora juega: {carta_ia}")

                        canto_persona, carta_persona = jugador_humano.juega(en_juego,turno_cantar_persona)

                        #print(f"En juego: {en_juego}, persona canta: {canto_persona}, turno persona: {turno_cantar_persona}")

                        if canto_persona != en_juego and canto_persona != None:
                            acepta_ia = jugador_ia.aceptar_juego(canto_persona)                    
                            if jugador_ia.aceptar_juego(canto_persona): en_juego,turno_cantar_persona = canto_persona, False
                            else: ganadas_persona += 2

                        print(f"Persona canta: {canto_persona}")
                        print(f"Persona juega: {carta_persona}")

                        ganador_mano = juego.primer_mano(carta_persona,carta_ia,mano_del_juego_persona)

                        if ganador_mano == "Persona": ganadas_persona += 1
                        else: ganadas_computadora +=1
                    
                    elif ganador_mano == "Persona":
                        canto_persona, carta_persona= None, None

                        print("Le toca jugar a la persona")
                        canto_persona, carta_persona = jugador_humano.juega(en_juego,turno_cantar_persona)

                        if canto_persona != en_juego and canto_persona != None:
                   
                            if jugador_ia.aceptar_juego(canto_persona): en_juego, turno_cantar_persona = canto_persona, False
                            else:  ganadas_persona += 2                       
                        print(f"Persona juega: {carta_persona}")
                        
                        canto_ia, carta_ia= jugador_ia.juega(en_juego,carta_persona, turno_cantar_persona,ganador_primera_mano)

                        if (canto_ia != en_juego and canto_ia != None) or (canto_persona == 0 and manos == 0):

                            if jugador_humano.aceptar_juego(): en_juego, turno_cantar_persona = canto_ia, True
                            else: ganadas_computadora += 2

                        print(f"Computadora juega: {carta_ia}")

                        ganador_mano = juego.primer_mano(carta_persona,carta_ia,mano_del_juego_persona)

                        if ganador_mano == "Persona": ganadas_persona += 1
                        else: ganadas_computadora +=1

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
                    if ganadas_persona < ganadas_computadora: print(f"GANADOR DEL TRUCO: ¡Computadora!")
                    else:  print(f"GANADOR DEL TRUCO: ¡Persona!")

                manos += 1    
        
            print(f"El juego queda: {juego.mostrar_tablero()}")                    
            counter += 1

juego = Juego()
main()