def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    c=0
    if temp<0:
        c="Freezing"
    if 1<=temp and temp<=10:
        c="Very Cold"
    if 11<=temp and temp<=20:
        c="Cold"
    if 21<=temp and temp<=30:
        c="Normal"
    if 31<=temp and temp<=40:
        c="Hot"
    if 41<=temp and temp<=50:
        c="Very Hot"


    return c