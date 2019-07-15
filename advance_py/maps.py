import math 

def ar(r):
    a= math.pi*r*r
    return a
ased = [1,2,3]
print(list(map(ar,ased)))


items=[-1,0,1]
def filt(i):
   return i>0
filter (filt,items)