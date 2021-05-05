def main():
	arreglo = input().split(" ")
	a = int(arreglo[0])
	b = int(arreglo[1])
	for i in range(b):
		if(a%10==0):
			a = a/10
		else:
			a=a-1
	print(int(a))
	
main()