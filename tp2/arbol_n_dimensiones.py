import pandas as pd


class Nodo_normal:
	
	def __init__(self,columna, dato):
		self.columna = columna
		self.dato = dato
		self.izq = None
		self.der = None
		
	def es_nodo_hoja(self):
		return False
		
	def get_dato(self):
		return self.dato
		
	def get_columna(self):
		return self.columna
		
	def set_izquierdo(self,nodo):
		self.izq = nodo
		
	def set_derecho(self, nodo):
		self.der = nodo
		
	def get_izquierdo(self):
		return self.izq
		
	def get_derecho(self):
		return self.der
		

class Nodo_hoja:
	
	def __init__(self,dataframe):
		self.dataframe = dataframe
		
	def es_nodo_hoja(self):
		return True
	
	def get_dataframe(self):
		return self.dataframe


class Arbol_n_dimensiones:
	
	def __init__(self, dataframe, columnas):
		self.raiz = crear_nodos(dataframe,columnas,0)
		
	def obtener_dataframe(self, dato):
		return buscar_nodos(self.raiz,dato)
		
		
		
def crear_nodos(dataframe, columnas, i):
	
	minimo_datos_en_hoja = 1500
	
	if (len(dataframe) <= minimo_datos_en_hoja):
		hoja = 	Nodo_hoja(dataframe.reset_index())
		return hoja	
		
	col = columnas[i % len(columnas)]
	promedio = dataframe.loc[:,col].mean()
	nodo = Nodo_normal(col, promedio)
	
	df_izq = dataframe.loc[dataframe[col] <= promedio,:]
	df_der = dataframe.loc[dataframe[col] > promedio, :]
	
	nodo.set_izquierdo(crear_nodos(df_izq, columnas, i+1))
	nodo.set_derecho(crear_nodos(df_der, columnas, i+1))
	
	return nodo
	

def buscar_nodos(nodo_actual, dato):
	if (nodo_actual.es_nodo_hoja()):
		return nodo_actual.get_dataframe()
		
	dato = nodo_actual.get_dato()
	col = nodo_actual.get_columna()
	
	if (dato[col] <= dato):
		return buscar_nodos(nodo_actual.get_izquierdo(), dato)
	return buscar_nodos(nodo_actual.get_derecho(), dato)
		
		
