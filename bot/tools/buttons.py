from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


welcome_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton('calculator 📱', callback_data='calculator')],
    [InlineKeyboardButton('help 📜', callback_data='help')],
])

math_symbols = InlineKeyboardMarkup([
    [InlineKeyboardButton('sum ➕', callback_data='sum')],
    [InlineKeyboardButton('minus ➖', callback_data='minus')],
    [InlineKeyboardButton('multiplication ✖️', callback_data='multiplication')],
    [InlineKeyboardButton('division ➗', callback_data='division')]
])

help_button = ReplyKeyboardMarkup([
    ['help 📜']
], resize_keyboard=True)

ok_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton('ok ✅', callback_data='ok')]
])


