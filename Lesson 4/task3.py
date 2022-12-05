def recursive_flat(source):
    if source == []:
        return source
    if isinstance(source[0], list):
        return(recursive_flat(source[0]) + recursive_flat(source[1:]))
    return (source[:1] + recursive_flat(source[1:]))
source = [[2, 1], [0, 5, [7, 6]], [4, 3]]
s_new = recursive_flat(source)
print("Выпрямленный список", s_new)


