def sum(n):
    return n*(n+1)/2
#Space Complexity: 0(1), Auxsillary Space = 0(1), Linear space:
def arraysum(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum
b = [1,2,1,2]
print(arraysum(b))
# With the size of the array, the space increases...
#Space Complexity 0(n), Auxsillary Space: 0(1)
def summ(n):
    if(n<=0):
        return
    return n + summ(n-1)

