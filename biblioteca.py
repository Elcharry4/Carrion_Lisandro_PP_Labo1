import json

def leer_json(nombre_archivo: str):
    try:
        with open(f"FACULTAD\\Parcial_labo\\{nombre_archivo}.json", "r") as archivo:
            lista_elementos = json.load(archivo)
        print("Archivo cargado con exito.")
        return lista_elementos
    except FileNotFoundError:
        print("El archivo no existe. verificar el nombre y volver a intentar.")

def imprimir_cabecera_mas_datos(lista:list, *claves):
    """
    Imprime una lista de diccionarios con una cabecera que muestra las claves especificadas,
    ajustando el ancho de las columnas para que se alineen con los datos más largos.
    
    Args:
    lista (list): La lista de diccionarios a imprimir.
    *claves: Las claves cuyos valores se desean imprimir. Si se pasa 'todo', se imprimirán todos los datos.
    """
    if not lista:
        print("La lista está vacía.")
        return

    if claves[0] == "todo":
        cabecera = list(lista[0].keys())
    else:
        cabecera = list(claves)

    max_ancho = {}
    for clave in cabecera:
        max_ancho[clave] = len(clave)
        for diccionario in lista:
            max_ancho[clave] = max(max_ancho[clave], len(str(diccionario[clave])))

    cabecera_str = []
    for clave in cabecera:
        cabecera_str.append(clave.center(max_ancho[clave]))
    
    cabecera_texto = " | ".join(cabecera_str)
    print(cabecera_texto)
    print("-" * len(cabecera_texto))

    for diccionario in lista:
        fila = []
        for clave in cabecera:
            fila.append(str(diccionario[clave]).center(max_ancho[clave]))
        print(" | ".join(fila))

def sub_menu(lista: list):
    while True:
        limpiar_pantalla()
        print("1- Minorista")
        print("2- Mayorista")
        print("3- Exportar")
        print("0- Volver al menu principal.")
        opcion = int(input("Seleccionar tipo de servicio: "))

        if opcion == 1:
            limpiar_pantalla()
            servicios_filtrados = list(filter(lambda servicio: servicio['tipo'] == "1", lista))
            with open("servicios_tipo_minorista.json", 'w') as archivo:
                json.dump(servicios_filtrados, archivo, indent=4)
                print(f"Archivo generado")
            presionar_tecla()
        elif opcion == 2:
            limpiar_pantalla()
            servicios_filtrados = list(filter(lambda servicio: servicio['tipo'] == "2", lista))
            with open("servicios_tipo_mayorista.json", 'w') as archivo:
                json.dump(servicios_filtrados, archivo, indent=4)
                print(f"Archivo generado")
            presionar_tecla()
        elif opcion == 3:
            limpiar_pantalla()
            servicios_filtrados = list(filter(lambda servicio: servicio['tipo'] == "3", lista))
            with open("servicios_tipo_exportar.json", 'w') as archivo:
                json.dump(servicios_filtrados, archivo, indent=4)
                print(f"Archivo generado")
            presionar_tecla()
        elif opcion == 0:
            limpiar_pantalla()
            break
        else:
            limpiar_pantalla()
            print("Opción no válida. Intente nuevamente.")
            presionar_tecla()

def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def presionar_tecla():
    import msvcrt
    print("Pulsa una tecla para volver al menú")
    msvcrt.getch()

def ordenamiento_por_burbujeo(lista:list, asc_o_des:str, clave:str) ->str:
    """
    Ordena una lista de diccionarios usando el algoritmo de burbujeo.
    
    Args:
    lista (list): La lista de diccionarios a ordenar.
    asc_o_des (str): El modo de ordenamiento, 'ascendente' o 'descendente'.
    clave (str): La clave del diccionario por la cual ordenar.
    """

    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if asc_o_des == "ascendente":
                if lista[i][clave] > lista[j][clave]:
                    lista[i], lista[j] = lista[j], lista[i]
            elif asc_o_des == "descendente":
                if lista[i][clave] < lista[j][clave]:
                    lista[i], lista[j] = lista[j], lista[i]
            else:
                return (f"El parametro debe de ser \"ascendente\" o \"descendente\" usted ingreso: \"{asc_o_des}\"")
    return (f"la lista se ordeno correctamente de manera {asc_o_des}")