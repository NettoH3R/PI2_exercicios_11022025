
chico_altura = 1.50
juca_altura = 1.10
anos = 0

while juca_altura <= chico_altura:
    chico_altura += 0.02
    juca_altura += 0.03
    anos += 1

print(f"Serão necessários {anos} anos para que Juca seja maior que Chico.")
