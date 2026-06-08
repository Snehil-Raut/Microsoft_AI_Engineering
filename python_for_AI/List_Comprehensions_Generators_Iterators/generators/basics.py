# Generator helps to save memory
# instead of storing the dataset in one go, Generator allows to visit the data in chunks
# List stores whole data, Generators YIELDS value and stops until next YIELD
# basics of generators

def generator(n):
    count=1
    while(count <=n ):
        yield count
        count += 1

for x in (generator(5)):
    print(x)

# # when large data

def generator(n):
    for i in range(n):
        yield i

gen = generator(100000000)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print("some code")
print("some code")
print("some code")
print("some code")
print("some code")
print("some code")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# 2. Generate squares
def generator(n):
    for i in range(1,n):
        yield i*i

for x in generator(6):
    print(x)


# 4. Convert this list comprehension into generator
# [x*x for x in range(10)]

li = [x*x for x in range(10)]
generator = (x*x for x in range(10))
print(next(generator))
print(next(generator))
print(next(generator))



# Concept	                    Meaning
# yield	                    pauses function
# lazy evaluation	        generate only when needed
# iteration	                values come one-by-one
# memory efficiency	        no giant list storage
# generator object	        iterable but not list