import random

name1 = input("Enter player 1: ")
name2 = input("Enter player 2: ")
print("Comp has fixed 5 nums in range 1 to 10.")
print("You guys have to guess it... Ready???")

# Computer generates 5 unique random numbers between 1 and 10
nums = []
while len(nums) < 5:
    d = random.randint(1, 10)
    if d not in nums:
        nums.append(d)

print("---------------------------")

# Score and previous guesses
s1 = 0
s2 = 0
player1 = []
player2 = []

# Game rounds
for i in range(3):
    print("------------ Round {} ------------".format(i+1))
    
    # Player 1's turn
    ch = int(input(f"Dear {name1}, guess your choice: "))
    while ch in player1:
        ch = int(input("It is already taken, choose another: "))
    player1.append(ch)
    if ch in nums:
        print("Correct!")
        s1 += 1
    else:
        print("Wrong!")

    # Player 2's turn
    ch = int(input(f"Dear {name2}, guess your choice: "))
    while ch in player2:
        ch = int(input("It is already taken, choose another: "))
    player2.append(ch)
    if ch in nums:
        print("Correct!")
        s2 += 1
    else:
        print("Wrong!")

# Final score
print("\n-------- Final Scores --------")
print(f"{name1}'s score: {s1}")
print(f"{name2}'s score: {s2}")

# Winner
if s1 > s2:
    print(f"{name1} wins!")
elif s2 > s1:
    print(f"{name2} wins!")
else:
    print("It's a tie!")

# For debugging (optional): print the actual numbers
# print("Computer's numbers were:", nums)
