#Ejercicio 3: Obtener el radio y longitud de un circulo
import math
r = float(input("ingrese el radio: "))
area = math.pi*(r**2)
longitud = 2*math.pi*r

print(f"El area es: {area:.1f}")
print(f"La longitud es: {longitud:.1f}")