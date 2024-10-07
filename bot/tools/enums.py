from enum import Enum


class Text(Enum):
    """
    ~ Fixed text structures.
    """
    
    WELCOME = 'hi %s %s.\n\nWelcome to Calculator Robot!\n\nWhat can I do for you?'
    
    EXAMPLES = '12 + 2341\n\n67 - 10\n\n12 * 10\n\n12 / 2'
    
    CHOOSE_SIGN = 'Choose one to write the math expression.'
    
    SUM = 'Write your plural (+) expression.\n\nexamples:\n\t12 + 78\n\t65 + 244 + 18\n\t1 + 1 + 1 + 1 + 1'
    
    MINUS = 'Write your minus (-) expression.\n\nexamples:\n\t50 - 25\n\t30 - 10 -2\n\t100 - 10 - 10 - 10'
    
    MULTIPLICATION = 'Write your multiplication (x) expression.\n\nexamples:\n\t10 x 12\n\t30 x 10 x 2\n\t100 x 10 x 10 x 10'
    
    DIVISION = 'Write your division (/) expression.\n\nexamples:\n\t10 / 12\n\t30 / 10 / 2\n\t100 / 10 / 10 / 10'
    
    SUM_OUTPUT = 'sum output:\n\n%s = %d'
    
    MINUS_OUTPUT = 'minus output:\n\n%s = %d'
    
    MULTIPLICATION_OUTPUT = 'multiplication output:\n\n%s = %d'
    
    DIVISION_OUTPUT = 'division output:\n\n%s = %d'
