# Define a function called happy_birthday that takes two parameters: name and age
# - Parameters act as placeholders for values that will be passed into the function
def happy_birthday(name, age):  # parameters
    # Print a personalized birthday message using the provided name and age
    print(f'Happy birthday to {name}') 
    print(f'You are {age} years old')
    print('Happy birthday to you')

# Call the happy_birthday function with specific arguments
# - Arguments are the actual values passed into the function when it is called
happy_birthday('John', 29)  # 'John' is passed as the name, 29 as the age
happy_birthday('Albert', 68)  # 'Albert' and 68 are used for this call
happy_birthday('George', 33)  # 'George' and 33 are used for this call

# Explanation of function calls with parameters and arguments:
# - When the function is defined, `name` and `age` are parameters, placeholders for values.
# - Each time we call happy_birthday, we provide specific arguments (like 'John' and 29).
# - These arguments are then used by the function to personalize the message.
# - The function can be called multiple times with different arguments, making it reusable.
