def main():
	n = int(input())
	lista = list(map(int, input().split()))
	lista2=[]
	for i in range(n):
		lista2.append(0)
	for i in range(n):
		for j in range(n):
			if i+1==lista[j]:
				lista2[i]=j+1
				break
	print(*lista2)
			
main()