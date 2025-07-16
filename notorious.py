#notorious=["DHARSHAN","ANUJ","ROHITH"]
#names=["ANU","DHARSHAN","ROHIT","JACK","PRIYA","BALA","RAI","RAM","RAJ","BEN"]
#score=[2,5,6,8,3,5,6,9,8,2]
#for i in range(len(names)):
#    if score[i]>5:
#        if names[i] not in notorious:
#           print(names[i])


a=[23,129,45,200,45,34,27,77,88,127]
for i in a:
    if(i > 100):
        a.remove(i)
print(sum(a)/len(a))