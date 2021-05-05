def detectar(cantidad,linea):
	cont=0
	for i in range(cantidad):
		if(i<cantidad-1):
			if(linea[i]==linea[i+1]):
				cont=cont+1
	if(cont==cantidad-2 and linea[0]==linea[cantidad-1]):
		cont=cont+1
	return cont		
 
def main():
	lon=int(input())
	a=input()
	print(detectar(lon,a))		
		
main()