1-100之内奇数和
sum=0
x=0
while True:
    x=x+1
    if x>100:
        break
    if x%2==0:
        continue
    sum+=x
    print(sum)


九九乘法表
for x in [1,2,3,4,5,6,7,8,9]:
    l=''
    for y in [1,2,3,4,5,6,7,8,9]:
        if x>y:
            continue
        l=l+(str(x)+'X'+str(y)+'='+str((x*y))+',')
    print(l)


def hhh(l):
    return   '\n'.join([','.join(['%sX%s=%-2s'%(x,y,x*y)for y in range(1,x+1)])for x in range(1,l+1)])
print(hhh(6))

九九乘法表（加逗号）

for x in [1,2,3,4,5,6,7,8,9]:
    l=''
    for y in [1,2,3,4,5,6,7,8,9]:
        if x<y:
            continue
        if x==y:
            l=l+(str(x)+'X'+str(y)+'='+str((x*y)))
        else:
            l=l+(str(x)+'X'+str(y)+'='+str((x*y))+',')
    print(l)




方法二
for x in range(1,10):
    i=''
    for y in range(1,x+1):
        i+=( '%sX%s=%-2s'%(x,y,x*y))
        if x!=y:
            i = i + ','
    print(i)


一行代码：
print( '\n'.join([','.join(['%s+%s=%-2s'%(x,y,x*y)for y in range(1,x+1)])for x in range(1,10)]))


复杂化 big = []
for x in range(1,10):
    small = []
    for y in range(1,x+1):
        small.append( '%sX%s=%-2s'%(x,y,x*y))
    big.append(','.join(small))
print('\n'.join(big))



3的倍数
array = range(3,102,3)
for l in array:
    print(l)



问题(计算range（1,101） 1*1+2*2+....100*100)
方法1：
a=range(1,101)
sum=0
while a<4:
    sum+=a*a
    a=a+1
    print(sum)

方法2：
L = []
x = 1
while x <= 100:
    L.append(x * x)
    x = x + 1
print（sum(L)）