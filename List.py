#a=[1,2,3,4,5,6]
#print(a)


#a=[1,2,3,4,5,6]
#print(a[2:5])

#a=[1,2,3,4,5,6,"virat"]
#for i in a:
#    print(i)

#a=[1,2,3,4,5,6,27,27]
#print(a.count(27))

#a=[1,2,3,4,5,6,27,27]
##print(a)

#a=[1,2,3,4,5,6,27,27]
#a.extend(["a","b"])
#print(a)

names=[]
for i in range(5):
    a=input("Enter name{}".format(i+1))
    names.append(a)
index=1
for i in names:
    print("{}. Mr/Ms {}".format(index,i))
    index = index + 1