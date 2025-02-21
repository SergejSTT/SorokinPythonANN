def is_balanced(bracket_sequence):
    stack = []
    for char in bracket_sequence:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack:
                return False
            top = stack.pop()
            if char == ")" and top != "(":
                return False
            if char == "]" and top != "[":
                return False
    return len(stack) == 0

bracket_sequence = "[[(())()(())]]" #testing sequence
if is_balanced(bracket_sequence):
    print("The sequence is balanced.")
else:
    print("The sequence is not balanced.")
