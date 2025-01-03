def diagonal(matrix):
    return [line[i] for i, line in enumerate(matrix)]

def constant_matrix(m, n, fill=0):
    return [[fill for j in range(n)] for i in range(m)]

def transpose(matrix):
    return [[line[i] for line in matrix] for i in range(len(matrix))]

def magic_matrix(n):
    matrix = constant_matrix(n, n, fill=0)
    num = 1
    i = 0
    j = len(matrix) // 2

    while True:
        # keep in matrix size
        i %= n
        j %= n

        if matrix[i][j]:  # not equal to zero
            j += 1
            i += 2
        else:
            matrix[i][j] = num
            num += 1
            i -= 1
            j -= 1

        if num == (n**2 + 1):
            break

    return matrix


if __name__ == "__main__":
	n = int(input('Enter dimension of matrix: '))
	matrix = magic_matrix(n)
	matrix_t = transpose(matrix)
	main_diameter = diagonal(matrix[::-1])[::-1]
	secondary_diameter = diagonal(matrix)

	from pprint import pprint
	pprint(matrix)

	print(f'\Main Diameter: {main_diameter}')
	print(f'Secondary Diameter :{secondary_diameter}')
	print(f'\nSum Rows: {[sum(line) for line in matrix]}')
	print(f'Sum Cols: {[sum(line) for line in matrix_t]}')
	print(f'Sum Main Diameter: {sum(main_diameter)}')
	print(f'Sum Secondary Diameter: {sum(secondary_diameter)}')
