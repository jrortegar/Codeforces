def main():
	a='hello'
	b=input()
	c=''
	for i in range(len(a)):
		for j in range(len(b)):
			if(a[i]==b[j]):
				c=c+a[i]
				b=b[j+1:]
				break
	if(c==a):
		print('YES')
	else:		
		print('NO')

main()