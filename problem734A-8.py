def main():
	cantidad = int(input())
	juegos = input()
	a=juegos.count("A")
	d=juegos.count("D")
	if(a==d):
		print('Friendship')
	elif(a>d):
		print('Anton')
	else:
		print('Danik')	
		
main()