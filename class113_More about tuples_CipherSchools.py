# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed =(1,2,3,4.0)

# for loop and tuple
for i in mixed:
    print(i)
# Note -You can use while loop too

# tuple with one element
nums =(1,)
words = ('word1',)
print(type(nums))
print(type(words))


# tuple without parenthesis
guitars = 'yamaha','baton rogue','taylor'
print(type(guitars))

# tuple unpacking
guitarists = ('Maneli Jamal','Eddie Van Der Meer','Andrew Foy')
guitarists1,guitarists2,guitarists3 =(guitarists)
print(guitarists1)

# lists inside tuples
favourites = ('outhern mangolia',['Tokyo Ghoul Theme','landscape'])
favourites[1].pop()
favourites[1].append("we made it")
print(favourites)

# min(),max,sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))