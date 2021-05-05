def main():
	pasos=int(input())
	if (pasos<=5):
		print(1)
	elif (pasos%5==0):
		print(int(pasos/5))
	else:
		print(int(pasos/5)+1)
main()