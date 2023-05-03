
## Version 1 provisoire: ------

# def is_a_dyck_word(word: str) -> bool:
#     stack = []
#     for c in word:
#         if c == '(':
#             stack.append(c)
#         elif c == ')':
#             if len(stack) == 0:
#                 return False
#             stack.pop()
#         else:
#             return False
#     return len(stack) == 0


# ## Version 2 Provisoire :  ----
#
# def is_a_dyck_word(word):
#     opening_symbols = set('([{‹«')
#     closing_symbols = set(')]}›»')
#     stack = []
#     for c in word:
#         if c in opening_symbols:
#             stack.append(c)
#         elif c in closing_symbols:
#             if not stack:
#                 return False
#             elif opening_symbols.index(stack.pop()) != closing_symbols.index(c):
#                 return False
#     return not stack


# Version 3 :

def is_a_dyck_word(word):
    opening_symbols = {'[', '{', '(', '‹', '«', '“', '‘'}
    closing_symbols = {']', '}', ')', '›', '»', '”', '’'}
    stack = []
    for c in word:
        if c in opening_symbols:
            stack.append(c)
        elif c in closing_symbols:
            if not stack or opening_symbols.index(stack.pop()) != closing_symbols.index(c):
                return False
    return not stack

# Exemple d'utilisation :

from dyck_word import is_a_dyck_word

# Test with valid Dyck word
word1 = "(<{}>)[]"
if is_a_dyck_word(word1):
    print(f"'{word1}' is a valid Dyck word.")
else:
    print(f"'{word1}' is not a valid Dyck word.")

# Test with invalid Dyck word
word2 = "(()))"
if is_a_dyck_word(word2):
    print(f"'{word2}' is a valid Dyck word.")
else:
    print(f"'{word2}' is not a valid Dyck word.")
