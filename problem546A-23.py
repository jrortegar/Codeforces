def sumarV(valores):
	suma = 0
	restar = valores[1]
	for i in range(valores[2]):
		suma = suma + (i+1)*valores[0]
	if (suma-restar<=0):
		return 0
	return suma-restar
			
def main():
	lectura = input()
	enteros=[]
	valores = lectura.split(" ")
	for i in valores:
		enteros.append(int(i))
	print(sumarV(enteros))
	
main()