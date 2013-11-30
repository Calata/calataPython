print "Hola Introduce una palabra"
palabra = raw_input()
print "Ahora introduce un numero"
numero_int = int(raw_input())


for x in palabra:
	for y in range(palabra):
		print "La %d es %s"%y,x
