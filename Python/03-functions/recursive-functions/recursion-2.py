def is_palindrome(words):
    """
    The function `is_palindrome` recursively checks if each word in a list of words is a palindrome.
    
    :param words: The `words` parameter in the `is_palindrome` function is a list of words that are
    checked for being palindromes. The function recursively checks each word in the list to determine if
    it is a palindrome or not
    :return: In the provided code snippet, the `is_palindrome` function is a recursive function that
    checks if each word in a list of words is a palindrome. The function prints whether each word is a
    palindrome or not.
    """
    
    # Base case: If the list is empty, return (all words checked)
    if not words:
        return 'All words checked'
    

    # Check if the first word is a palindrome
    word = words[0]
    if word == word[::-1]:
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is not a palindrome")
    
    # Recursive call on the remaining words
    is_palindrome(words[1:])

# Get user input
s = input("Enter a string: ").lower()
words = s.split()  # Split the input into individual words

# Call the recursive function
is_palindrome(words)
