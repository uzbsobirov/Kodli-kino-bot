from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from loader import db, bot
from data.config import ADMINS
from utils.extra_datas import make_title

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    """
            MARKDOWN V2                     |     HTML
    link:   [Google](https://google.com/)   |     <a href='https://google.com/'>Google</a>
    bold:   *Qalin text*                    |     <b>Qalin text</b>
    italic: _Yotiq shriftdagi text_         |     <i>Yotiq shriftdagi text</i>



                    **************     Note     **************
    Markdownda _ * [ ] ( ) ~ ` > # + - = | { } . ! belgilari to'g'ridan to'g'ri ishlatilmaydi!!!
    Bu belgilarni ishlatish uchun oldidan \ qo'yish esdan chiqmasin. Masalan  \.  ko'rinishi . belgisini ishlatish uchun yozilgan.
    """

    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_mention = message.from_user.mention_html(name=full_name)
    user = None
    try:
        user = await db.add_user(user_id=user_id, full_name=full_name, username=username)
    except Exception as error:
        logger.info(error)
    if user:
        count = await db.count_users()
        msg = (f"[{make_title(user['full_name'])}](tg://user?id={user['user_id']}) bazaga qo'shildi\.\n"
               f"Bazada {count} ta foydalanuvchi bor\.")
    else:
        msg = f"[{make_title(full_name)}](tg://user?id={user_id}) bazaga oldin qo'shilgan"
    for admin in ADMINS:
        try:
            await bot.send_message(
                chat_id=admin,
                text=msg,
                parse_mode=ParseMode.MARKDOWN_V2
            )
        except Exception as error:
            logger.info(f"Data did not send to admin: {admin}. Error: {error}")
    text = f"""<b>👋 Assalomu alaykum {user_mention} botimizga xush kelibsiz.</b>

<i>✍🏻 Kino kodini yuboring.</i>"""
    await message.answer(text=text)
