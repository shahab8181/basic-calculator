from pyrogram.client import Client
from pyrogram.types import Message
from pyrogram.filters import create



def sum_checker(_, client: Client, message: Message) -> bool:
    """
    ~ sum filter
    """
    if '+' in message.text:
        return True
    else:
        return False
    
    
def minus_checker(_, client: Client, message: Message) -> bool:
    """
    ~ minus filter
    """
    if '-' in message.text:
        return True
    else:
        return False
   
 
def multiplication_checker(_, client: Client, message: Message) -> bool:
    """
    ~ multiplication filter
    """
    if 'x' in message.text:
        return True
    else:
        return False
    

def division_checker(_, client: Client, message: Message) -> bool:
    """
    ~ division filter
    """
    if '/' in message.text:
        return True
    else:
        return False
    


# Define filters

sum_filter = create(sum_checker)
minus_filter = create(minus_checker)
multiplication_filter = create(multiplication_checker)
division_filter = create(division_checker)