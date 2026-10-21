import math
area = float(input("digite a área: "))
litros = area/3
latas = math.ceil(litros / 18)
preco = (litros / 18)
print(f"Você precisará comprar {latas} lata(s).")
print(f"O preço total é R$ {preco:.2f}")