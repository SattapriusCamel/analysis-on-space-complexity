def sum(n):
    return n*(n+1)/2

def arraysum(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum
b = [1,2,1,2]
print(arraysum(b))
def summ(n):
    if(n<=0):
        return
    return n + summ(n-1)

