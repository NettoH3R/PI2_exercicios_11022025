try:
    valor = float(input("Digite o valor da compra: "))

    print("Digite sua credencial \n\n 1 - FUNCIONARIO \n 2 - CLIENTE VIP \n 3  - CLIENTE COMUM \n")    
    credencial = int(input("> "))

    if credencial == 1:
        print(f"Valor da Compra: R${0.9*valor:.2f}")

    elif credencial == 2:
        print(f"Valor da Compra: R${0.95*valor:.2f}")

    elif credencial == 3:
        print(f"Valor da Compra: R${valor:.2f}")

    else: 
        print("Número Inadequado")
except:
    print("Valor Inadequado!")