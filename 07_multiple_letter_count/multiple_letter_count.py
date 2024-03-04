def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_frequency={}
    for word in phrase:
        for letter in word:
            keys=letter_frequency.keys()
            if letter in keys:
                letter_frequency[letter]+=1
            else:
                letter_frequency[letter]=1
    return letter_frequency

print (multiple_letter_count('yay'))
print (multiple_letter_count('Yay'))
print (multiple_letter_count('how are you'))


 