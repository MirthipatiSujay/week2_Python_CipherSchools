# dictionaries intro
# Q - Why we use dictionaries
# A - Because of limitations of lists, lists are not enough to represent
# real data

# Example
user = ['Harshit',24,['coco','kimi no na wa'],['awakening','fairy tales']]
# this lists contains user name , age , fav movies , fav tunes
# you can do this but this is not a good way to do this 

# Q - what are dictionaries
user = {'name' : 'Harshit','age' : 24}
print(user)
print(type(user))

# Second method to create dictionaries
user1 = dict(name = 'Harshit',age = 24)
print(user1)

# how to access data from dictionary
# Note - There is no indexing because of unordered collection of data
print(user['name'])
print(user['age'])

# Which type of data a dictionary can store?
# anything
# numbers,string,list,dictionaries

user_info = {
    'name' : 'harshit',
    'age' : 24,
    'fav_movies' : ['coco','kimi no na wa']
}
print(user_info['fav_movies'])

# How to add data to empty dictionaries
user_info2 = {}
user_info['name'] = 'mohit'
user_info2['age'] = 19

print(user_info2)