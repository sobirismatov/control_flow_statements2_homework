def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    d=0
    if a==b:
        d=0
    if a!=b:
        if a>b:
            d=a
        else:
            d=b



    return d