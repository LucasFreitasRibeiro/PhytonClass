velocidade = float(input('Qual a velocidade do seu carro? '))
if velocidade > 80:
    print('MULTADO! Você ultraoassou o limite de velocidade permitido, que é de 80km/h.')
    multa = (velocidade-80) * 7
    print(f'Você deve pagar um multa de R${multa}!')
print('Tenha um bom dia! Dirija com segurança.')