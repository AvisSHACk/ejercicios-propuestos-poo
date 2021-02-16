print("*"*10,"Centro de salud", "="*10)

nombres = input("Ingresa los nombres y apellidos del paciente: ")
edad = int(input("Ingresa la edad del paciente: "))
sexo = input("Ingrese el sexo:(M/F) ")
peso = float(input("Ingresa el peso en kilos: "))
talla = float(input("Ingresa la talla en cm: "))

tratamiento = False

if edad == 5 and peso < 18.03 and talla < 106.40 \
    or edad == 6 and peso < 19.91 and talla < 112.77 \
    or edad == 7 and peso < 22 and talla < 118.50 \
    or edad == 8 and peso < 23.56 and talla < 122.86:
    tratamiento = True

if tratamiento:
    print("El paciente", nombres, "necesita un tratamiento nutricional")
else:
    print("El paciente", nombres, "no necesita un tratamiento nutricional")
