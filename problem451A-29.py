a, b= map(int, input().split())
if(b<a):
	menor=b
else:
	menor=a
if(menor%2==0):
	print('Malvika')
else:
	print('Akshat')