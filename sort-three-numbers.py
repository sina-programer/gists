def sort(a, b, c):
	if a>b:
		a, b = b, a
	if b>c:
		b, c = c, b
	if a>b:
		a, b = b, a
	return a, b, c

if __name__ == "__main__":
	x, y, z = 6, 5, 8
	s = tuple(sorted([x, y, z]))
	assert sort(x, y, z) == s, 'The sorting has problems'
	assert sort(x, z, y) == s, 'The sorting has problems'
	assert sort(y, x, z) == s, 'The sorting has problems'
	assert sort(y, z, x) == s, 'The sorting has problems'
	assert sort(z, y, x) == s, 'The sorting has problems'
	assert sort(z, x, y) == s, 'The sorting has problems'
	print('The sorting worked perfect!')
	print('Sorted Numbers:', *sort(x, y, z))
