"""Encodage RLE simple : liste de tuples (caractère, occurrences consécutives)."""

#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """Retourne la liste de tuples encodant la chaîne s (version itérative)."""
    if not s:
        return []
    chars = [s[0]]
    counts = [1]
    for ch in s[1:]:
        if ch == chars[-1]:
            counts[-1] += 1
        else:
            chars.append(ch)
            counts.append(1)
    return list(zip(chars, counts))


def artcode_r(s):
    """Retourne la liste de tuples encodant la chaîne s (version récursive)."""
    # cas de base
    if not s:
        return []
    # recherche du nombre de caractères identiques au premier
    first = s[0]
    i = 0
    n = len(s)
    while i < n and s[i] == first:
        i += 1
    # construction du résultat et appel récursif sur le reste
    return [(first, i)] + artcode_r(s[i:])


#### Fonction principale


def main():
    """Point d'entrée : tests simples d'exécution."""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))


if __name__ == "__main__":
    main()
