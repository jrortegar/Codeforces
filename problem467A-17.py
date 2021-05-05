def main():
	n = int(input())
	cont=0
	for i in range(n):
		pi, cui = map(int, input().split())
		if(pi+2<=cui):
			cont=cont+1
	print(cont) 
main()