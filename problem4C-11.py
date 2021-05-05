n = int(input())
 
diccionario={}
lista=[]
 
for i in range(n):
	a = input()
	if (a not in diccionario):
		diccionario[a]=1
		lista.append('OK')
	else:
		lista.append(a+str(diccionario[a]))
		diccionario[a]=diccionario[a]+1		
 
for j in lista:
	print(j)