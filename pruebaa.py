pelicula=('CARS')
asientos= [[False] * 11 for _ in range(16)]
asientos_asignados={}

def mostrar_asientos(pelicula):

    print(f'Asientos disponibles para la película: {pelicula}')
    print('*********************************\n\
           *           PANTALLA            *\n\
           *********************************\n')
    for f in range(16):  # Rango corregido
        for c in range(11):  # Rango corregido
            if f == 0:  # Fila 0 representa los números de columna
                if c == 10:  # Última columna
                    print()
                else:
                    print(f' {c + 1} ', end='')  # Mostrar número de columna
            else:
                if c == 10:  # Última columna
                    print(f' {f} ', end='')  # Mostrar número de fila
                else:
                    if asientos[f - 1][c]:  # Acceder a la matriz de asientos (restar 1 para compensar)
                        print(' x ', end='')  # Asiento reservado
                    else:
                        print(' . ', end='')  # Asiento disponible
        print()

def comprar_entrada():
    print("Películas a la venta:")
    print(pelicula)

    mostrar_asientos(pelicula)
    while True:
        try:
            fila = int(input("Ingrese el número de fila del asiento: "))
            columna = int(input("Ingrese el número de columna del asiento: "))
            break
        except:
            print('error, vuelva a intentarlo.')
            

        if fila < 1 or fila > 15 or columna < 1 or columna > 10:
            print("Asiento inválido.")
        

        if asientos[fila - 1][columna - 1]:
            print("El asiento seleccionado ya está reservado.")
            return

    nombre = input('Indique su nombre para generar la boleta: ')
    asientos[fila - 1][columna - 1] = True
    asientos_asignados[nombre]=[fila, columna]
    
    while True:
        cont_ventas=0
        duoc = input('Es alumno de Duoc UC? [y] or [n]: ')
        if duoc == 'n':
            cont_ventas+=1
            boleta = f"\nBOLETA DE COMPRA{cont_ventas}\n" \
                        f"---------------\n" \
                        f"Cliente: {nombre.upper}\n" \
                        f"Película: {pelicula}\n" \
                        f"Asiento: Fila {fila}, Columna {columna}\n" \
                        f"Valor de la entrada: $2500\n"\
                        f"¡Disfrute de la función!\n"
            break
        elif duoc == 'y':
            cont_ventas+=1
            descuento= 2500*0.2
            boleta = f"\nBOLETA DE COMPRA{cont_ventas}\n" \
                    f"---------------\n" \
                    f"Cliente: {nombre.upper}\n" \
                    f"Película: {pelicula}\n" \
                    f"Asiento: Fila {fila}, Columna {columna}\n" \
                    f"Valor de la entrada: ${2500-descuento}\n"\
                    f"Descuento aplicado del 20% por ser alumno de duoc\n"\
                    f"¡Disfrute de la función!\n"
            break

        else:
            print('error')
            

    print(boleta)

    nombre_archivo = f"boleta{cont_ventas}.txt"  
    with open(nombre_archivo, "w") as archivo:
        archivo.write(boleta)

        print("Se ha generado una copia de la boleta y exportado exitosamente en el archivo 'boleta.txt'.")
        print('Gracias por preferirnos😀')


    
def listar_nombre_asiento():
    print(f"Película: {pelicula}")
    for j in asientos_asignados:
        print(f"Asistente: {j}\nAsiento: fila {asientos_asignados[j][0]} columna {asientos_asignados[j][1]}\n")

while True:
    try:
        print('*********  MENU  **********')
        print('[1] Comprar entrada para Cars')
        print('[2] Mostrar Asientos')
        print('[3] Listar entradas')
        print('[0] Salir')

        opc=int(input('Ingrese una opcion: '))
        print('\033c', end='')
        if opc == 1:
            comprar_entrada()
            input('Presione -intro- para continuar')
            print('\033c', end='')
        elif opc == 2:
            mostrar_asientos(pelicula)
            input('Presione -intro- para continuar')
            print('\033c', end='')
        elif opc== 3:
            listar_nombre_asiento()
            input('Presione -intro- para continuar')
            print('\033c', end='')
        elif opc== 0:
            break
            print('\033c', end='')
        else:
            print('opcion invalida, intente denuevo.')
    except:
        print('error. Intente nuevamente')