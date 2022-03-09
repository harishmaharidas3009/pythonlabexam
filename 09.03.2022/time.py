class time:
    def __init__(self,h,m,s):
        self._h1=h
        self._m1=m
        self._s1=s
    def __add__(self,x):
        sum1=self._h1+x.h1
        sum2=self._m1+x.m1
        sum3=self._s1+x.s1
        if sum3>=60:
            sum3=sum3-60
            sum2=sum2+1
        if sum2>=60:
            sum2=sum2-60
            sum1=sum1+1
print("Time 1")
h1=int(input("Enter hour:"))
m1=int(input("Enter minute:"))
s1=int(input("Enter seconds:"))
obj1=time(h1,m1,s1)
print("Time2")
h2=int(input("Enter second hr:"))
m2=int(input("enter second minute:"))
s2=int(input("Enter 2nd seconds:"))
obj3=time(h2,m2,s2)
obj1+obj3
print("sum is:",obj1+obj3)


