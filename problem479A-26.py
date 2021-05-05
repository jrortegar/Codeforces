def main():
	a = int(input())
	b = int(input())
	c = int(input())
	mayor=a+b+c
	if(mayor<a+b*c):
		mayor=a+b*c
	if(mayor<(a+b)*c):
		mayor=(a+b)*c
	if(mayor<a*b+c):
		mayor=a*b+c
	if(mayor<a*(b+c)):
		mayor=a*(b+c)
	if(mayor<a*b*c):
		mayor=a*b*c
	print(mayor)
    
main()