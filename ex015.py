dias = int(input("Qauntos dias? "))
km = float(input("Quantos km rodados "))
pago = (dias * 60) + (km * 0.15)
print(f"O total a pagar e de R${pago:.2f}")
