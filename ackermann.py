def ackermann(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(2135)

    print('Ackermann(1, 1):', ackermann(1, 1))  # 3
    print('Ackermann(1, 2):', ackermann(1, 2))  # 4
    print('Ackermann(2, 1):', ackermann(2, 1))  # 5
    print('Ackermann(2, 2):', ackermann(2, 2))  # 7
    print('Ackermann(3, 2):', ackermann(3, 2))  # 29
    print('Ackermann(3, 3):', ackermann(3, 3))  # 61
    print('Ackermann(3, 4):', ackermann(3, 4))  # 125
    print('Ackermann(4, 2):', ackermann(4, 2))  # runs 2132 iterations
