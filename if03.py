def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    d=0
    if a<b and b<c:
        d=b
    if a<c and c<b:
        d=c
    if b<a and a<c:
        d=a
        
    return d