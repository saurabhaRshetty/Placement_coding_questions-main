def prime(i):
    if i < 2:
        return False
    for j in range(2, i):
        if(i % j == 0):
            return False
    return True

def sod(i):
    d = list(str(i))
    x = sum([int(j) for j in d])
    return x

def dig(i):
    while(i > 0):
        d = i % 10
        if(not prime(d)):
            return False
        i = i // 10
    return True    

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Is {num} prime? {prime(num)}")
    print(f"Sum of digits of {num}: {sod(num)}")
    print(f"Are all digits of {num} prime? {dig(num)}")
        