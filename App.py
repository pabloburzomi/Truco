import random
import time

from Verificador_Juego import *
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

    while verificador_juego.mostrar_tablero()[0] < ptos_para_ganar and verificador_juego.mostrar_tablero()[1] < ptos_para_ganar:

        mazo.mezclar_mazo()
        cartas_humano = mazo.repartir_cartas()
        cartas_ia = mazo.repartir_cartas()
        print("Repartiendo cartas...\n\n")
        time.sleep(2)
        #Los Jugadores
        jugador_humano = Humano(cartas_humano)
        jugador_ia = Computadora(cartas_ia)

        mano_humano = False

        if counter % 2 == 0:   # ES MANO LA PERSONA
            print("Es mano la persona")
            juega_persona = int(input(f"Elija: {menu_opciones}")) - 1

            # SI LA PERSONA JUEGA CON EL MENU DE ENVIDO
            if juega_persona == 0:  
                verificador_juego.envido_mano_persona(jugador_humano,jugador_ia, mano_humano)
            verificador_juego.definicion_truco_persona(jugador_humano, jugador_ia)

            counter += 1
            

        else: # Es mano la IA

            print("Es mano la computadora")
            verificador_juego.envido_mano_computadora(jugador_humano,jugador_ia, mano_humano)
            verificador_juego.definicion_truco_computadora(jugador_humano, jugador_ia)

            counter += 1
           

verificador_juego = Verificador_Juego()
main()