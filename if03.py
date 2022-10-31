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
    d=b
    if a<b and b<c or c<b and b<a:
        d=b
    if a<c and c<b or b<c and c<a:
        d=c
    if b<a and a<c or c<a and a<b:
        d=a
        
    return d
