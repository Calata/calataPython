from sys import argv 
print "nombra el archivo"
filename = raw_input()+".txt"
print "Creando el Archivo %r"%filename

file = open(filename,"w")
file.write("Este es un archivo generado con python")
file.close()

print "terminado"