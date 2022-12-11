user_info = {
    'name' : 'harshit',
    'age' : 24,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening','fairy tale'],
}
# how to add data
user_info['fav_songs'] = ['songs1','songs2']
print(user_info)

# pop method
popped_item = user_info.pop('fav_tunes')
print(type(popped_item))
print(user_info)

# popitem method
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))