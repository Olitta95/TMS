
bytes = b'r\xc3\xa9sum\xc3\xa9'
result = bytes.decode("utf-8")
print(result)                        # вариант1

print(str(bytes, "utf-8"))           #вариант2

result2 = result.encode("Latin1")
print(result2)

result3 = result2.decode("latin1")
print(result3)
print(str(result2, "latin1"))

