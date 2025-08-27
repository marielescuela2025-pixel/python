def consultar_saldo(saldo):
    print(f"Tu saldo es: {saldo}\n")

def retirar_dinero(saldo):
    retirar = float(input("Cuanto dinero quieres retirar: \n   "))
    if retirar > saldo:
        print("No hay suficiente saldo\n") 
    else:
        saldo -= retirar
        print(f"Retiraste: {retirar}\n")
    return saldo

def depositar_dinero(saldo):
    depositar = float(input("\nCuanto dinero quieres depositar:   \n "))
    if depositar > 0:
        saldo += depositar
        print(f"\nDepositaste: {depositar}\n")
    else:
        print("\nCantidad no valida\n")
    return saldo

intentos = 0
saldo = 1000
while intentos < 3:
    pin = int(input("Ingresa tu pin:    "))
    if pin == 1234:
        print("Pin correcto")
        opcion = 0  
        while opcion != 4:
            print("1. Consultar saldo\n2. Retirar dinero\n3. Depositar dinero\n4. Salir")
            opcion = int(input("Escoge una opcion:    "))
            if opcion == 1:
                consultar_saldo(saldo)
            elif opcion == 2:
                saldo = retirar_dinero(saldo)
            elif opcion == 3:
                saldo = depositar_dinero(saldo)
            elif opcion == 4:
                print("\nGracias por usar el cajero\n")
            else:
                print("\nOpcion no valida\n")
        break
    else:
        intentos += 1
        print(f"\nPin incorrecto. Intento {intentos} de 3.\n")
        if intentos == 3:
            print("pasaste el numero de intentos")