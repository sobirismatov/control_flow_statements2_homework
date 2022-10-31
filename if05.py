def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1=n%2
    n2=n//10%2
    n3=n//100%2
    n4=n//1000%2
    n5=n//10000
    mx=n1
    if mx<n2:
        mx=n2
    if mx<n3:
        mx=n3
    if mx<n4:
        mx=n4
    if mx<n5:
        mx=n5
    return mx
print(main(36465))