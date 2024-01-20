def test():
    print(' I am a function\n')

def test():
    print(' I am a function again....\n')

def test2():
    print(' I am a function again and again....\n')

#test()
#test2()
    
def addNum(a,b):
    return a+b

print('the sum is ',addNum(11,34))

def calc(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e


p,q,r=calc(12,34)

print(p,q,r)

x=calc(10,2)

print(x,type(x))

for i in x:
    print(i)


def data():
    return "a",12.34,True


e=data()


print(e,type(e))

t,y,u=data()

print(t,y,u)


print('---------------------')

# positional argument
# keyword argument
# default argument
# variable length argument

def caller(a,b,c,d):
    return a,b,c,d

a,b,c,d=caller(1,2,3,4)
print(a,b,c,d)

a,b,c,d=caller(d='amitava',b=100,a=False,c=9.8)

print(a,b,c,d)

def whatprice(name,address,price=1000,company='flipkart'):
    print(name,address,price)

whatprice('amitava','kolkata')

whatprice('amitava','kolkata',4000)


def callme(*n):
    print(n)


callme()

callme(22)

callme(1,2,3,4,5,5,6,True)


def g1(a):
    print(a)

def g2(a):
    print(a)

g1(10)
g2(12)


name="Amitava"

def g11():
    print(name)


def g12():
    print(name)

g11()
g12()

def g13():
    global name
    name="Prasasti"
    print(name)

def g14():
    print(name)

g13()
g14()



def square(x):
    return x*x

w=lambda p: p*p # LAMBDA or anonymous function

print(w(12))





















