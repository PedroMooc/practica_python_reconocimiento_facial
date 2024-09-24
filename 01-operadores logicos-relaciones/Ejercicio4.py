#Ejercicio 4: Obtener el precio final que se tiene que pagar si se aplica el 36% de descuento del total de la compra.

precioinicial = float(input("Ingrese el precio: "))
descuento = precioinicial*(36/100)
preciofinal = precioinicial -  descuento

print(f"El precio final es: {preciofinal:.2f}")