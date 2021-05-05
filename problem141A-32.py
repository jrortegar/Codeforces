def main():
	a = input()
	b = input()
	c = input()
	d = a+b
	sortedd="".join(sorted(d))
	sortedc="".join(sorted(c))
	if(sortedd==sortedc):
		print('YES')
	else:
		print('NO')
        
main()