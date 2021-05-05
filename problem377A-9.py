def main():
	n, m = map(int, input().split())
	lista = list(map(int,input().split()))
	lista.sort(reverse=True)
	menor = lista[0]-lista[n-1]
	for i in range((m-n)+1):
		a = lista[i]-lista[(n-1)+i]
		if(a<menor):
			menor=a
	print(menor)	
main()