# LPIII_2016
# Autor: JAVIER RIVERA (UNEFA)
# Ver en : http://replit.com/DaSb

# CLASE NODO
class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.sig = None
	
# CLASE LISTA
class Lista:
	
	# CONSTRUCTOR
	def __init__ (self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0
		self.__pos = 0

    # Metodo para insertar al inicio de la lista
	def insertar_inicio (self, valor):
		nodo = Nodo (valor)
		
		nodo.sig = self.__primero
		self.__primero = nodo
		self.__actual = nodo
		if (self.__ultimo == None):
			self.__ultimo = nodo
		
		self.__n = self.__n+1
		self.__pos = 0
		
	# Metodo para insertar al final de la lista
	def insertar_ultimo (self, valor):
		nodo = Nodo(valor)
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
		
	# Metodo para insertar adelanta de la posicion actual de la lista
	def insertar_actual (self, valor):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
		nodo = Nodo(valor)
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
		
		
	# Metodo para mostrar los elementos de la lista 
	def mostrar (self):
		nodo = self.__primero
		for i in range (self.__n):
			print nodo.info,
			nodo=nodo.sig
		print	
	# Metodo para posicionar el actual
	def pos_actual (self , posicion ):
		if (self.__n == 0 or posicion > self.__pos):
			return
		nodo=self.__primero
		for i in range (self.__n):
			if (i==posicion):
				self.__actual=nodo
				return self.__actual.info
			nodo=nodo.sig


	# Metodo para buscar el elemento
	def buscar_elem (self , valor ):
		if (self.__n==0):
			return
		nodo = self.__primero
		for i in range (self.__pos+1):
			if (nodo.info != valor):
				nodo=nodo.sig
			else:
	
				return nodo.info , i 

	# Metodo para elimiar el primero de la lista 
	def eliminar_primero(self):
		if(self.__primero==None):
			return
		nodo=self.__primero
		if (self.__actual == nodo):
			self.__actual == nodo.sig
		self.__primero=nodo.sig
		self.__n = self.__n-1
		self.__pos = self.__pos-1
		del nodo
		if(self.__n==0):
			self.__ultimo=None
			self.__actual=None
	# Metodo para eliminar elementos repetidos
	def elimina_repetido (self):
		if (self.__n==0):
			return
		nodo=self.__primero
		while (nodo.sig!=None and nodo.sig!=None):
			nodo2=nodo
			for i in range (self.__n):
				if (nodo2 == None or nodo2.sig==None):
					break
				if (nodo.info == nodo2.sig.info):
					while True:
						nodo3 = nodo2.sig
						nodo2.sig = nodo2.sig.sig
						del nodo3
						self.__n = self.__n-1
						self.__pos = self.__pos-1
						if (nodo2.sig== None):
							break
						elif(nodo2.sig.info != nodo.info):
							break
				nodo2 = nodo2.sig
			if (nodo.sig != None):
				nodo = nodo.sig	
	#Elemntos repetido de una lista arynsai y antony
	def verificar_elem_repetido(self):
		if (self.__n==0):
			return
		nodo=self.__primero
		for j in range (self.__n-1):
			nodo2=nodo.sig
			for i in range (self.__n-1):
				if (nodo2!=None and nodo!=None):
					if (nodo.info==nodo2.info):
						return True
					nodo2=nodo2.sig
			nodo=nodo.sig
		return False	
	#verifica que la lista sea consecutiva arynsay y antony 
	def verifica_elem_consecutivo(self):
		if (self.__n==0):
			return
		nodo = self.__primero
		nodo2=nodo.sig
		for i in range(self.__n-1):
			if (nodo2!=None and nodo!=None):
					if (nodo.info==nodo2.info-1):
						nodo2=nodo2.sig
						nodo=nodo.sig
					else:
						break
		if (nodo and nodo2 == None):
			return True
		return False
	#Metodo para saber la longitudes de las listas
	def longitud(self): 
		if (self.__n==0):
			return 0
		return self.__n
	#Metodo para verificar las listas vacias
	def lista_vacia(self):
		if (self.__n==0):
			return True
		return False
	#Metodo para pararse al primero de la lista
	def Nprimero(self):
		return self.__primero
	#Metodo para ver si dos listas son iguales
	def verifica_listas_iguales(self, l2):
		if (self.lista_vacia() or l2.lista_vacia()):
			return
		if (self.longitud() != l2.longitud()):
			return
		nodo=self.__primero
		nodo2=l2.Nprimero
		for i in range (self.__n):
			if (nodo.info==nodo2.info):
				nodo=nodo.sig
				nodo2=nodo2.sig
			else:
				break
		if (nodo==None and nodo2==None):
			return True 
		return False 
	#verifica si la lista esta ordenada
	def verifica_lista_ordenada(self):
		if (self.longitud==0):
			return
		nodo=self.__primero
		nodo2=nodo.sig
		if (nodo.info < nodo2.info ) :
			for i in range(self.__n-1):
				if (nodo2!=None and nodo!=None):
					if (nodo.info <= nodo2.info):
						nodo2=nodo2.sig
						nodo=nodo.sig
					else:
						return False
			return True ,"ascedente"
		if (nodo.info >= nodo2.info ):
			for i in range(self.__n-1):
				if (nodo2!=None and nodo!=None):
					if (nodo.info >= nodo2.info):
						nodo2=nodo2.sig
						nodo=nodo.sig
					else:
						return False
			return True , "descendente"
	#Sumae una lista multitipo
	def suma_num(self):
		if (self.lista_vacia()):
			return
		nodo = self.__primero
		suma = 0.0
		while (nodo != None):
			if (type(nodo.info) == int or type(nodo.info) == float):
				suma += nodo.info
			nodo = nodo.sig;
		return suma

	#invertir lista
	def invertir(self):
		if (self.lista_vacia()):
			return
		nodo = self.__ultimo
		cont = 1
		while True:
			nodo2 = self.__primero
			if (nodo2==nodo):
				break
			if (self.__primero.sig == None):
				break
			self.__primero = self.__primero.sig
			self.__actual=self.__primero
			nodo2.sig = nodo.sig
			nodo.sig = nodo2
			if (cont == 1) :
				self.__ultimo = nodo2
				cont = cont + 1
# PRINCIPAL 			

# Crea la lista de elementos
l = Lista()
l2 = Lista()
# Inserta elementos en la lista 
l.insertar_actual('h');
l.insertar_actual(10);
l.insertar_actual("hola");
l.insertar_inicio(5);
l.insertar_actual(3.5);
l.insertar_ultimo(20);
l.insertar_inicio(1);
l2.insertar_actual(1);
l2.insertar_actual(2);
l2.insertar_actual('h');
l2.insertar_actual(4);
l2.insertar_actual(5);

# Muestra los elementos de la lista 
l.mostrar()
# ubica la posicion en
#m=l.verifica_elem_consecutivo()
#print m , "elem con"
l.invertir()
l.mostrar()
#buscar elemento existente
#l.elimina_repetido()
#yinnelydiaz06@gmail.com
