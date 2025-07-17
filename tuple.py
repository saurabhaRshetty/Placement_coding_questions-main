#immutable ,orderd,(),representable
a={1,2,3,4,5,6}
b={3,4,5,6,7,8,9}
print(a & b)
print(a - b)
print(b - a)
print(a^b)

stu={"name":"SACHIN","age":54,"runs":563}
stu["name"]="RAJU"
print(stu)
for i in stu.keys():
    print(i)
print(stu)


student=[{"name":"Advik","marks":[30,50,54,67,90]},
         {"name":"Advik","marks":[10,50,54,67,93]},
         {"name":"Advik","marks":[30,50,54,66,90]}]
print(student[3])