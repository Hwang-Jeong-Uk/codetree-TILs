r=input()
l=input()
r=float(r)
l=float(l)

if r>=1.0 and l>=1:
    print('High')
elif r>=0.5 and l>=0.5:
    print('Middle')
else:
    print('Low')