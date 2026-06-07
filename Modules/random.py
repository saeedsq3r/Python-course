import random

# Random float between 0 and 1
print(random.random())

# Random integer
print(random.randint(1, 10))

# Random range value
print(random.randrange(1, 20, 2))

# Random choice from list
print(random.choice(["A", "B", "C"]))

# Multiple random choices
print(random.choices([1,2,3,4], k=2))

# Shuffle list randomly
items = [1,2,3,4]
random.shuffle(items)
print(items)

# Random sample without repetition
print(random.sample([1,2,3,4], 2))

# Random float in range
print(random.uniform(1.5, 5.5))

# Set seed for reproducibility
random.seed(10)

# Get random state
print(random.getstate())

# Beta distribution
print(random.betavariate(1,2))

# Exponential distribution
print(random.expovariate(1))

# Gaussian distribution
print(random.gauss(0,1))

# Triangular distribution
print(random.triangular(1,10,5))

# Log normal distribution
print(random.lognormvariate(0,1))

# Von Mises distribution
print(random.vonmisesvariate(0,1))

# Pareto distribution
print(random.paretovariate(1))

# Weibull distribution
print(random.weibullvariate(1,2))

# Random bits
print(random.getrandbits(8))

# Random character from string
print(random.choice("PYTHON"))