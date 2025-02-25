from telegram import ReplyKeyboardMarkup, Update, InlineKeyboardMarkup, InlineKeyboardButton

full_menu_keyboard = [
    [InlineKeyboardButton("0", callback_data='0')],
    [InlineKeyboardButton("1", callback_data='1')],
]
main_menu_keyboard = [
    [InlineKeyboardButton("main menu", callback_data='main_menu')]
]
full_menu_markup = InlineKeyboardMarkup(full_menu_keyboard)
main_menu_markup = InlineKeyboardMarkup(main_menu_keyboard)