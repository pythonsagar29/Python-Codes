a=set([1,1,2,3,5,8,13,21,34,55,89])
b=set([1,2,3,4,5,6,7,8,9,10,11,12,13])
list3=[x for x in set(a) if x in set(b)]
print(list3)