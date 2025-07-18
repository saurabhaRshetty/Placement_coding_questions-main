num=int(input("Enter any num "))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a    
def cop(a,b):
    return gcd(a,b) == 1

for i in range(1,num):
    for j in range(1,i):
        for k in range(1,j):
            if(j*j + k*k == i*i and cop(i,j) and cop(i,k) and cop(j,k)):
                print(k,j,i)
            