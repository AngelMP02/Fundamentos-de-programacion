def partida_ajedrez(nombre_fichero):
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero=[]
    for i in tablero_inicial.split("/n"):#las separo unas de otras y las uno a tablero
        tablero.append(i.split("/t"))
    f=open(nombre_fichero,"w")
    for i in tablero:
         f.write('\t'.join(i) + '\n')
     
    f.close()
    movimiento=0
    while True:
        continuar=input("¿quieres hacer otro movimiento?(si/no):")
        if continuar!="si":
            break #si el usuario pone algo distinto a si se para
        else: #si pone si contiunua jugando
            fila_inicial=input("introduce la fila de la pieza a mover:")
            columna_inicial=input("introduce la columna inicial:")
            fila_destino=input("introduce la fila a la que quieres mover:")
            columna_destino=input("introduce la columna a la que quieres mover:")
            tablero[fila_destino-1][columna_destino-1] = tablero[fila_inicial-1][columna_inicial-1]
            tablero[fila_inicial-1][columna_inicial-1] = ""
            movimiento += 1 #sumo 1 al contador
            f=open(nombre_fichero, "a")
            f.write('Movimiento' + str(movimiento) + '\n')
            for i in tablero:
                f.write(('\t'.join(i) + '\n'))
                f.close
    return
def partida_ajedrez(nombre_fichero):
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero=[]
    for i in tablero_inicial.split("/n"):#las separo unas de otras y las uno a tablero
        tablero.append(i.split("/t"))
    f=open(nombre_fichero,"w")
    for i in tablero:
       f.write('\t'.join(i) + '\n')
     
    f.close()
    movimiento=0
    while True:
        continuar=input("¿quieres hacer otro movimiento?(si/no):")
        if continuar!="si":
            break #si el usuario pone algo distinto a si se para
        else: #si pone si contiunua jugando
            fila_inicial=input("introduce la fila de la pieza a mover:")
            columna_inicial=input("introduce la columna inicial:")
            fila_destino=input("introduce la fila a la que quieres mover:")
            columna_destino=input("introduce la columna a la que quieres mover:")
            tablero[fila_destino-1][columna_destino-1] = tablero[fila_inicial-1][columna_inicial-1]
            tablero[fila_inicial-1][columna_inicial-1] = ""
            movimiento += 1 #sumo 1 al contador
            f=open(nombre_fichero, "a")
            f.write('Movimiento' + str(movimiento) + '\n')
            for i in tablero:
                f.write(('\t'.join(i) + '\n'))
                f.close
    return


partida_ajedrez('partida1.txt')

    