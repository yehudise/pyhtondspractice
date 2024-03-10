
m1 = [
[1,   2],
[30, 40],
]
m2 = [
 [1, 2, 3],
[4, 5, 6],
[7, 8, 9],
 ]
def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    size = len(matrix)
    sum_tl_br = sum(matrix[i][i] for i in range(size))  # Top-left to bottom-right diagonal
    sum_bl_tr = sum(matrix[i][size - 1 - i] for i in range(size))  # Bottom-left to top-right diagonal
    return sum_tl_br + sum_bl_tr
print(sum_up_diagonals(m1))
print(sum_up_diagonals(m2))