import io
tup = [9,5,7,5,9,7]
rep = []
for t in tup:
    found = 0
    for r in rep:
        if(r[0]==t):
            r[1]+=1
            found = 1
            break
    if(not found):
        rep.append([t,1])
num = 0
count = 0
for r in rep:
    if(r[1]>count):
        count = r[1]
        num =r[0]
if(count > 1):
    print('repeated number:'+str(num)+'repeat times' + str(count))
else:
    print('no number repeated')
