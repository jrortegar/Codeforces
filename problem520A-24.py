def main():
	nmi = int(input())
	a=input()
	a=a.lower()
	if(len(set(a))<26):
		print('NO')
	else:
		print('YES')
main()