"""
# 1-100之内奇数和
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
"""


"""
# 九九乘法表
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

# 九九乘法表（逗号）

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




# 方法二
for x in range(1,10):
    i=''
    for y in range(1,x+1):
        i+=( '%sX%s=%-2s'%(x,y,x*y))
        if x!=y:
            i = i + ','
    print(i)


# 一行代码：
print( '\n'.join([','.join(['%s+%s=%-2s'%(x,y,x*y)for y in range(1,x+1)])for x in range(1,10)]))

# 复杂化
big = []
for x in range(1,10):
    small = []
    for y in range(1,x+1):
        small.append('%sX%s=%-2s'%(x,y,x*y))
    big.append(','.join(small))
print('\n'.join(big))

"""

"""
# 还是小九九
# 原始
def table(max=9):
    n = 1
    while n <= max:
        h = ['%sX%s=%s' % (i, n, i*n)for i in range(1, n+1)]
        n += 1
        print(h)
table()

# 改进
def table2(max=9):
    n =1
    l = []
    while n <= max:
        N = ['{}X{}={}'.format(i, n ,i*n)for i in range(1, n+1)]
        l.append(N)
        n += 1
    return l
T = table2()
for t in T:
    print(t)

# 生成器
def table3(max=9):
    n = 1
    while n <= max:
        N = ['{}X{}={}'.format(i, n, i*n)for i in range(1, n+1)]
        n += 1
        yield N
T = table3()
for t in T:
    print(t)
"""

"""
# 3的倍数
array = range(3,102,3)
for l in array:
    print(l)
"""


"""
# 问题(计算range（1,101） 1*1+2*2+....100*100)
# 方法1：
num=0
for a in range(1,101):
    num += a*a
    a=a+1
print(num)

# 方法2：
L = []
x = 1
while x <= 100:
    L.append(x * x)
    x = x + 1
print(sum(L))
"""

"""
# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    l = []
    for i in range(max):
        l.append(b)
        a, b = b, a + b
        yield l
for d in fib(3):
    print(d)
"""


"""
# 杨辉三角
def yanghui(max):
    N = [1]
    n = 0
    while n < max:
        yield N
        N.append(0)
        N = [N[i-1]+N[i]for i in range(len(N))]
        n += 1
for t in yanghui(5):
    print(t)
"""


