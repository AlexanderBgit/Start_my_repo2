""" Замикання версія 1
- автоперевірку не проходить
- не обмежене 1000 ітерацій
"""  
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def fib_closure(n):
    f = fib()
    for i in range(2, n + 1):
        num = next(f)
    return num

""" Замикання версія 2
- автоперевірку проходить
- має обмеження до 1000 ітерацій
""" 
def caching_fibonacci():
    cache = {}

    def fibonacci3(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            result = fibonacci3(n-1) + fibonacci3(n-2)
            cache[n] = result
            return result

    return fibonacci3

fib_cach = caching_fibonacci()


n = 10000
print(fib_closure(n+2)) 
print(fib_cach(n))

import timeit
print(timeit.timeit(lambda: fib_closure(n), number=1)*1000) #час у мілісекундах
print(timeit.timeit(lambda: fib_cach(n), number=1)*1000) #час у мілісекундах

