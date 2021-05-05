def main():
	casos = int(input())
	lista=[]
	for i in range(casos):
		a, b = map(int,input().split())
		c = a%b
		c = b-c
		if(c==b):
			lista.append(0)
		else:
			lista.append(c)
	for j in lista:
		print(j)
main()