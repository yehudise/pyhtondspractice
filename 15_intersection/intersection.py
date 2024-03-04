def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> ç
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    intersection = list(set(l1).intersection(l2))
    return intersection

print (intersection([1, 2, 3], [2, 3, 4]))
print (intersection([1, 2, 3], [4, 5, 6]))
print (intersection([1, 2, 3], [3, 4]))
