def main():
	paradas = int(input())
	lista = []
	for i in range(paradas):
		a = input().split(" ")
		lista.append(int(a[0]))
		lista.append(int(a[1]))
	mayor = 0
	cuenta = 0
	for i in range(len(lista)):
		if(i%2==0):
			cuenta = cuenta - lista[i]
		else:
			cuenta = cuenta + lista[i]
		if(i%2==1):
			if(cuenta>mayor):
				mayor = cuenta
	print(mayor)

main()