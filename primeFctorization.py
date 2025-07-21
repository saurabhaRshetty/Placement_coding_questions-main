#using recursion write program to print prime factorization of a any integer
#write program to print prime factorization of a any integer using recursion
#all the steps explaination
# 1. Define a function `prime_factors` that takes two parameters: `n` (the number to factor) and `i` (the current divisor, starting at 2).
# 2. If `n` is less than or equal to 1, return (base case).
# 3. If `n` is divisible by `i`, print `i` and recursively call `prime_factors` with `n // i` (the quotient) and the same `i`.
# 4. If `n` is not divisible by `i`, recursively call `prime_factors` with `n` and `i + 1` (the next potential divisor).
# 5. Read an integer `n` from user input.
# 6. Call the `prime_factors` function with `n` to start the factorization process.
# 7. The function will print the prime factors of `n` in ascending order as it finds them.
def prime_factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            print(i, end=" ")
            prime_factors(n // i)
            break  # Ensure we only factor once per prime factor        
n = int(input("Enter a number: "))
prime_factors(n)  # Call the function to start the factorization process


#explain again
#
# Output the prime factors of n



