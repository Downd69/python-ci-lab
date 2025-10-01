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
    halfway = len(text) // 2

    for c in text[:halfway]:
        queue.append(c)
    
    for c in text[halfway + 1:]:
        if c != queue.pop():
            return False
        
    return True
