def main():
	a = "I hate"
	b = "I love"
	t = " that " 
	c = " it"
	n = int(input())
	f=""
	for i in range(n):
		if(i%2==0):
			f=f+a
		else:
			f=f+b
		if(i==n-1):
			f=f+c
		else:
			f=f+t
	print(f)
    
main()