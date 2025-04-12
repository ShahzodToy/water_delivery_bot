from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils.translation import _

language_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="🇬🇧 English", ),
        ],
        [
            KeyboardButton(text="🇺🇿 Uzbek", ),
        ],
        [
            KeyboardButton(text="🇷🇺 Russian",)
        ]
            ], resize_keyboard=True
    )

def back_button(lang):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('⬅️ Back',lang))
            ]
        ],resize_keyboard=True
    )

def back_and_phone_button(lang):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=(_('📞 Phone number',lang)),request_contact=True)
            ],
            [
                KeyboardButton(text=_('⬅️ Back',lang))
            ]
        ],resize_keyboard=True
    )

def back_and_location_button(lang):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=(_('📞 Location',lang)),request_location=True)
            ],
            [
                KeyboardButton(text=_('⬅️ Back',lang))
            ]
        ],resize_keyboard=True
    )

def main_menu(lang):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('Order product',lang)),
                KeyboardButton(text=_('Contacts',lang))
            ],

            [
                KeyboardButton(text=_('⚙️ Settings',lang))
            ]
        ],resize_keyboard=True
    )

def time_interval(lang):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='8-10'),
                KeyboardButton(text='12-14')
            ],
            [
                KeyboardButton(text='15-18'),
                KeyboardButton(text='17-20')
            ],
            [
                KeyboardButton(text=_('⬅️ Back',lang))
            ]

        ]
    )

def quantity_product(lang):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='2'),
                KeyboardButton(text='3'),
                KeyboardButton(text='4')
            ],
            [
                KeyboardButton(text='4'),
                KeyboardButton(text='5'),
                KeyboardButton(text='6')
            ],
            [
                KeyboardButton(text='7'),
                KeyboardButton(text='8'),
                KeyboardButton(text='8')
            ],
            [
                KeyboardButton(text=_('⬅️ Back',lang))
            ]
        ]
    )

def keyboard_location_input(lang):
    return ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_("Tasdiqlayman",lang)),
            KeyboardButton(text=_("Qo'lda kiritaman",lang))
        ]
    ],resize_keyboard=True)