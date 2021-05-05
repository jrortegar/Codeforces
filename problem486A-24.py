def main():
	n = int(input())
	a = int(n/2)
	if n%2==1:
		a=a+1
		a=int(-1*a)
	print(a)
    
main()