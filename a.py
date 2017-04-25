'''# L=[95.5,85,59]
# print(L[-1])
# print(L[-4])'''
'''l=['adam','lisa','mobi']
l.append('paul')
print(l)
l.insert(2,'lance')
print(l)
l.pop()
print(l)
l.pop(-3)
print(l)'''
'''t=(0,1,2,3,4,5,6,7,8,9)
print(t)
b=(1,)
print(b)
a=('adam',)
print(a)
u=('c','h',['C','H'])
i=u[2]
i[0]='c'
i[1]='h'
print(u)'''
'''# score=75
# if score>=60:
#     print('passed')
# else:
#     print('failed')
# age=20
# if 18>age>=6:
#     print('teen')
# elif age>=18:
#     print('adult')
# else:
#     print('baby')
score=85
if score>=90:
    print('excellent')
elif 90>score>=80:
    print('goood')
elif 80>score>=60:
    print('passed')
else:
    print('failed')'''
'''# l=['lisa','adam','mona']
# for name in l:
#     print(name)
# s=[75,81,92,48]
# sum=0.0
# for score in s:
#     sum+=score
# print(sum/4)
# sum=0
# x=1
# while x<100:
#     sum+=x
#     x=x+2
# print(sum)'''
'''sum=0.0
x=1
n=1
while True:
    sum+=x
    n=n+1
    x=x*2
    if n>20:
        break
print(sum)'''
# l=[90,85,64,87,70,68,53,32,46,57]
# for score in l:
#     sum=0
#     sum+=score
# print(sum)
'''l=[90,85,64,87,70,68,53,32,46,57]
sum=0
for score in l:
    sum+=score
print(sum)'''
# sum=0
# x=1
# while True:
#     sum+=x
#     x=x+1
#     if x>4:
#         print('x>4:',x)
#         continue
#     if x>8:
#         break
#         print('x>8:',x)
#     print(x)
# print(sum)
'''d={'adam':95,'lisa':85,'bart':59}
d.insert[2,,'paul':75]
print(d)'''
'''d={'adam':95,'lisa':85,'bart':59}
 d['paul']=73
 print(d)
 print(d['adam'])
 if 'adam' in d:
    print(d['adam'])
 if 'mona'in d:
     print(d['mona'])
d={95:'lisa',85:'adam',59:'bart'}
print(d[85])
print(d[0])
for l in d :
    print(l,',',d[l])'''
# sum=0
# x=0
# while True:
#     x=x+1
#     if x>100:
#         break
#     if x%2==0:
#         continue
#     sum+=x
#     print(sum)
# for x in  [0,1,2,3,4,5,6,7,8,9]:
#     for y in [1,2,3,4,5,6,7,8,9]:
#         if x<=y:
#             continue
#         print(10*y+x)

# for x in [1,2,3,4,5,6,7,8,9]:
#     l=''
#     for y in [1,2,3,4,5,6,7,8,9]:
#         if x<y:
#             continue
#         l=l+(str(x)+'X'+str(y)+'='+str((x*y)))
#         if x>y:
#             l=l+','
#     print(l)
# array = range(3,102,3)
# for l in array:
#     print(l)
# # print(array[::3])

# for x in range(1,10):
#     l=''
#     for y in range(1,10):
#         if x>y:
#             continue
#         l += str(x) + 'X' + str(y) + '=' + str(x * y) + ','
#     print(l)
#
# print( '\n'.join([','.join(['%s+%s=%-2s'%(x,y,x*y)for y in range(1,x+1)])for x in range(1,10)]))
# big = []
# for x in range(1,10):
#     small = []
#     for y in range(1,x+1):
#         small.append( '%sX%s=%-2s'%(x,y,x*y))
#     big.append(','.join(small))
# print('\n'.join(big))
# #
# s=set(['A','B','C','D'])
# print(s)
# print(len(s))

# s=set(['Adam','Lisa','Bart','Paul'])
# print('adam' in s)

# L = []
# x = 1
# while x <= 100:
#     L.append(x * x)
#     x = x + 1
# print(sum(L))

# sum=0
# for i in range(1,101):
#     sum+=(i*i)
# print(sum)
# temp = []
# for i in range(1,101):
#     temp.append(i*i)
# print(sum(temp))

# print('\n'.join([','.join(['%sX%s=%-2s'%(x,y,x*y)for y in range (1,x+1)])for x in range(1,10)]))
# print( '\n'.join([','.join(['%s+%s=%-2s'%(x,y,x*y)for y in range(1,x+1)])for x in range(1,10)]))

# a=["LI",'niu','lin']
# print('ma'.join(a))
'''s=set(['adam','lisa'])
s.add('paul')
s.remove('adam')
print(s)'''
# def abs(a):
#     if a >= 0:
#         return a
    # else:
    #     return -a
# print(abs(-3))

# import  math
# def hhh(a,b,c):
#     hhh=-b+math.sqrt([b-a*c])
#     return(x)
# print(hhh(3,4,5))




# import math
# def quadratic_equation(a, b, c):
#     t = math.sqrt(b * b - 4 * a * c)
#     return (-b + t) / (2 * a),( -b - t )/ (2 * a)
# print (quadratic_equation(2, 3, 0))
# print (quadratic_equation(1, -6, 5))
# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
# print(fact(3))
# def aquare_of_sum(n):
#     for a in n:
#

