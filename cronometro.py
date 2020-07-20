import time

segundero = 0
maximo = 5

while True: 
	time.sleep(1)   # esperamos un segundo
	segundero += 1  # segundero = segundero + 1
	print(segundero)

	if segundero == maximo:
		print("Se ha llegado al límite, rompiendo el bucle infinito")
		break