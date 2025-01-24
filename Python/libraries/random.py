# Importing the random module
import random

# ---------------------------------------------------
# Example 1: Using random.randint() to generate a random integer
# ---------------------------------------------------
random_int = random.randint(1, 100)  # Generates a random integer between 1 and 100 (inclusive)
print(f"Random integer between 1 and 100: {random_int}")

# ---------------------------------------------------
# Example 2: Using random.uniform() to generate a random float
# ---------------------------------------------------
random_float = random.uniform(1.0, 10.0)  # Generates a random float between 1.0 and 10.0
print(f"Random float between 1.0 and 10.0: {random_float:.2f}")

# ---------------------------------------------------
# Example 3: Using random.choice() to select a random element from a list
# ---------------------------------------------------
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
random_fruit = random.choice(fruits)  # Selects a random fruit from the list
print(f"Randomly selected fruit: {random_fruit}")

# ---------------------------------------------------
# Example 4: Using random.shuffle() to shuffle a list in place
# ---------------------------------------------------
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
random.shuffle(cards)  # Shuffle the list of cards in place
print(f"Shuffled deck of cards: {cards}")

# ---------------------------------------------------
# Example 5: Using random.sample() to get a sample of elements from a list
# ---------------------------------------------------
sample_fruits = random.sample(fruits, 3)  # Select 3 random elements from the fruits list without replacement
print(f"Random sample of 3 fruits: {sample_fruits}")

# ---------------------------------------------------
# Example 6: Using random.seed() to set the seed for reproducibility
# ---------------------------------------------------
random.seed(10)  # Set the seed for random number generation
random_int_seeded = random.randint(1, 100)  # Generates a random integer using the seeded random generator
print(f"Random integer with seed 10: {random_int_seeded}")
