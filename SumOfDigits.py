a = int(input("Enter the number: "))
sum_digits = 0
while a > 0:
    sum_digits += a % 10
    a //= 10
print("Sum of digits:", sum_digits)

# This code calculates the sum of the digits of a given number.
# It repeatedly extracts the last digit using modulo operation and adds it to the sum,
# then removes the last digit by performing integer division by 10 until the number becomes zero
#3+(12%10)= 3+2=5
#4+(12%10)= 4+2=6
#5+(12%10)= 5+2=7
#this 12%10 gives the last digit of the 
# number, and integer division by 10 removes that last digit.
