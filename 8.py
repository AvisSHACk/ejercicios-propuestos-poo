print("="*10, "XYZ SAC" , "*"*10)

h_trabajadas = float(input("Ingrese el numero de horas trabajadas: "))
turno = input("Ingrese el turno de trabajo: ")

salario_bruto = h_trabajadas * 36

if turno == "tarde":
    salario_bruto += 1.60
elif turno == 'noche':
    salario_bruto += 2.50

print("Turno: ", turno)
print("Salario neto: ", salario_bruto)

