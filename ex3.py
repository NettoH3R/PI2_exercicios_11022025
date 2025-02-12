try:
    f_cust = float(input("Digite o custo de fabrica do carro: "))

    total_custc = f_cust + (f_cust*0.28) + (f_cust*0.45)

    print(f"O Custo final do carro será de R$ {total_custc:.2f}")

except:
    print("Valor digitado invalido!")