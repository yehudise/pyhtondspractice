def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here
    char_positions = {}
    for char in 'abcdefghijklmnopqrstuvwxyz':
        position = ord(char.lower()) - ord('a') + 1
        char_positions[char] = position
    
    # Convert the word to lowercase for uniformity
    word_lower = word.lower()
    
    # Calculate the sum of character positions in the word
    total = 0
    for char in word_lower:
        if char in char_positions:
            total += char_positions[char]
    
    # Check if the sum is odd
    if total % 2 != 0:
        return True
    else:
        return False
print (is_odd_string('a'))
print (is_odd_string('A'))
print (is_odd_string('aaaa'))
print (is_odd_string('AAaa'))
print (is_odd_string('amazing'))