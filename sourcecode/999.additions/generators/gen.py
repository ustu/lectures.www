def id_maker():
    index = 0
    while True:
        yield index
        index += 1

gen = id_maker()

print(next(gen))
print(next(gen))
print(next(gen))
