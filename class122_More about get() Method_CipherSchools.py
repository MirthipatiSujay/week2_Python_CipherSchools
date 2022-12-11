# more about get, two same keys in dictionaries 
user = {'name':'Harshit','age':24,'age':34}
print(user.get('name'))
print(user.get('names'))
print(user.get('fav','not found!'))
print(user.get('age')) # last age will come as output