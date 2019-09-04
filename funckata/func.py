def add(n1, n2):
    n3 = 0
    n3 = n1 + n2
    return n3
add(2, 4)

def multiply(n1, n2):
    var1 = 0
    for i in range (1, n2 + 1):
        var1 = add(var1, n1)
    return var1
multiply(6,8)

    


def factorial(n):
        sum = 1
        for i in range(1, n + 1):
               sum = multiply(i,sum)  
        return sum      

factorial(4)

def fibonacci(n):
        a = 0
        b = 1
        if n < 0:
                result = "whaaaaat"
        elif n == 0:
                a = 0
                result = 0
        elif n == 1:
                b = 1
                result = 1
        else:
                for i in range(2,n):
                        c = add(a,b)
                        a = b
                        b = c
        return c




print(add(2,4))
print(multiply(6,8))
print(factorial(4))
print(fibonacci(8))