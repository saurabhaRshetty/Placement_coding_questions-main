#enter the marks until the user is given user puts input as 0 and total should be 190 (70+110+80+40+0)=190
total = 0
while True:
    a = int(input("Enter the marks (0 to stop): "))
    if a == 0:
        break
    total += a
print("Total marks:", total)