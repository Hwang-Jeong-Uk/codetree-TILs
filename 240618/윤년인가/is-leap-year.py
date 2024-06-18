y= int(input())

#윤년
if y%4==0:
    if y%100==0 and y%400!=0: #평년
        print('false')
    else:
        print('true')
else: 
    print('false')