from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo: "))
sen = sin(radians(angulo))
print(f"O ângulo de {angulo} tem o Seno de {sen:.2f}")
cosseno = cos(radians(angulo))
print(f"O ângulo de {angulo} tem o Conseno de {cosseno:.2f}")
tangente = tan(radians(angulo))
print(f"O ângulo de {angulo} tem a Tangente de {tangente:.2f}")
