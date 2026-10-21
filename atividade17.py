mb = float(input("digite o tamanho do arquivo em MB: "))
velocidade = float(input("digite a velocidade da conexão de Internet: "))
resultado = mb * 8
segundos = resultado/velocidade
tempo = segundos/60
print(f"o tempo estimado de acabar o download é {tempo:.2} minutos")