NO TENGO GANAS DE ABRIR UBUNTU PARA HACERLO EN JUPYTER MANIANA LO HAGO



# Prueba todas las combinaciones de algoritmos y calcula el promedio de ellos
# El set de pruebas debe tener una columna por algoritmo con su resultado
# Las columnas deben llamarse resutado_algoritmo

algoritmos = ['KNN', 'Random_Forests', 'Decision_Tree', 'Bagging_Regressor','Perceptron']

def calcular_promedio(lista, set_pruebas):
	set_pruebas.loc[:,'promedio'] = 0
	for i in range(len(lista)):
		columna = 'resultado_' + lista[i]
		set_pruebas.loc[:,'promedio'] = set_pruebas.loc[:,'promedio'] + set_pruebas.loc[:,columna]
	set_pruebas.loc[:,'promedio'] = set_pruebas.loc[:,'promedio'] / len(lista)
	error = ..................
	return error

errores = []
for j in range(len(algoritmos)):
	for k in range(j + 1,len(algoritmos)):
		l = algoritmos[j] + algoritmos[k:]
		error = calcular_promedio(l,set_pruebas)
		errores.append((error,l))
		print("Error = {}, algoritmos = {}".format(error,l))

min_error = float("inf")
min_e = ()
for e in errores:
	if e[0] < min_error:
		min_error = e[0]
		min_e = e[1]
		
print("Menor Error = {}, algoritmos = {}".format(min_error,min_e))
