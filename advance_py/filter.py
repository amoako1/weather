
items=[-1,0,1,2,3,4,5,6,7,8,9]
def filt(i):
   return 0<i<=8
print(list(filter (filt,items)))