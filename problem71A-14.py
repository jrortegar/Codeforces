def acortar(palabra):
	if len(palabra)>10:
		longitud=len(palabra)-2
		auxiliar=palabra[0]+str(longitud)+palabra[len(palabra)-1]
	else:
		auxiliar=palabra
	return auxiliar
	
def main():
	veces=int(input())
	lista=[]
	lista2=[]
	for i in range(veces):
		lista.append(input())
	for i in range(veces):
		lista2.append(acortar(lista[i]))
	for i in range(veces):
		print(lista2[i])
 
main()