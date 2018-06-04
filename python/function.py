def person(name, age, **kw):
    print(kw)

def calc(*numbers):
    print(numbers)
    sum =0
    for n in numbers:
        sum=sum+n*n
    return sum
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
# person('jose', 20, city='beijing', addr='xibwiwang')
# a = [1,2,3,4]
# calc(*a)
print(fact(10))
