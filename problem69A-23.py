def main():
	vectores=int(input())
	sumax=0
	sumay=0
	sumaz=0
	for i in range(vectores):
		a=input().split(" ")
		sumax=sumax+int(a[0])
		sumay=sumay+int(a[1])
		sumaz=sumaz+int(a[2])
	if(sumax==0 and sumay==0 and sumaz==0):
		print('YES')
	else:
		print('NO')
main()