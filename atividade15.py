hora = float(input("quantas horas vc trabalhou no mes: "))
hora2 = float(input("quantas horas vc trabanhou por mes: "))
salario = hora * hora2 
ir = salario * 0.11
inss = salario * 0.08
sin = salario * 0.05
desconto = ir + inss + sin
resultado = salario - desconto
print(f"O seu salario bruto é R${salario}")
print(f"IR(11%) R${ir}")
print(f"INSS(8%) R${inss}")
print(f"SINDICADO(5%) R${sin}")
print(f"O resultado final é R${resultado}")