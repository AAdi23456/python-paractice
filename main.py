
import math


# problem 1
print("Hello World")

# problem 2--
x=8
y="ertu"
z=True
print(type(z))

# problem 3

def func():
    numbers=list(range(1,11))
    print(numbers)
    numbers.append(0)
    print(numbers)
    if 3 in numbers:
        numbers.remove(3)
    print(numbers)
    numbers.sort()
    print(numbers)
func()    

# problem 4

def sumandavg(arr):
    sum=0
    for char in arr:
         sum+=char
    length=len(arr)  
    avg=sum/length 
    return print("sum is:-"+str(sum)+"and avg is:-"+str(avg))
sumandavg([1,2,3,4])

# problem 5

def rev(s):
    revv=""
    for char in s:
        revv=char+revv

    return print(revv)

rev("aadi")

# problem 6--

def countvowels(a):
    vowels=["a","i","e","o","u"]
    count=0
    for char in a:
        if char in vowels:
            count+=1

    return count
print("the no of vowels are:-"+str(countvowels("hello")))

# problem 7--

def checkprimeno(n):
    x=math.floor(math.sqrt(n))
    for i in range(2,x+1):
        
        if n%i==0:
           
            return False
    return True
print(checkprimeno(17))    

# problem 8

def printfact(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return print(x)
printfact(5)

#problem 9

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

print(fibonacci_recursive(5))

# problem 10

def createsq():
    res=[]
    for i in range(1,11):
        res.append(i**2)
    return print(res);
createsq()        
