from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
from telegram_package.domain_layer.reply_method_domain import ReplyMethod

def authenticator(func):
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        #build your authentification method

        reply_method = ReplyMethod(update, context)
        return await func(update, context, reply_method, *args, **kwargs)
    return wrapper