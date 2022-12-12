def decor(func):
     def inner(*args, **kwargs):
         result = func(*args, **kwargs)
         return result
     return inner
@decor
def create_list(count: int):
     result = []
     for i in range(1, count+1):
         if i%2==0:
             print(i)
     return result
result = create_list(200)
