a=int(input("enter the number:"))
c=0
for i in range(2,a):
    if(a%i==0):
        c=c+1
if(c==0):
    print("prime")
else:
    print("composite")
    # This code checks if a number is prime or composite.
    # It initializes a counter `c` to 0, then iterates from 2 to `a-1`.
    # If `a` is divisible by any number in this range, it increments `c`.
    # If `c` remains 0 after the loop, `a` is prime; otherwise, it is composite.