s = input("Enter password: ")
up=0
lw=0
dg=0
sp=0
if(len(s) > 7):
    for i in s :
        if (i.isupper()):
            up = up + 1
        elif (i.islower()):
            lw = lw + 1
        elif (i.isdigit()):
            dg = dg + 1
        else:
            sp = sp + 1
    if(up > 0 and lw > 0 and dg > 0 and sp > 0):
        print("Good Password")
    else:
        print("Bad password")
else:
    print("BAD PASSWORD NO ENOUGH CHARACTERS")