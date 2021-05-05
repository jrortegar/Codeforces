def main():
	n = int(input())
	lista = []
	cont = 0
	for i in range(n):
		lista.append(input())
	a = lista.count('Tetrahedron')
	b = lista.count('Cube')
	c = lista.count('Octahedron')
	d = lista.count('Dodecahedron')
	e = lista.count('Icosahedron')
	print(int(a*4+b*6+c*8+d*12+e*20))
    
main()