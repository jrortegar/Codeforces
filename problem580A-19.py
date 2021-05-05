def main():
	n = int(input())
	lista = list(map(int, input().split()))
	cont = 0
	aux = lista[0]
	aux2 = cont
	
	for i in range(n):
		if(lista[i]>=aux):
			cont = cont+1
			aux=lista[i]
			#print(aux)
		else:
			cont = 1
			aux=lista[i]
		if(cont>aux2):
			aux2 = cont
	print(aux2)
    
main()