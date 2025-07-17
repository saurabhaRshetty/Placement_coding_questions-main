ben="aaabbcccccaa"
c=0
res=""
for i in range(len(ben)):
    if(i+1 < len(ben) and ben[i]==ben[i+1]):
        c=c+1
    else:
        res=res+ben[i]
        res=res+str(c+1)
        c=0
print(res)
for i in range(len(ben)):
    if(i+1 < len(ben) and ben[i]==ben[i+1]):
        c=c+1
    


