def main():
	cantidad = int(input())
	de100 = int(cantidad/100)
	restante = int(cantidad%100)
	de20 = int(restante/20)
	restante = int(restante%20)
	de10 = int(restante/10)
	restante = int(restante%10)
	de5 = int(restante/5)
	de1 = int(restante%5)
	print(de100+de20+de10+de5+de1)
main()