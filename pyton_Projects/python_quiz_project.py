print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
playing = playing.lower()
if playing != "yes":
    quit()

print("Okey! Let's play :)")
score = 0
total_Q = 4
# Q1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
# Q3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q4
answer = input("What does PSU stand for? ")
if answer.lower() == "power suply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")
if score != 0:
    print(f"Your percentage is {(score/total_Q) *100}%.")
else:
    print("Your percentage is 0.0%.")
