def Vuelo():
    vuelo = {
        "Aerolinea": "Avianca",
        "Vuelo": "AV3102",
        "Origen": "CTG",
        "Destino": "MDE",
        "Tipo_Maleta": ['Cabina', 'Mano', 'Bodega']
    }

    for key, value in vuelo.items():
        print(f"{key}: {value}")

    print("Tipos de Maleta:")
    for tipo in vuelo["Tipo_Maleta"]:
        print(tipo)

Vuelo()