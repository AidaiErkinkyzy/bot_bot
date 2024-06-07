from aiogram import Router, F
from aiogram.filters import Command, CommandStart 
from aiogram.types import (
    Message, ReplyKeyboardMarkup, KeyboardButton, 
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, FSInputFile
)

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    description = (
        "Здравствуйте! \n"
        "Добро пожаловать в HOUSEKG1_SHOP \n"
        "/address - Адрес HOUSEKG1_SHOP \n"
        "/contacts - Контакты \n"
        "/grafic - График работы \n"
        "/price_of_houses- Расценки \n"
        "/feed_back - Отзывы \n"
    )
    kb = [
        [KeyboardButton(text="/address"), KeyboardButton(text="/price")],
        [KeyboardButton(text="/contacts"), KeyboardButton(text="/price_of_houses")],
        [KeyboardButton(text="/grafic"), KeyboardButton(text="/feed_back")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(description, reply_markup=keyboard)



@router.message(Command(commands=['address']))
async def address(message:Message):
    await message.answer(
        "Адресс  \n"
        "Улица Днепровский 111 \n"
        "Ссылка, на сайт - https://www.house.kg/  \n"
    )


@router.message(Command(commands=['contacts']))
async def contacts(message:Message):
    await message.answer(
        "Контакты \n"
        "Тел: +996507223344 \n"
        "whatsApp: wa.me//996507223344 \n"
        "Instagram: https://www.instagram.com/house_kg/?hl=en \n"
        "Youtube: https://www.youtube.com/channel/UCvk3xGUIThJMfKwZyNI8Krw \n"
    )


@router.message(Command(commands=['grafic']))
async def grafic(message:Message):
    await message.answer(
        "График работы \n"
        "Пн - Вс 24:00 \n"
        )



@router.message(Command(commands=['price']))
async def price(message:Message):
    price_list = (
        "Дом, 6 и более комнат, 500 м2 - $ 600 000 \n"
        "Квартира, 4-комн. кв., 142 м2 - $ 198 800 \n"
        "Коммерческая недвижимость, 63 м2 - $ 119 700 \n"
        "Комната в квартире, 35 м2  -  $ 46 000 \n"
        "Участок, 4 соток -  $ 125 000 \n"
        "Дача, 4-комн., 80 м2 - $ 65 000 \n"
        "Ссылка на сайт - https://www.house.kg/details/5712766665ef87e581a46-16785941 \n"
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Дом", callback_data="1")],
        [InlineKeyboardButton(text="Квартира", callback_data="2")],
        [InlineKeyboardButton(text="Коммерческая недвижимость", callback_data="3")],
        [InlineKeyboardButton(text="Комната в квартире", callback_data="4")],
        [InlineKeyboardButton(text="Участок", callback_data="5")],
        [InlineKeyboardButton(text="Дача", callback_data="6")],
        [InlineKeyboardButton(text="Ссылка на сайт", callback_data="7(https://www.house.kg/details/5712766665ef87e581a46-16785941)")],
    ])

    await message.answer(price_list,reply_markup=keyboard)



@router.callback_query(F.data=="1")
async def send_1_picture(callback:CallbackQuery):
    await callback.message.answer_photo(
        photo=FSInputFile("1.jpg"),
        caption = ( # Описание к фото
            "Дом, 6 и более комнат, 500 м2 - $ 600 000 \n"
            "Улица Днепровский 111 \n"
            "Тел: +996507223344 \n"
            "whatsApp: wa.me//996507223344 \n"
            "Instagram: https://www.instagram.com/house_kg/?hl=en \n"
            "Youtube: https://www.youtube.com/channel/UCvk3xGUIThJMfKwZyNI8Krw \n"
        )
    )


@router.callback_query(F.data=="2")
async def send_2_picture(callback:CallbackQuery):
    await callback.message.answer_photo(
        photo=FSInputFile("2.jpg"),
        caption = ( # Описание к фото
            "Квартира, 4-комн. кв., 142 м2 - $ 198 800 \n"
            "Улица Днепровский 111 \n"
            "Тел: +996507223344 \n"
            "whatsApp: wa.me//996507223344 \n"
            "Instagram: https://www.instagram.com/house_kg/?hl=en \n"
            "Youtube: https://www.youtube.com/channel/UCvk3xGUIThJMfKwZyNI8Krw \n"
        )
    )





@router.callback_query(F.data=="3")
async def send_3_picture(callback:CallbackQuery):
    await callback.message.answer_photo(
        photo=FSInputFile("3.jpg"),
        caption = ( # Описание к фото
            "Коммерческая недвижимость, 63 м2 - $ 119 700 \n"
            "Улица Днепровский 111 \n"
            "Тел: +996507223344 \n"
            "whatsApp: wa.me//996507223344 \n"
            "Instagram: https://www.instagram.com/house_kg/?hl=en \n"
            "Youtube: https://www.youtube.com/channel/UCvk3xGUIThJMfKwZyNI8Krw \n"
        )
    )




@router.callback_query(F.data=="4")
async def send_4_picture(callback:CallbackQuery):
    await callback.message.answer_photo(
        photo=FSInputFile("4.jpg"),
        caption = ( # Описание к фото
            "Комната в квартире, 35 м2  -  $ 46 000 \n"
            "Улица Днепровский 111 \n"
            "Тел: +996507223344 \n"
            "whatsApp: wa.me//996507223344 \n"
            "Instagram: https://www.instagram.com/house_kg/?hl=en \n"
            "Youtube: https://www.youtube.com/channel/UCvk3xGUIThJMfKwZyNI8Krw \n"
        )
    )


@router.callback_query(F.data=="5")
async def send_5_picture(callback:CallbackQuery):
    await callback.message.answer_photo(
        photo=FSInputFile("5.jpg"),
        caption = ( # Описание к фото
            "Участок, 4 соток -  $ 125 000 \n"
            "Улица Днепровский 111 \n"
            "Тел: +996507223344 \n"
            "whatsApp: wa.me//996507223344 \n"
            "Instagram: https://www.instagram.com/house_kg/?hl=en \n"
            "Youtube: https://www.youtube.com/channel/UCvk3xGUIThJMfKwZyNI8Krw \n"
        )
    )




@router.callback_query(F.data=="6")
async def send_6_picture(callback:CallbackQuery):
    await callback.message.answer_photo(
        photo=FSInputFile("6.jpg"),
        caption = ( # Описание к фото
            "Дача, 4-комн., 80 м2 - $ 65 000 \n"
            "Улица Днепровский 111 \n"
            "Тел: +996507223344 \n"
            "whatsApp: wa.me//996507223344 \n"
            "Instagram: https://www.instagram.com/house_kg/?hl=en \n"
            "Youtube: https://www.youtube.com/channel/UCvk3xGUIThJMfKwZyNI8Krw \n"
        )
    )





@router.callback_query(F.data=="7")
async def send_7_picture(callback:CallbackQuery):
    await callback.message.answer_photo(
        photo=FSInputFile("7.jpg"),
        caption = ( # Описание к фото
            "Ссылка на сайт - https://www.house.kg/details/5712766665ef87e581a46-16785941 \n"
            "Улица Днепровский 111 \n"
            "Тел: +996507223344 \n"
            "whatsApp: wa.me//996507223344 \n"
            "Instagram: https://www.instagram.com/house_kg/?hl=en \n"
            "Youtube: https://www.youtube.com/channel/UCvk3xGUIThJMfKwZyNI8Krw \n"
        )
    )