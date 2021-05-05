def dividir(a,b):
	return int (a*b/2)
	
def main():
	cadena=input()
	lista=cadena.split(" ")
	print(dividir(int(lista[0]),int(lista[1])))
 	
main()