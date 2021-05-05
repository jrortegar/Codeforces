def main():
	cadena = ('').join(input().split(','))
	cadena = cadena[1:-1]
	cadena=cadena.replace(' ','')
	print(len(set(cadena)))
main()