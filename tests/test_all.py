from palinlib import is_palindrome

def test_palindrome_simple_odd():
    assert is_palindrome("abcba") == True

def test_palindrome_simple_even():
    assert is_palindrome("abba") == True

def test_palindrome_simple_odd_negative():
    assert is_palindrome("abcca") == False

def test_palindrome_simple_even_negative():
    assert is_palindrome("abca") == False

def test_palindrome_simple_longer_odd():
    assert is_palindrome("abcdefghijkjihgfedcba") == True

def test_palindrome_simple_longer_even():
    assert is_palindrome("abcdefghijjihgfedcba") == True

def test_palindrome_empty():
    assert is_palindrome("") == True

def test_palindrome_one_letter():
    assert is_palindrome("") == True

def test_palindrome_two_letters():
    assert is_palindrome("aa") == True

def test_palindrome_two_letters_negative():
    assert is_palindrome("ab") == False
