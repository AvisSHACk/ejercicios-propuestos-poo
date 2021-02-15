print("*"*10, "Feria del King Kong", "*"*10)

n_celular = int(input("Numero de celular: "))
dni = input("Ingresa el numero de dni: ")
n_entradas = int(input("Ingrese el numero de entradas que se va a vender: "))
modalidad = ''

precio = 50 * n_entradas
descuento = 0

if n_entradas >= 3: 
    modalidad = "Grupo"
    descuento = precio * 0.30
elif n_entradas == 2: 
    modalidad = 'Pareja'
    descuento = precio * 0.10
else: 
    modalidad = 'Solo'

print("*"*10, "Feria del King Kong", "*"*10)
print("DNI: ", dni)
print("Modalidad: ", modalidad)
print("Descuento: ", descuento)
print("Total a pagar: ", precio - descuento)
