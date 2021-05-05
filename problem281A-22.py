def capitalizar(linea):
	a=linea[:1]
	b=linea[1:]
	a=a.upper()	
	return a+b
 
def main():
	a=input()
	print(capitalizar(a))
			
main()