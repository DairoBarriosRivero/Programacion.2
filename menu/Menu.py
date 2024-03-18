while True:
    print("Menu de opciones:")
    print("1. Personas")
    print("2. Vehiculos")
    print("3. Universidades")
    print("4. Notas")
    print("5. Salir")

    opcion = input("Seleccione una opción : ")

    if opcion == '1':
      print("Has elegido la opción Personas")
    elif opcion == '2':
      print("Has elegido la opción Vehiculos")
    elif opcion == '3':
       print("Has elegido la opción Universidades")
    elif opcion == '4':
       print("Has elegido la opción Notas")
    elif opcion == '5':
       print("Saliendo del programa...")
       break
    else:
        print("Opción inválida. Por favor seleccione una opción válida")