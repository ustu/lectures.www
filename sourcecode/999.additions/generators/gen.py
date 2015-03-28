def idMaker():
    index = 0
    while True:
        yield index
        index += 1

gen = idMaker()

print(next(gen))
print(next(gen))
print(next(gen))
