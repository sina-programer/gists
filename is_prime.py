def is_prime(number):
    # there isn't any negative prime number (one is neither prime or complex)
    if number <= 1:
        return False

    # if be an even number, except 2 (all even numbers are devided by two)
    if (not number % 2) and (number != 2):
        return False

    # examining the divisibility of numbers
    for n in range(3, number//2+1):
        if number % n == 0:
            return False

    return True


if __name__ == "__main__":
	print(f"Prime numbers in range 0-99: {list(filter(is_prime, range(100)))}")
