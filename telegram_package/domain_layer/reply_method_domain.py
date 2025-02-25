from telegram import ReplyKeyboardMarkup, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler, CallbackContext

class ReplyMethod():
    def __init__(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.update = update
        self.context = context

    async def update_previous_message(self, reply_text, reply_markup=None):
        await self.update.callback_query.edit_message_text(
            text=reply_text,
            reply_markup=reply_markup
        )

    async def reply_to_message(self, reply_text, reply_markup=None):
        await self.update.message.reply_text(
            text=reply_text,
            reply_markup=reply_markup,
        )

    async def send_direct_message(self, reply_text, reply_markup=None):
        await self.context.bot.send_message(
            chat_id=self.update.effective_user.id,
            text=reply_text,
            reply_markup=reply_markup
        )

