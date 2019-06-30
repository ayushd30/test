from collections import Counter

dict1={'a':10,'b':25,'c':50}
dict2={'a':20,'b':5,'d':30}

cdict=Counter(dict1)+Counter(dict2)
print(cdict)
