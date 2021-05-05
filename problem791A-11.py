def comparar(a,b):
	cont=0
	while(a<=b):
		a = a*3
		b = b*2
		cont=cont+1
	return cont
 
def main():
	lectura = input().split(" ")
	limak = int(lectura[0])
	bob = int(lectura[1])
	print(comparar(limak,bob))
	
main()