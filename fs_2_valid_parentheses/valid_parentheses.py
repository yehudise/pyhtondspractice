def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    parentheses_stack = []
    for paren in parens:
        if paren == '(':
            parentheses_stack.append(paren)
        elif paren == ')':
            if not parentheses_stack:
                return False  # If there's no opening parenthesis to match
            parentheses_stack.pop()  # Match with the topmost opening parenthesis
    return len(parentheses_stack) == 0 
print(valid_parentheses("()"))

print(valid_parentheses("()()"))


print(valid_parentheses("(()())"))
  

print(valid_parentheses(")()"))

print(valid_parentheses("())"))


print(valid_parentheses("((())"))
   

print(valid_parentheses(")()("))