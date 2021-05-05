def main():
	a, b = map(int, input().split())
	fila = input()
	for i in range(b):
		fila=fila.replace("BG","GB")
	print(fila)
	
 
main()