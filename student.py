students = [
    {"name": "raju", "dept": "cse", "marks": [20, 30, 40]},
    {"name": "vijay", "dept": "cse", "marks": [10, 70, 43]},
    {"name": "pavi", "dept": "ece", "marks": [22, 38, 56]},
    {"name": "rose", "dept": "ece", "marks": [26, 36, 89]},
    {"name": "virat", "dept": "ece", "marks": [16, 90, 43]}
]

for i in students:
    sum1 = sum(i["marks"])
    per = sum1 / 3  # Assuming percentage out of 100 for 3 subjects
    i["per"] = per
print(students)


des=["FIRST","SECOND","THIRD","FOURTH","FIFTH"]

b = sorted(students, key=lambda x: x["per"], reverse=True)
for idx, student in enumerate(b):
    print("{}. {} stands {} : {:.2f}%".format(idx+1, student["name"], des[idx], student["per"]))