def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    DAYS = {1:"Sunday", 
        2:"Monday", 
        3:"Tuesday", 
        4:"Wednesday", 
        5:"Thursday", 
        6:"Friday", 
        7:"Shabbos"}

    if day_of_week <1 or day_of_week > 7:
        return None
    return DAYS[day_of_week]

print (weekday_name(0))
print (weekday_name(1))
print (weekday_name(3))
print (weekday_name(4))
print (weekday_name(5))
print (weekday_name(6))