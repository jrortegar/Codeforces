def main():
	cantidad = int(input())
	valores = list(map(int,input().split()))
	valores.sort(reverse=True)
	yo=[]
	sumYo = sum(yo)
	sumValores = sum(valores)
	while(sumValores>=sumYo):
		yo.append(valores.pop(0))
		sumYo=sum(yo)
		sumValores=sum(valores)
	print(len(yo))
	
		
main()