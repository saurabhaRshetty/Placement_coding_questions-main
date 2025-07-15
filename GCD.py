a=int(input("enter the number:"))
b=int(input("enter the number:"))
while b != 0:
    a, b = b, a % b

print("GCD is:", a)
# This code calculates the GCD (Greatest Common Divisor) of two numbers using the Euclidean algorithm.
# It repeatedly replaces the larger number with the remainder of the division until one of the numbers becomes zero.
# The final value of `a` will be the GCD of the two input numbers.
#b!=0 is the condition to continue the loop until the second number becomes zero.
#a,b = b, a % b is the step that updates the values of `a` and `b` in each iteration
