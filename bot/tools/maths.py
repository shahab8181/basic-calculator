from decimal import Decimal



def plus(*numbers: int | float | Decimal) -> int | float | Decimal:
    """
    ~ sum operator (+)
    """
    return sum(numbers)


def minus(*numbers: int | float | Decimal) -> int | float | Decimal:
    """
    ~ minus operator (-)
    """
    total = numbers[0]
    
    for _ in range(len(numbers)):
        if _ == 0: 
            continue
        else:
            total -= numbers[_]
    
    return total
        

def multiplication(*numbers: int | float | Decimal) -> int | float | Decimal:
    """
    ~ multiplication operator (x)
    """
    total = numbers[0]
    
    for _ in range(len(numbers)):
        if _ == 0: 
            continue
        else:
            total *= numbers[_]
    
    return total


def division(*numbers: int | float | Decimal) -> int | float | Decimal:
    """
    ~ division operator (-)
    """
    total = numbers[0]
    
    for _ in range(len(numbers)):
        if _ == 0: 
            continue
        else:
            total /= numbers[_]
    
    return total

