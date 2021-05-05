def main():
	levels = int(input())
	littleX = list(map(int,input().split()))
	littleY = list(map(int,input().split()))
	conj = set(littleX[1:]+littleY[1:])
	if(len(conj)==levels):
		print('I become the guy.')
	else:
		print('Oh, my keyboard!')
main()