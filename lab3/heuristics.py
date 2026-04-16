from connect4 import Connect4

"""
    Functions here should return a scalar value of a current 'position'
    in Connect4 game as seen for player playing with 'token' (one of ['o', 'x']).
"""


def simple_score(position: Connect4, token="x"):
    """Działanie:

    - Jeśli game over:
        odpowiednio 10000 ('mój token' wygrywa), -10000 ('mój token' przegrywa), 0 (w przypadku remisu)

    - Jeśli nie:
        - liczba 'czwórek' która zawiera trzy znaki typu 'mój token'
    odjąć liczba czwórek, która zawiera trzy znaki typu token przeciwnika


    Podpowiedzi:

    Skorzystać z:
        - position.iter_fours()
        - metody count() dla list: np. ['x', 'x', 'x', 'x'].count('x') -> 4

    """
    score = 0

    raise NotImplementedError("Implement simple_score function")

    return score


def advanced_score(position: Connect4, token="x"):
    """Działanie:

    Użyj wyobraźni i stwórz własną heurystykę oceny pozycji.

    Podpowiedzi:

    - pewnie powinno być to rozwinięcie simple_score
    - metoda position.center_column() - zwraca kolumnę środkową - pewnie nie jest napisana bez powodu

    """

    score = 0

    raise NotImplementedError("Implement advanced_score function")

    return score
