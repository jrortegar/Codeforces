def ordenar(linea):
	arreglo=linea.split("+")
	arreglo.sort()
	linea=""
	for i in range(len(arreglo)):
		linea=linea+arreglo[i]+"+"
	linea=linea[:-1]
	return linea
 
def main():
	a=input()
	print(ordenar(a))		
		
main()