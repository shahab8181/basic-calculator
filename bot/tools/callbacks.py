from pyrogram.client import Client
from pyrogram.types import CallbackQuery
from pyrogram.filters import regex
from .buttons import ok_keyboard, math_symbols
from .enums import Text



@Client.on_callback_query(regex('calculator'))
async def calculator_callback(client: Client, callback: CallbackQuery) -> None:
    """
    ~ calculator callback handling
    """
    await callback.edit_message_text(Text.CHOOSE_SIGN.value, reply_markup=math_symbols)


@Client.on_callback_query(regex('help'))
async def help_callback(client: Client, callback: CallbackQuery) -> None:
    """
    ~ help callback handling
    """
    await callback.edit_message_text(Text.EXAMPLES.value, reply_markup=ok_keyboard)


@Client.on_callback_query(regex('ok'))
async def ok_callback(client: Client, callback: CallbackQuery) -> None:
    """
    ~ ok callback handling
    """
    await callback.edit_message_text(Text.CHOOSE_SIGN.value, reply_markup=math_symbols)
    

@Client.on_callback_query(regex('sum'))
async def sum_callback(client: Client, callback: CallbackQuery) -> None:
    """
    ~ sum callback handling
    """
    await callback.edit_message_text(Text.SUM.value)
    
    
@Client.on_callback_query(regex('minus'))
async def minus_callback(client: Client, callback: CallbackQuery) -> None:
    """
    ~ minus callback handling
    """
    await callback.edit_message_text(Text.MINUS.value)
 
    
@Client.on_callback_query(regex('multiplication'))
async def multiplication_callback(client: Client, callback: CallbackQuery) -> None:
    """
    ~ multiplication callback handling
    """
    await callback.edit_message_text(Text.MULTIPLICATION.value)
    
    
@Client.on_callback_query(regex('division'))
async def division_callback(client: Client, callback: CallbackQuery) -> None:
    """
    ~ division callback handling
    """
    await callback.edit_message_text(Text.DIVISION.value)