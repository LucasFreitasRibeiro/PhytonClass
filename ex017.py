"""catetooposto = float(input("Comprimento do cateto oposto: "))
catetoadjacente = float(input("Comprimento do catoto adjacente: "))
hipotenusa = (catetooposto ** 2 + catetoadjacente ** 2) ** (1/2)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")"""

from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print(f"A hipoitenusa vai medir {hi:.2f}")
