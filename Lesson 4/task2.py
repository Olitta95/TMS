def recursive_max(source):
    if len(source) > 1:
        Max = recursive_max(source[1:])
        if source[0] < Max:
            return Max
        else:
            return source[0]
    if len(source) == 1:
        return source[0]
source = [2, 1, 0, 5, 7, 6, 4, 3]
s_new = recursive_max(source)
print("Максимальное число", s_new)