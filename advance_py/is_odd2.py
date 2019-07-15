
words=['hello','world']
def join_string(strings):
    return reduce(lambda x,y:x + ' ' + y,strings)
print(join_string(words))