a=10
for i in range (50):
    if(i%2==0 or i%3==0 or i%5==0 or i%7==0):
        continue
    print("hi")
    a=a+2
print(a)
# This code initializes a variable `a` to 10, then iterates through numbers from 0 to 49.
# If the number is divisible by 2, 3, 5, or 7, it skips the rest of the loop for that iteration.
# For all other numbers, it prints "hi" and increments `a` by 2. 
# The final value of `a` will depend on how many numbers were not skipped. 
# The loop runs 50 times, but only a subset of those will increment `a`.
#it will add 2 as  12 times, so the final value of `a` will be 34 (10 + 2*12)
