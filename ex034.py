salario = float(input('Digite o salário do funcionário: R$'))
if salario <= 1350:
    aumento = (salario * 15 / 100 ) + salario
else:
    aumento = (salario * 10 / 100) + salario
print(f'O salário era {salario:.2f} e passa a ser R${aumento:.2f} com o aumento.')
