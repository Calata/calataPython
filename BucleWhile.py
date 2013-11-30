contador = 0
while(contador < 20):
	contador += 1
	print "El contador es igual a %d"%contador
contador = 0

while contador > -1 :
	print "El contador es igual a %d"%contador
	contador += 1

	if contador == 5:
		print "Write EXIT to finish the cicle"
		
		salir = raw_input()
		if(salir == "EXIT"):
			break;
print "You finished all the cicles WELL DONE!"