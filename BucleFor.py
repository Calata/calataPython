
#Ejemplo con rango
for i  in range (0,5):
	i += 1
	print "Vuelta numero %d"%i
#Ejemplo con array
nombre = ["Jorge","Juan","Ivan","Elisabeth"]
for j in nombre:
	print "mi amigo es %s"%j
#bucle infinito
for x in range (2):
	for y in range(x):
		for z in range(y):
			if z == y:
				break
			print z
			