import math

print "introduce un numero"
numero = float(raw_input())

factorial = math.factorial(math.floor(numero))
logaritmo = math.log1p(numero)

print "El el factorial del numero %d es %d y el su logaritmo es %f"%(numero,factorial,logaritmo)
