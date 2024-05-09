def has_unique_characters(data):
    data_set = set(data)
    return len(data_set) == len(data)
    
    
print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
