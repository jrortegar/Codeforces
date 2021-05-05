def main():
	k = int(input())
	l = int(input())
	m = int(input())
	n = int(input())
	d = int(input())
	cont=0
	for i in range(d):
		if((i+1)%k!=0):
			if((i+1)%l!=0):
				if((i+1)%m!=0):
					if((i+1)%n!=0):
						cont=cont+1
	print(d-cont)
    
main()