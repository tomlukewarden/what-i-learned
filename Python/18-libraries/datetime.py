# Importing the datetime module
import datetime

# ---------------------------------------------------
# Example 1: Getting the current date and time
# ---------------------------------------------------
current_datetime = datetime.datetime.now()  # Get the current date and time
print(f"Current date and time: {current_datetime}")

# ---------------------------------------------------
# Example 2: Formatting the current date
# ---------------------------------------------------
current_date = datetime.date.today()  # Get today's date
formatted_date = current_date.strftime("%B %d, %Y")  # Format the date in a readable format
print(f"Today's date: {formatted_date}")

# ---------------------------------------------------
# Example 3: Creating a specific date
# ---------------------------------------------------
specific_date = datetime.date(2023, 12, 25)  # Create a date for December 25, 2023
print(f"A specific date: {specific_date}")

# ---------------------------------------------------
# Example 4: Working with time objects
# ---------------------------------------------------
current_time = datetime.datetime.now().time()  # Get the current time
formatted_time = current_time.strftime("%H:%M:%S")  # Format the time
print(f"Current time: {formatted_time}")

# ---------------------------------------------------
# Example 5: Calculating the difference between two dates (timedelta)
# ---------------------------------------------------
date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2023, 12, 31)
date_diff = date2 - date1  # Difference between two dates
print(f"Difference between {date2} and {date1}: {date_diff.days} days")

# ---------------------------------------------------
# Example 6: Adding/subtracting days using timedelta
# ---------------------------------------------------
delta = datetime.timedelta(days=10)  # Define a time difference of 10 days
new_date = current_date + delta  # Add 10 days to the current date
print(f"10 days from today: {new_date}")
