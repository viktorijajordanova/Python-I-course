def fib(n):
    prv = 0
    vtor = 1
    for i in range(0, n):
        if i in (0,1):
            yield i
        else:
            prv, vtor= vtor, prv + vtor
            # prv = vtor
            # vtor = prv + vtor

            yield vtor

s = fib(7)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

