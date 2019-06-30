def speed(s,birthday):
    tic =''
    if(birthday == True):
        s=s-5
    if(s<=60):
        tic = 'No ticket'
    elif(s>=60 and s<80):
        tic = 'small ticket'
    elif(s>=80):
        tic = 'big ticket'
    return tic
print('enter your speed')
s = int(input())
print('is your birthday 0 for false and 1 for true')
b = int (input())
if(b==0):
    birthday = False
elif(b==1):
    birthday =True
else:
    print ('you entered wrong value by default it is taking false')
    birthday =False
ans = speed(s,birthday)
print(ans)
