source = [1, 2, 3, 4, 5]
s_new = []
def recursive_reverse(source):
    if len(source) == 1:
        s_new.append(source[0])
        return
    s_new.append(source[-1])
    return recursive_reverse(source[0:len(source)-1])

recursive_reverse(source)
print(s_new)