print("="*5, "Produccion total por metro cuadrado", "="*5)

while True:
    try :
        hectareas = int(input("¿Cuantas hectareas posee el agricultor?: ")) * 10000
        kilos = int(input("Kilos producidos por cada metro cuadrado: "))
        total = kilos * hectareas
        print("Por cada metro cuadrado se producen", total, "kilos")
        break
    except ValueError:
        print("ERROR: ingresa datos numericos")
