
numbers = [1,56,234,87,4,76,24,69,90,135]
def is_odd(x):
         return x%2!= 0
        
print (list(filter(is_odd,numbers)))
print (list(map(is_odd,numbers)))

print(list(filter (lambda x: x % 2!= 0,numbers)))