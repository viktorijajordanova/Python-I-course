def SentanceIterator(s):

    p = iter(s.split(" "))
    return p

p = input("Napisi recenica ")
s = SentanceIterator(p)

print(next(s))
print(next(s))
print(next(s))

