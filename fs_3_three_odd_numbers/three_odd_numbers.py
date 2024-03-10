def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    n = len(nums)
    

    for i in range(n - 2):  
        num1 = nums[i]
        num2 = nums[i + 1]
        num3 = nums[i + 2]
        if (num1 + num2 + num3) % 2 != 0:
            return True 
    return False

print (three_odd_numbers([1, 2, 3, 4, 5]))
print (three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))
print(three_odd_numbers([5, 2, 1]))
print (three_odd_numbers([1, 2, 3, 3, 2]))