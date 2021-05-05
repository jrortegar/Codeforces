def main():
	n, k = map(int,input().split())
	
	if(n%2==0):
		if(k>(n/2)):
			#es par
			k = k-(n/2)
			print(int(2*k))
		else:
			print(int(2*k-1))
	
	else:
		if(k>(n+1)/2):
			k = k - ((n+1)/2)
			print(int(2*k))
		else:
			print(int(2*k-1))	
	
main()