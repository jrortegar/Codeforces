def main():
	n = int(input())
	lista=[]
	for i in range(n):
		a = int(input())
		if(a%2==0):
			lista.append(int(a/2)-1)
		else:
			lista.append(int(a/2))
	for j in lista:
		print(j)
main()