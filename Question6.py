import functools
list=[1,2,3,4]
def summ(list):
    sum = 0
    for num in range(0,len(list)):
        sum = sum+list[num]
    print(sum)
    return
def mul(list):
    multi =functools.reduce(lambda x,y :x*y , list)
    print(multi)
    return
mul(list)
summ(list)
