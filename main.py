from biblioteca import *

def menu():
    lista_completa = None
    archivo_cargado = False
    while True:
        limpiar_pantalla()
        print("1- Cargar archivo con los servicios")
        print("2- Imprimir lista de servicios")
        print("3- Calcular total del servicio y asignarlo a la lista")
        print("4- filtrar por tipo de servicio")
        print("5- Servicios ordenados por descripcion de forma ascendente")
        print("")
        print("0-Salir del programa.")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            limpiar_pantalla()
            nombre_del_Archivo_a_cargar = input("Ingrese el nombre del archivo: ")
            input_sin_espacios = nombre_del_Archivo_a_cargar.replace(" ", "")
            lista_completa = leer_json(input_sin_espacios)
            if lista_completa is not None:
                archivo_cargado = True
            presionar_tecla()
        elif opcion == 2:
            limpiar_pantalla()
            if archivo_cargado:
                imprimir_cabecera_mas_datos(lista_completa, "todo")
            else:
                print("Primero debes cargar el archivo con los servicios!")
            presionar_tecla()
        elif opcion == 3:
            limpiar_pantalla()
            if archivo_cargado:
                list(map(lambda servicio: servicio.update({'totalServicio': float(servicio['precioUnitario']) * int(servicio['cantidad'])}), lista_completa))
                print("Totales calculados con exito.")
            else:
                print("Primero debes cargar el archivo con los servicios!")
            presionar_tecla()
        elif opcion == 4:
            limpiar_pantalla()
            if archivo_cargado:
                sub_menu(lista_completa)
            else:
                print("Primero debes cargar el archivo con los servicios!")
            presionar_tecla()
        elif opcion == 5:
            limpiar_pantalla()
            if archivo_cargado:
                ordenamiento_por_burbujeo(lista_completa, "ascendente", "descripcion")
                imprimir_cabecera_mas_datos(lista_completa, "todo")
            else:
                print("Primero debes cargar el archivo con los servicios!")
            presionar_tecla()
        elif opcion == 6:
            limpiar_pantalla()
            if archivo_cargado:
                with open("servicios_ordenados_por_descripcion.json", 'w') as archivo:
                    json.dump(lista_completa, archivo, indent=4)
                    print(f"Archivo generado")
            else:
                print("Primero debes cargar el archivo con los servicios!")
            presionar_tecla()
        elif opcion == 0:
            limpiar_pantalla()
            print("Saliendo del programa...")
            break
        else:
            limpiar_pantalla()
            print("Opción no válida. Intente nuevamente.")
            presionar_tecla()

menu()