# Mots de Dyck


## Mots de Dyck ? 

Ce programme permet de vérifier si une expression donnée est une expression dyck valide. Une expression dyck est une expression qui utilise des paires de symboles tels que (), [], {}, ‹› ou «» et qui respecte les règles suivantes :


1. Chaque symbole d'ouverture doit être suivi d'un symbole de fermeture correspondant.
2. Les expressions imbriquées doivent être correctement fermées avant de fermer l'expression la plus externe.
 
### Limitations
Ce programme ne prend pas en compte les espaces ou les autres caractères qui ne font pas partie des symboles dyck. Par exemple, l'expression "(( ))" sera considérée comme valide par le programme, bien qu'elle ne le soit pas en réalité.

De plus, ce programme ne supporte pas les expressions dyck contenant des caractères autres que ceux proposés dans l'énoncé. Si vous souhaitez utiliser d'autres symboles dyck, vous devrez modifier le code source.
