def main():
	cadena = input()
	probar = input()
	inversa = cadena[-1::-1]
	if (probar==inversa):
		print('YES')
	else:
		print('NO')
		
main()