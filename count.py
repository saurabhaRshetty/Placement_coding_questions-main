import time

start = time.time()  # Start timing before input
s = input("Enter Sentence: ")
end = time.time()    # End timing after input

c = 0
for i in range(len(s) - 1):  # Avoid index out of range
    if s[i] == " " and s[i + 1] != " ":
        c += 1

if len(s.strip()) == 0:
    print("The number of words are 0")
else:
    print("The number of words are", c + 1)

print("Time taken to enter the sentence:", round(end - start, 2), "seconds")
