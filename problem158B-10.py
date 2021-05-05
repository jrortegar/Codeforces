def main():
	n = int(input())
	lista = list(map(int,input().split()))
	lista.sort(reverse=True)
	j = n-1
	cont = 0
	i = 0
	while i<=j:
		cont+=1
		four = 4-lista[i]
		while lista[j]<=four and j>=i:
			four-=lista[j]
			j-=1
		i+=1
	print(cont)
    
main()