from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def channels_func(lst, url):
    channels = InlineKeyboardMarkup(inline_keyboard=[])  # Initialize the keyboard

    for number in range(1, lst + 1):
        button = InlineKeyboardButton(
            text=f"{number} - kanal",
            url=url[number - 1]  # Access the corresponding URL from the list
        )
        channels.inline_keyboard.append([button])  # Add each button as a new row

    check_button = InlineKeyboardButton(
        text="✅ Tasdiqlash",
        callback_data='check_subs'
    )
    channels.inline_keyboard.append([check_button])

    return channels
