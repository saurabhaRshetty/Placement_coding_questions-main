from datetime import datetime

a = input("Enter first date (DD-MM-YYYY): ")
b = input("Enter second date (DD-MM-YYYY): ")

d1 = datetime.strptime(a, "%d-%m-%Y")
d2 = datetime.strptime(b, "%d-%m-%Y")

diff = d2 - d1
print("Difference:", abs(diff.days), "days")
