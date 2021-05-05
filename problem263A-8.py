def centro(matriz):
	posFila=0
	posCol=0
	for i in range(5):
		for j in range(5):
			if (matriz[i][j]=='1'):
				posFila=i
				posCol=j
				break
	posiciones=abs(posFila-2)+abs(posCol-2)
	return posiciones
			
def main():
	lista=[]
	for i in range(5):
		lista.append(input().split(" "))
	print(centro(lista))
				
main()