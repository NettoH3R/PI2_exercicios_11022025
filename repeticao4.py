try:
    maior_preco = 0
    soma_precos = 0

    for i in range(15):
        preco = float(input(f"Digite o preço do produto {i+1}: "))
        soma_precos += preco
        if preco > maior_preco:
            maior_preco = preco

    media_precos = soma_precos / 15

    print(f"O maior preço lido foi: R$ {maior_preco:.2f}")
    print(f"A média aritmética dos preços é: R$ {media_precos:.2f}")

except:
    print("Valor Inadequado!")