def is_a_dyck_word(word: str) -> bool:
    # Si le mot est vide, il est correctement parenthésé
    if not word:
        return True

    # Si le mot a une longueur impaire, il n'est pas correctement parenthésé
    if len(word) % 2 != 0:
        return False

    # Si le mot contient plus de deux symboles différents, il n'est pas valide
    if len(set(word)) > 2:
        return False

    # On déduit les symboles ouvrant et fermant en fonction de leur ordre d'apparition
    opening = word[0]
    closing = word[-1]  # On prend le dernier caractère au lieu du deuxième

    # On crée une pile vide
    stack = []

    # On parcourt le mot caractère par caractère
    for char in word:
        # Si on rencontre un symbole ouvrant, on l'empile
        if char == opening:
            stack.append(char)
        # Si on rencontre un symbole fermant, on le compare avec le sommet de la pile
        elif char == closing:
            # Si la pile est vide, il y a un déséquilibre
            if not stack:
                return False
            # Si le sommet de la pile est différent du symbole fermant, il y a une erreur
            if stack[-1] != opening:
                return False
            # Sinon, on dépile le sommet de la pile
            else:
                stack.pop()
        # Si on rencontre un autre symbole, il y a une erreur
        else:
            return False

    # À la fin du mot, si la pile est vide, le mot est correctement parenthésé
    return not stack
