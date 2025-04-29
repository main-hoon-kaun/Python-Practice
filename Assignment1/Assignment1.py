a=12
b=5
c='7'
d= True
res=0
if (d) :
    res = (a+b)*int(c)
    print(res)
if res %2 ==0:
    res=res >> 2
    print(res)
if res%2!=0:
    res=res<<1
    print(res)
res=res//(b|a)
print(res)
print(res>=a or res in [10,20,30,40])
