# Define a function called display_invoice that takes three parameters: username, amount, and due_date
# - Parameters are variables in the function definition that accept values when the function is called
def display_invoice(username, amount, due_date): 
    # Print a greeting message that includes the provided username
    print(f"Hello {username}")
    # Print the invoice details, showing the amount in a dollar format with two decimal places
    # and displaying the due date. The "{amount:.2f}" formats the amount to two decimal places.
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

# Call the display_invoice function with specific arguments
# - Each argument here corresponds to a parameter in the function definition
display_invoice("BroCode", 42.50, "01/02")  # username="BroCode", amount=42.50, due_date="01/02"
display_invoice("JoeSchmo", 100.99, "02/03")  # username="JoeSchmo", amount=100.99, due_date="02/03"

# Explanation of parameters, arguments, and string formatting:
# - When the function is defined, `username`, `amount`, and `due_date` are parameters that
#   act as placeholders for the data.
# - Each time we call display_invoice, we provide specific arguments (like "BroCode", 42.50, "01/02").
# - The function uses these values to create a customized invoice message for each user.
# - The amount is formatted as "{amount:.2f}" to ensure it always displays two decimal places.
