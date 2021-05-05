def comparar(a,b):
	a=a.lower()
	b=b.lower()
	if(a==b):
		return 0
	else:
		for i in range(len(a)):
			if (a[i]>b[i]):
				return 1
				break
			elif(a[i]<b[i]):
				return -1
				break
 
def main():
	cadena1=input()
	cadena2=input()
	print(comparar(cadena1,cadena2))
	
main()