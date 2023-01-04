def progression(start=1, n=10, q=3):
    answer = list()
    value = start
    for i in range(n):
        yield value
        value *= q


result = progression(1, 5, 3)
for i in result:
    print(i)
