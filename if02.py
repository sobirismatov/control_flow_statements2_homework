def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    answer=a
    if answer<b:
        answer=b
    if answer<c:
        answer=c
    return answer