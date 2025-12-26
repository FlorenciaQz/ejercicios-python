def fermat_number(n: int) -> int:
    """
    Return the n-th Fermat number.

    F_n = 2^(2^n) + 1

    Returns -1 if n is negative.
    """
    if n < 0:
        return -1
    return 2 ** (2 ** n) + 1
