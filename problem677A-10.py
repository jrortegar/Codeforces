def main():
	n, h = map(int, input().split())
	hs = list(map(int, input().split()))
	cont = 0
	for i in hs:
		if i>h:
			cont = cont+2
		else:
			cont = cont+1
	print(cont)
main()