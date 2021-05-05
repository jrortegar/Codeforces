def main():
	ano = input()
	c = int(ano)+1
	ano = str(c)
	lista=[ano[x] for x in range(len(ano))]
	conjunto = set(lista)
	while(len(conjunto)<4):
		c=c+1
		ano=str(c)
		lista=[ano[x] for x in range(len(ano))]
		conjunto = set(lista)
		
	print(c)
		
main()