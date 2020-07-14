tablero =  {7: ' ' , 8: ' ' , 9: ' ' ,
            4: ' ' , 5: ' ' , 6: ' ' ,
            1: ' ' , 2: ' ' , 3: ' ' }

posiciones_tablero = []

for key in tablero:
    posiciones_tablero.append(key)

def imprimirTablero(tablero):
    print('|' + tablero[7] + '|' + tablero[8] + '|' + tablero[9] + '|')

    print('|' + tablero[4] + '|' + tablero[5] + '|' + tablero[6] + '|')

    print('|' + tablero[1] + '|' + tablero[2] + '|' + tablero[3] + '|')

def jugar():

    jugador = 'X'
    contador = 0
    
    for i in range(10):
            imprimirTablero(tablero)
            print("jugador : " + jugador + " elija posición a marcar")

            mover = int(input())

            try:
                if tablero[mover] == ' ':
                    tablero[mover] = jugador
                    contador += 1
                else:
                    print("Esa posición está marcada.\nelija posición a marcar")
                    continue
            except KeyError:
                print("Debe ingresar un número entre 1 y 9")
                continue
            
            if contador >= 5:
                if tablero[7] == tablero[8] == tablero[9] != ' ':
                    imprimirTablero(tablero)
                    print("\nJuego Terminado.\n")                
                    print(" Jugador " +jugador + " ha ganado.\n")                
                    break
                elif tablero[4] == tablero[5] == tablero[6] != ' ':
                    imprimirTablero(tablero)
                    print("\nJuego Terminado.\n")                
                    print(" Jugador " +jugador + " ha ganado.\n")
                    break
                elif tablero[1] == tablero[2] == tablero[3] != ' ':
                    imprimirTablero(tablero)
                    print("\nJuego Terminado.\n")                
                    print(" Jugador " +jugador + " ha ganado.\n")
                    break
                elif tablero[1] == tablero[4] == tablero[7] != ' ':
                    imprimirTablero(tablero)
                    print("\nJuego Terminado.\n")                
                    print(" Jugador " +jugador + " ha ganado.\n")
                    break
                elif tablero[2] == tablero[5] == tablero[8] != ' ':
                    imprimirTablero(tablero)
                    print("\nJuego Terminado.\n")                
                    print(" Jugador " +jugador + " ha ganado.\n")
                    break
                elif tablero[3] == tablero[6] == tablero[9] != ' ':
                    imprimirTablero(tablero)
                    print("\nJuego Terminado.\n")                
                    print(" Jugador " +jugador + " ha ganado.\n")
                    break 
                elif tablero[7] == tablero[5] == tablero[3] != ' ':
                    imprimirTablero(tablero)
                    print("\nJuego Terminado.\n")                
                    print(" Jugador " +jugador + " ha ganado.\n")
                    break
                elif tablero[1] == tablero[5] == tablero[9] != ' ':
                    imprimirTablero(tablero)
                    print("\nJuego Terminado.\n")                
                    print(" Jugador " +jugador + " ha ganado.\n")
                    break
            if contador == 9:
                print("\nJuego Terminado.\n")                
                print("Empate")

            if jugador =='X':
                jugador = 'O'
            else:
                jugador = 'X'
    reiniciar = input("Desea jugar nuevamente?(y/n)")
    if reiniciar == "y" or reiniciar == "Y":  
        for key in posiciones_tablero:
            tablero[key] = " "
        jugar()

jugar()
