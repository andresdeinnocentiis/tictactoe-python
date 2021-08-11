import random


class Campo(object):
    def __init__(self):
        pass
    
    def crearCampo(self):
        campo = []
        for linea in range(5):
            fila = []
            if linea % 2 == 0:
                for columna in range(5):
                    if columna % 2 == 0:
                        fila.append("   ")
                    else:
                        fila.append("|")
            
            else:
                for columna in range(5):
                    if columna % 2 == 0:
                        fila.append("---")
                    else:
                        fila.append("-")
                #fila.append("-----")
            campo.append(fila)
                
        return campo

    def convertirString(self, campo):
        campo_str = ""
        for fila in campo:
            for columna in fila:
                campo_str += columna
            campo_str += "\n"
            
        return campo_str
    

                        
            
class Jugador:
    def __init__(self, nombre = ""):
        self.__nombre: nombre
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre    
        
    def elegir_ficha(self):
        ficha = (input("Eliga la ficha con la cual desea jugar (X / O): ")).upper()
        if ficha != "X" and ficha != "O":
            print("La ficha elegida no existe. Por favor elija nuevamente.")
            ficha = (input("Eliga la ficha con la cual desea jugar (X / O): ")).upper()
        
        return ficha
    
        
    def mover_filas(self):
        moverFila = int(input("Por favor ingrese el nro. de fila en la que desea mover (0, 1 o 2): "))
        if moverFila != 0:
            moverFila *= 2
            
        return moverFila
    
    
    def mover_columnas(self):
        moverColumna = int(input("Por favor ingrese el nro. de columna en la que desea marcar (0, 1 o 2): "))
        if moverColumna != 0:
            moverColumna *= 2
            
        return moverColumna
                
                


    





def main():
    jugador1 = Jugador()
    jugador1.set_nombre(input("Ingrese el nombre del Jugador 1: "))
    ficha1 = jugador1.elegir_ficha()
    ficha2 = ""
    if ficha1 == "X":
        ficha2 = "O"
    else:
        ficha2 = "X"
    jugador2 = Jugador()
    jugador2.set_nombre(input("Ingrese el nombre del Jugador 2: "))
    print("\n")
    campo = Campo().crearCampo()
    
    campostr = Campo().convertirString(campo)
    print(campostr)
    print("\n")
    print(campo)
    terminar = False
    mover1 = False
    mover2 = False
    while not terminar:
        while not mover1:
            jugador = jugador1.get_nombre()
            print(f"Turno de {jugador}:\n")
            fila = jugador1.mover_filas()
            columna = jugador1.mover_columnas()
            print("\n")
            if campo[fila][columna] == "   ":
                campo[fila][columna] = f" {ficha1} "
                mover1 = True
                mover2 = False
            else:
                print("La casilla seleccionada no se encuentra vacía. Elegí otra, no seas tramposo.")
            
            campostr = Campo().convertirString(campo)
            
        print(campostr)
        print("\n")
            
        while not mover2:
            jugador = jugador2.get_nombre()
            print(f"Turno de {jugador}:\n")
            fila = jugador2.mover_filas()
            columna = jugador2.mover_columnas()
            print("\n")
            if campo[fila][columna] == "   ":
                campo[fila][columna] = f" {ficha2} "
                mover2 = True
                mover1 = False
            else:
                print("La casilla seleccionada no se encuentra vacía. Elegí otra, no seas tramposo.")
            
            
            campostr = Campo().convertirString(campo)
            
        print(campostr)
        print("\n")
        
# VICTORIA POR FILAS:
        
        if ((campo[0][0] == campo[0][2]) and (campo[0][0] == campo[0][4])) and campo[0][0] != "   ":
            if ficha1 in campo [0][0]:
                print(f"Ha ganado {jugador1.get_nombre()}.\n{jugador2.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            else: 
                print(f"Ha ganado {jugador2.get_nombre()}.\n{jugador1.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            terminar = True
               
        elif ((campo[2][0] == campo[2][2]) and (campo[2][0] == campo[2][4])) and campo[2][0] != "   ":
            if ficha1 in campo [2][0]:
                print(f"Ha ganado {jugador1.get_nombre()}.\n{jugador2.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            else: 
                print(f"Ha ganado {jugador2.get_nombre()}.\n{jugador1.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            terminar = True
                
        elif ((campo[4][0] == campo[4][2]) and (campo[4][0] == campo[4][4])) and campo[4][0] != "   ":
            if ficha1 in campo [4][0]:
                print(f"Ha ganado {jugador1.get_nombre()}.\n{jugador2.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            else: 
                print(f"Ha ganado {jugador2.get_nombre()}.\n{jugador1.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            terminar = True
            
# VICTORIA POR COLUMNAS:

        elif ((campo[0][0] == campo[2][0]) and (campo[0][0] == campo[4][0])) and campo[0][0] != "   ":
            if ficha1 in campo [0][0]:
                print(f"Ha ganado {jugador1.get_nombre()}.\n{jugador2.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            else: 
                print(f"Ha ganado {jugador2.get_nombre()}.\n{jugador1.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            terminar = True
        
        elif ((campo[0][2] == campo[2][2]) and (campo[0][2] == campo[4][2])) and campo[0][2] != "   ":
            if ficha1 in campo [0][2]:
                print(f"Ha ganado {jugador1.get_nombre()}.\n{jugador2.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            else: 
                print(f"Ha ganado {jugador2.get_nombre()}.\n{jugador1.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            terminar = True
        
        elif ((campo[0][4] == campo[2][4]) and (campo[0][4] == campo[4][4])) and campo[0][4] != "   ":
            if ficha1 in campo [0][4]:
                print(f"Ha ganado {jugador1.get_nombre()}.\n{jugador2.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            else: 
                print(f"Ha ganado {jugador2.get_nombre()}.\n{jugador1.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            terminar = True
        
# VICTORIA EN DIAGONAL:

        elif ((campo[0][0] == campo[2][2]) and (campo[0][0] == campo[4][4])) and campo[0][0] != "   ":
            if ficha1 in campo [0][0]:
                print(f"Ha ganado {jugador1.get_nombre()}.\n{jugador2.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            else: 
                print(f"Ha ganado {jugador2.get_nombre()}.\n{jugador1.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            terminar = True
        
        elif ((campo[4][0] == campo[2][2]) and (campo[4][0] == campo[0][4])) and campo[4][0] != "   ":
            if ficha1 in campo [4][0]:
                print(f"Ha ganado {jugador1.get_nombre()}.\n{jugador2.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            else: 
                print(f"Ha ganado {jugador2.get_nombre()}.\n{jugador1.get_nombre()} ha resultado ser un perdedor tras una derrota humillante.")
            terminar = True
        print("\n")
main()