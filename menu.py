import time

while True:
    print("[1] Mostrar la hora\t[2] Mostrar la fecha\t[3] Salir")
    opcion = input("> ")
    if opcion == "1":
        print(time.strftime("%H:%M:%S"))

    if opcion == "2":
        print(time.strftime("%d/%m/%Y"))

    if opcion == "3":
        break