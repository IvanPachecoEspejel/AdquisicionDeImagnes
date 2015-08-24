strops =  '\n\n********************** Menu de opciones ************************\n'
strops += '1.- Accion Agregar Imagen\n'
strops += '4.- Accion Agregar Imagen de la web\n'
strops += '2.- Accion Agregar Imagenes de un archivo de rutas por Condicion\n'
strops += '3.- Accion Agregar Imagenes de un direcorio por Condicion\n'
strops += '4.- Accion Borrar Imagen\n'
strops += '5.- Accion Borrar Imagenes por Condicion\n'

def getOpcion():
	'''Imprime el menu de opciones y espera la opcion del usuario'''
	print strops;
	while True:
		try:
			op = input('Escoje una opcion: ')
			if(op is not None and op in (1,2,3,4,5)):
				break
			raise Exception("")
		except:
			print("Opcion incorrecta")
			
	return op

def start():
	'''Inicia la interfaz de usuario'''
	while(True):
		op = getOpcion()
		print('Opcion elejida: '+str(op))


if __name__ == '__main__':
	print ('Opcion Elejida: ',getOpcion())
	start()