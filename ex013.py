sal = float(input("Qual e o salario do funcionario: R$"))
aum = float(input("Qual vai ser o aumento: "))
novosal = sal + (sal * aum / 100)
print(f"O funcionario que ganhava R${sal:.2f}, com {aum:.2f}% de aumento, passa a receber R${novosal:.2f}.")