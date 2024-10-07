from pyrogram.client import Client
from pyrogram.types import Message
from pyrogram.enums import ChatAction
from pyrogram.filters import command, regex
from .filters import (
    sum_filter, minus_filter,
    multiplication_filter, division_filter
)
from .buttons import welcome_keyboard, ok_keyboard
from .enums import Text
from .maths import (
    plus, minus,
    multiplication, division
)



@Client.on_message(command('start'))
async def welcome_handler(client: Client, message: Message) -> None:
    """
    ~ welcome handler
    """
    await message.reply_chat_action(ChatAction.TYPING)
    await message.reply(Text.WELCOME.value % (message.from_user.first_name if message.from_user.first_name else '', message.from_user.last_name if message.from_user.last_name else ''), reply_markup=welcome_keyboard)


@Client.on_message(regex('help'))
async def help_handler(client: Client, message: Message) -> None:
    """
    ~ help handler
    """
    await message.reply(Text.EXAMPLES.value)
    

@Client.on_message(sum_filter)
async def sum_handler(client: Client, message: Message) -> None:
    """
    ~ sum handler
    """
    sum_expression = map(int, message.text.split('+'))
    sum_string = '+'.join(message.text.split('+'))
    await message.reply_chat_action(ChatAction.TYPING)
    await message.reply(Text.SUM_OUTPUT.value % (sum_string, plus(*sum_expression)), reply_markup=ok_keyboard)
    

@Client.on_message(minus_filter)
async def minus_handler(client: Client, message: Message) -> None:
    """
    ~ minus handler
    """
    minus_expression = map(int, message.text.split('-'))
    minus_string = '-'.join(message.text.split('-'))
    await message.reply_chat_action(ChatAction.TYPING)
    await message.reply(Text.MINUS_OUTPUT.value % (minus_string, minus(*minus_expression)), reply_markup=ok_keyboard)
    
    
@Client.on_message(multiplication_filter)
async def multiplication_handler(client: Client, message: Message) -> None:
    """
    ~ multiplication handler
    """
    multiplication_expression = map(int, message.text.split('x'))
    multiplication_string = 'x'.join(message.text.split('x'))
    await message.reply_chat_action(ChatAction.TYPING)
    await message.reply(Text.MULTIPLICATION_OUTPUT.value % (multiplication_string, multiplication(*multiplication_expression)), reply_markup=ok_keyboard)


@Client.on_message(division_filter)
async def division_handler(client: Client, message: Message) -> None:
    """
    ~ division handler
    """
    division_expression = map(int, message.text.split('/'))
    division_string = '/'.join(message.text.split('/'))
    await message.reply_chat_action(ChatAction.TYPING)
    await message.reply(Text.DIVISION_OUTPUT.value % (division_string, division(*division_expression)), reply_markup=ok_keyboard)
 
    
@Client.on_message(~command('start') & ~regex('help'))
async def unknown_handler(client: Client, message: Message) -> None:
    """
    ~ unknown handler
    """
    await message.reply('❌Anonymous command!❌')
        

