n, l = map(int, input().split())
lista = list(map(int, input().split()))
lista.sort()
#Creo ke hay ke tener en cuenta si empieza en cero o no
#empieza en cero
disMin=0
if len(lista)==1:
	if(lista[0]==0):
		disMin=l
	else:
		if(l-lista[0]>lista[0]):
			disMin=l-lista[0]
		else:
			disMin=lista[0]
else:
	if(lista[0]==0):
		disMin=lista[1]/2
		for i in range(1,len(lista)):
			if lista[i-1]+disMin*2<lista[i]:
				disMin=(lista[i]-lista[i-1])/2
		if(disMin+lista[-1]<l):
			disMin=l-lista[-1]

	else:
		disMin=lista[0]
		for i in range(1,len(lista)):
			if lista[i-1]+disMin*2<lista[i]:
				disMin=(lista[i]-lista[i-1])/2
		if(disMin+lista[-1]<l):
			disMin=l-lista[-1]

print(format(disMin, '.10f'))