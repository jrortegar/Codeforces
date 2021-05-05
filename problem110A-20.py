def main():
	w=input()
	cuatros=w.count("4")
	sietes=w.count("7")
	tot=cuatros+sietes
	lista=[]
	while(tot!=0):
		lista.append(tot%10)
		tot=int(tot/10)
	con=set(lista)
	if(len(con)>2):
		print("NO")
	elif(len(con)==2 and 4 in con and 7 in con):
		print("YES")
	elif(len(con)==1):
		if(4 in con or 7 in con):
			print("YES")
		else:
			print("NO")
	else:
		print("NO")
		
main()