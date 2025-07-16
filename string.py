#a=[i for i in range(100,200)]
#print(a)

#display the 2 digit numbers which are divisible by 3 ,4 ,5 ,7

#a = [i for i in range(10,100) if i%3==0 & i%4==0 & i%5==0 ]
#print(a)

#int a[2][3][4][2]

#a=[[20,30,40],
#   [1,2,3],
#   [40,50,60]]
#print(a[2][1])


a=[[[11,22,33],
   [44,55,66],
   [77,12,32]],

   [[41,42,43],
    [52,54,56],
    [98,97,95]]]
#for i in range(3):
#    print(a[1][0][i])


#for i in range(1,3):
#    for j in range(0,3):
#        print(a[0][i][j])


for i in range(2):
    for j in range(3):
        for k in range(3):
            print(a[i][j][k],end=" ")
        print()
    print("____________")



    