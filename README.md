



# Mots de Dyck

Ce programme prend en entrée une chaîne de caractères et vérifie si elle est un mot de Dyck. Un mot de Dyck est une chaîne formée par deux symboles, un symbole ouvrant et un symbole fermant, tels que les parenthèses, les crochets, les accolades, etc. Un mot de Dyck est correctement parenthésé si pour tout préfixe du mot, le nombre de symboles ouvrants est supérieur ou égal au nombre de symboles fermants, et si le nombre total de symboles ouvrants et fermants est égal.

Par exemple, les mots suivants sont des mots de Dyck :

- ()
- [()]
- ()[]{}
- (())[]

Les mots suivants ne sont pas des mots de Dyck :

- )( 
- ([)]
- (][)
- ([{}]

## Fonctionnement du programme

Le programme définit une fonction `is_a_dyck_word` qui prend en paramètre une chaîne de caractères `word` et renvoie un booléen indiquant si la chaîne est un mot de Dyck ou non.

La fonction utilise une pile pour vérifier le bon équilibre des symboles ouvrants et fermants. Elle suit les étapes suivantes :

- Si le mot est vide, il est correctement parenthésé et la fonction renvoie `True`.
- Si le mot a une longueur impaire, il n'est pas correctement parenthésé et la fonction renvoie `False`.
- Si le mot contient plus de deux symboles différents, il n'est pas valide et la fonction renvoie `False`.
- On déduit les symboles ouvrant et fermant en fonction de leur ordre d'apparition dans le mot. Le premier caractère du mot est le symbole ouvrant et le dernier caractère du mot est le symbole fermant.
- On crée une pile vide.
- On parcourt le mot caractère par caractère. Si on rencontre un symbole ouvrant, on l'empile. Si on rencontre un symbole fermant, on le compare avec le sommet de la pile. Si la pile est vide ou si le sommet de la pile est différent du symbole fermant, il y a un déséquilibre et la fonction renvoie `False`. Sinon, on dépile le sommet de la pile. Si on rencontre un autre symbole que les deux définis, il y a une erreur et la fonction renvoie `False`.
- À la fin du mot, si la pile est vide, le mot est correctement parenthésé et la fonction renvoie `True`. Sinon, il y a un déséquilibre et la fonction renvoie `False`.

## Exemples d'utilisation

Voici quelques exemples d'utilisation de la fonction `is_a_dyck_word` :

```python
>>> is_a_dyck_word("()")
True
>>> is_a_dyck_word("([)]")
False
>>> is_a_dyck_word("([{}])")
True
>>> is_a_dyck_word("(a)")
False
```
