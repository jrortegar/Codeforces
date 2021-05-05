def main():
	a = input()
	bandera = False
	if(a==a.upper()):
		a=a.lower()
		bandera = True
	if(a[1:]==a[1:].upper() and a[:1]==a[:1].lower() and bandera==False):
		a = a[:1].upper()+a[1:].lower()
	print(a)
	
main()