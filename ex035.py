print('-=-'*20)
print('Analisador de Triângulo')
print('-=-'*20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM FORMAR0 um Triângulo.')
else:
    print('Os segmentos acima NÂO PODEM FORMAR um Triângulo.')