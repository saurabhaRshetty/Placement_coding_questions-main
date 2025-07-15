a = 4
b = 3

greater = max(a, b)

while True:
    if greater % a == 0 and greater % b == 0:
        lcm = greater
        break
    greater += 1

print("LCM is:", lcm)
# This code calculates the LCM (Least Common Multiple) of two numbers using a while loop.
#if greater % a == 0 and greater % b == 0 means to check if the current greater number is divisible by both `a` and `b`.
#then lcm = greater assigns the value of `greater` to `lcm` when the condition is met.
#greater += 1 increments the `greater` number by 1 to check the next possible LCM