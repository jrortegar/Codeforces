def main():
	cantidad = int(input())
	cont = 0
	aux=''
	for i in range(cantidad):
		a = input()
		if(a!=aux):
			cont = cont+1
			aux = a
	print(cont)
	