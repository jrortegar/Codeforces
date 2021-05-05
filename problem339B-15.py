n, m= map(int, input().split())
lista = list(map(int, input().split()))
cont = 0
for i in range(m):
	if(i==0):
		cont = cont + lista[i]
	else:
		if(lista[i-1]>lista[i]):
			cont = cont+(n-lista[i-1])
			cont = cont+lista[i]
		else:
			cont = cont + (lista[i]-lista[i-1])
print(cont-1)