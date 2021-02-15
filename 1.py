
print("="*10,"Calcular cuantas personas quedaran sin ser atendidas", "="*10)

minutos = int(input("Cuantos minutos demoran en atender a una persona: "))
n_personas = int(input("Cantidad de personas que esperan en la cola: "))

tiempo = int(input("Cuantas horas falta para cerrar el banco: ")) * 60

personasSinAtender = (minutos * n_personas - tiempo) // minutos

print("===========================================================")
print(personasSinAtender, "personas se quedarán sin ser atendidas")




