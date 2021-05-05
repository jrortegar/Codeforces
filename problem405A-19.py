def main():
	a = int(input())
	lista = list(map(int, input().split()))
	lista.sort()
	print(' '.join([str(x) for x in lista]))
main()