# def square_of_sum(l):
#     return sum([(a*a)for a in l])
# print(square_of_sum([1,2,3,4,5,]))



# a=['la','ha','ma']
# b = {'aaa':'sss','bb':'hhh'}
# c = 'aaaaaaaaa'
# print(a)
# print(b)
# print()

# def hhh(l):
#     return   '\n'.join([','.join(['%sX%s=%-2s'%(x,y,x*y)for y in range(1,x+1)])for x in range(1,l+1)])
# print(hhh(6))

# def hhh(l):
#     for x in range(1,l+1) :
#         a=''
#         for y in range(1,x+1) :
#             a=a+(str(x)+'X'+str(y)+'='+str(x*y)+',')
#         print(a)
# hhh(6)

# for x in [1,2,3,4,5,6] :
#     a=''
#     for y in (1,2,3,4,5,6) :
#         if x<y:
#             continue
#         else:
#             a=a+(str(x)+'X'+str(y)+'='+str(x*y)+',')
#     print(a)

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(4))

# def move(n, a, b, c):
#     if n ==1:
#         print(a, '-->', c)
#         return
#     move(n-1, a, c, b)
#     print(a, '-->', c)
#     move(n-1, b, a, c)
# print(move(4, 'A', 'B', 'C'))

# def power(x,n):
#     if n==0:
#         return 1
#     return x*(power(x,n-1))
# print(power(4,3))

# x=10
# n=2
# for i in range(1,n):
#     x*=x
# print(x)

# def power(x,n):
#     s=1
#     while n > 0:
#         n=n-1
#         s=s*x
#     return s
# print(power(4,3))

# def greet(aaa,ooo="world"):
#     if aaa=='':
#         return 'hello,'+ooo
#     return 'hello,'+aaa
# print(greet())

# def greet(name='world'):
#     print('Hello, ' + name + '.')
# greet()
# greet('Bart')


# def aaa(*args):
#     return args
# print(aaa('haha'))

# def average(*args):
#     return args
# print(average(1,2,3,4))

# l=['adam','lisa','bart']
# print(l[:2])

# a=range(1,101)
# print(a[2::3])
# print(a[0:10])
# print(a[0:50][0::5])

# print('\n'.join(','.join(('%sX%s=%-2s'%(x,y,x*y))for y in range(1,x+1))for x in range(1,10)))

# h=range(1,101)
# print(h[90:100])
# print(h[-10:])


# a='ASDFGHJKL'
# print(a[:4])

# def firstupper(s):
#     return s[0].upper()+s[1:]
# print(firstupper('hello'))

# for i in range(1,101):
#     if i%7==0:
# print(i)

# def s(l):
#     return [x.upper() for x in l if isinstance(x,str)]
# print(s(['hello','world']))

# print([(l+''+y+''+t)for l in range(1,10) for y in range(0,10)for t in range(0,10)if l ==t])
# print([100*a+10*b+c for a in range(1,10) for b in range (0,10)for c in range(0,10)if a ==c ])


# def a(x):
#     return x*x
# print(list(map(a,[1,2,3,4])))

# from functools import reduce
#
# def f(x,y):
#     return x+y
# print(reduce(f,[1,3,5,7,9]))

# from functools import reduce
# def f(x,y):
#     return x*y
# print(reduce(f,[2,4,5,7,12]))

# def is_odd(x):
#     return x%2==1
# temp = list(filter(is_odd,[1,2,3,4,5,6]))
# print(temp)

# d={'Adam':95,'Lisa':85,'Bart':59}
# tds=['<tr><td>%s</td><td>%s</td></tr>'%(name,score)for name,score in d.items()]
# print('<table>')
# print('<tr><th>Name</th><th>Score</th><tr>')
# print('\n'.join(tds))
# print('</table>')

# import math
# def add(x,y,f):
#     return f(x)+f(y)
# print(add




# x 是一个函数，用于过滤l的数据，当返回true时，则保留数据，否则过滤掉
# l 是一个list
# def liqiang(x,l):
#     result=[]
#     for i in l :
#         if x(i):
#             result.append(i)
#     return result
#
# print(sorted(liqiang(lambda x:x%2==1,[1,5,4,3,6,7])))

# def wenzel(x,l):
#     a=[]
#     for i in l:
#         a.append(x(i))
#     return a
# print(wenzel(lambda x:x*x,range(1,5)))
#
# from math import pow,sin,log
# print(pow(2,10))

# try:
#     from sSringIO import StingIO
# except ImportError:
#     from StringIO import StringIO

# 7
# print('猜我想的数字')
# a=input('请输入')
# a=True
# while a!='8':
#     a=input('请输入')
# else:
#     print('结束')

# print('猜数字')
# while True:
#     a=input('输入数字：')
#     if a == '8':
#         break
# print('恭喜你猜对了，数字是8')

# class Person(object):
#     pass
# xiaoming=Person()

# class Person(object):
#     pass
# xiaoming = Person()
# xiaohong = Person()
# print(xiaoming)
# print(xiaohong)
# print(xiaoming == xiaohong)

