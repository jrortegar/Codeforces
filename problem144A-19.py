def main():
	a = int(input())
	lista = list(map(int, input().split()))
	maxValor = max(lista)
	minValor = min(lista)
	posMax = lista.index(maxValor)
	posMin = (len(lista)-1)-list(reversed(lista)).index(minValor)
	if(posMax>posMin):
		print(posMax+(len(lista)-1-posMin)-1)
	else:
		print(posMax+(len(lista)-1-posMin))
 
main()