s, n=map(int, input().split())
listaA=[]
for i in range(n):
	a,b=(map(int,input().split()))
	c=(a,b)
	listaA.append(c)
listaA.sort()
strength=s
cont=0

for i in range(len(listaA)):
	if(strength>listaA[i][0]):
		strength+=listaA[i][1]
	else:
		cont+=1
if(cont==0):
	print('YES')
else:
	print('NO')