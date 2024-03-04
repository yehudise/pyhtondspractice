def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_to_swap = None
    if to_swap.islower():
        swapped_to_swap = to_swap.upper()
    else: 
        swapped_to_swap = to_swap.lower()
    output_string = ""
    for letter in phrase:
        if letter == to_swap or letter == swapped_to_swap:
           if letter.islower():
              output_string += letter.upper()
           else:
              output_string += letter.lower()
        else:
            output_string += letter
    return output_string
print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))
    
            
            