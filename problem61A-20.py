def main():
	a = input()
	b = input()
	c = ['1' if a[i]!=b[i] else '0' for i in range(len(a))]	
	print(''.join(c))
main()