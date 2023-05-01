def is_a_dyck_word(word: str) -> bool:
    stack = []
    for c in word:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            stack.pop()
        else:
            return False
    return len(stack) == 0
