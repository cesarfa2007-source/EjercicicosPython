valor_compra = float(input("Ingrese el valor de la compra: "))
if valor_compra > 100000:
    descuento = valor_compra * 0.1
else:
    descuento = 0
    valor_final = valor_compra - descuento
    print(f"Valor a pagar: {valor_final}")