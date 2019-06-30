import random
n=int(input('enter the length of list'))
a=list(map(int,input("\nenter the numbers:" ).strip().split()))[:n]
print(a)
random.shuffle(a)
print('shuffeled list is : ' + str(a))
