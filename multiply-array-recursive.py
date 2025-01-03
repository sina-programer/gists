def multiply_recursive(array: list):
    if len(array) == 1:
        return array.pop()
 
    return array.pop() * multiply_recursive(array)


if __name__ == "__main__":
	print(multiply_recursive([2, 4, 8]))  # 2×4×8=64
	print(multiply_recursive(list(range(1, 5))))  # 4! = 24
