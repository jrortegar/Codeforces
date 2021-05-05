def main():
	n = int(input())
	local = []
	visitante = []
	cont=0
	for i in range(n):
		a, b = map(int, input().split())
		local.append(a)
		visitante.append(b)
	for j in range(n):
		k=j+1
		while(k<len(local)):
			if(local[j]==visitante[k]):
				cont=cont+1
			k=k+1
		l=j+1
		while(l<len(local)):
			if(visitante[j]==local[l]):
				cont=cont+1
			l=l+1
	print(cont)
			
main()