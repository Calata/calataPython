def vectorProporcional():	
	print "Introduzca el Vector 1"
	vector1a = int(raw_input())
	vector1b = int(raw_input())
	print "Introduzca el vector 2"
	vector2a = int(raw_input())
	vector2b = int(raw_input())

	Cociente1 = vector1a/vector1b
	Cociente2 = vector2a/vector2b

	if Cociente1 == Cociente2:
		print "Los Vectores son Proporcionales"
	else:
		print "Los vectores son linealmente Independientes"
		print "Quieres Calcular el vector que forman?"
		print "S/N"
		Cond = raw_input()
		if Cond == "S":
			vector3a = int(vector1a + vector1b)
			vector3b = int(vector2b + vector2b)
			print "El Vector resultante es "
			print vector3a
			print vector3b
	print "Quiere calcular otro vector"
	print "S/N"
	Cond2 = raw_input()
	if Cond2 == "S":
		vectorProporcional()
	else:
		print "Hasta Luego!"
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||
	
vectorProporcional()
