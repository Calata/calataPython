def crear(finalfile):
	Arch = open(finalfile,"w")
	print "se ha creado el archivo"

def escribir(finalfile):
	print "Escriba su mensaje"
	Mensaje = raw_input()
	Arch = open(finalfile,"a")
	Arch.write(Mensaje)
	#Arch.write('Linea 2\n')
	Arch.close
	print "se ha escrito el archivo"
def leer(finalfile):
	Arch = open(finalfile)
	Mensaje = Arch.readline()
	while Mensaje != "":
		print Mensaje
		Mensaje = Arch.readline()
	Arch.close()
	print "se ha leido el archivo"
#Pedimos los Datos 
print "Introduce nombre del archivo"
filename = raw_input()
print "Introduce el formato del archivo (Ejemplo .txt)"
fileformat = raw_input()
finalfile = filename+fileformat
#LLamamos a los metodos
crear(finalfile)
escribir(finalfile)
leer(finalfile)