def reverse_vowels(s):
    """ got help fo this one online - Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] in vowels and s[right] in vowels:
            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in vowels:
            right -= 1
        elif s[right] in vowels:
            left += 1
        else:
            # Neither left nor right characters are vowels, move both pointers
            left += 1
            right -= 1

    return ''.join(s)
print (reverse_vowels("aeiou"))
print(reverse_vowels("Tomatoes"))
print (reverse_vowels("Hello!"))
print(reverse_vowels("why try, shy fly?"))
print(reverse_vowels("Reverse Vowels In A String"))