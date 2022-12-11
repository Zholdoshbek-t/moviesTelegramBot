from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
button_start = KeyboardButton('/start')
button_quiz = KeyboardButton('/games')
button_location = KeyboardButton('ShareLocation', request_location=True)
button_info = KeyboardButton('Share Info', request_contact=True)


keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_start.row(button_start, button_quiz, button_location, button_info)
