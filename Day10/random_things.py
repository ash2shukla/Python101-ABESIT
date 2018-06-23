import random

# Print a random number between 0 to 1
print(random.random())

# Print a random integer between min to max
print(random.randint(1, 10))

# Choose something from an iterable
print(random.choice([1,2,3,4]))

# Create a random sample from an iterable's elements
# Sample size should always be smaller than the population
print(random.sample([1,2,3,4], 5))