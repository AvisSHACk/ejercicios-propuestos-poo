print("*"*10, "Salario de un trabajador", "*"*10)

valor_hora = int(input("Ingrese el valor por hora del trabajador: "))
horas_trabajadas = int(input("Ingresa el numero de horas trabajadas: "))

salario_bruto = valor_hora * horas_trabajadas
descuento = salario_bruto * 0.10

salario_neto = salario_bruto - descuento

print("Salario bruto         : ", salario_bruto)
print("Descuento             : ", descuento)
print("Salario del trabajador: ", salario_neto)
