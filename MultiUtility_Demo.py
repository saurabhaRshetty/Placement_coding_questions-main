header = ["Name", "Age", "Department"]
data = [["Alice", 30, "HR"],
        ["Bob", 25, "Engineering"], 
        ["Charlie", 35, "Marketing"]]
print(f"{header[0]:<10} {header[1]:<5} {header[2]:<15}")
print("*" * 30)
for row in data:
    print(f"{row[0]:<10} {row[1]:<5} {row[2]:<15}")
    print("-" * 30)
# This code checks all 3-digit numbers to see if they meet the conditions:          
# 1. The number itself is prime.
# 2. The sum of its digits is prime.    
# 3. All digits of the number are prime (2, 3, 5, 7).
# It prints all valid 3-digit numbers that satisfy these conditions.    
# This code implements a simple bank management system with functionalities like checking balance, depositing, withdrawing, and transferring money.
# The user can interact with the system by entering their account number and choosing options from a menu   