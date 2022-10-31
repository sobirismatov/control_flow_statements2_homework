def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """

    n1 = n % 10
    n2 = (n // 10) % 10
    n3 = (n // 100) % 10
    n4 = (n // 1000) % 10
    n5 = (n // 10000)
    
    mx = n1
    index = 1
    
    if(mx < n2):
        mx = n2
        index = 2
    if(mx < n3):
        mx = n3
        index = 3
    if(mx < n4):
        mx = n4
        index = 4
    if(mx < n5):
        mx = n5
        index = 5
    else:
        index = 1
    return index

  