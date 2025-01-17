# from aiogram import Dispatcher
# from sqlalchemy.orm import sessionmaker

from .throttling import ThrottlingMiddleware
from .subscription import SubscriptionMiddleware


# def setup(dp: Dispatcher, pool: sessionmaker):
#     dp.message.middleware(SubscriptionMiddleware())
