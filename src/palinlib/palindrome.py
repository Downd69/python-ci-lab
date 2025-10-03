def is_palindrome(text: str) -> bool:
    """Check whether or not a string is a palindrome.

    Args:
        - text: the string to check

    Returns:
        - True if a palindrome, otherwise False.
        
    Examples:
        - "abba" is a palindrome; should return True.
        - "abcd" is not a palindrome; should return False.
    """
    
    queue = []
    n = len(text)
    halfway = n // 2

    # push left half
    for c in text[:halfway]:
        queue.append(c)

    # for odd lengths, skip the middle character
    if n % 2 == 0:
        right_half = text[halfway:]
    else:
        right_half = text[halfway + 1:]

    # compare right half with stack
    for c in right_half:
        if c != queue.pop():
            return False

    return True
