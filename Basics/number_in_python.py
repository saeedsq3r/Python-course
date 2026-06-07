# Types: int() , float(), complex() 
# Operators: +, -, *, /, //, %, **

# Rounding Functions: abs(), round(), pow(),ceil(), floor(),trunc()
# advance math: sqrt(), sin(), cos(), log()

# random: random(), randint()

# validation: isinteger(), isfloat(), isinstance()

# challenge
# Generate a random integer between 1 and 100 and check if it is even or odd.
import random
number = random.randint(1, 100)

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")