try:

    tipo = int(input("Digite o tipo de combustível (1-Álcool, 2-Gasolina): "))
    litros = float(input("Digite a quantidade de litros: "))

    preco_alcool = 2.90
    preco_gasolina = 3.30
    
    if tipo == 1:  
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
        preco_litro = preco_alcool

    elif tipo == 2:  
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
        preco_litro = preco_gasolina
    else:
        print("Tipo de combustível inválido.")
    
    valor_total = litros * preco_litro * (1 - desconto)
    valor_total = round(valor_total, 2)


    print(f"Valor a ser pago: R$ {valor_total}")

except:
    print("Valor Inadequado!")