from telegram import ReplyKeyboardMarkup, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram_package.domain_layer.inline_keyboard_domain import full_menu_markup
from telegram_package.repository_layer.decorator import authenticator
from telegram.ext import MessageHandler, filters
from telegram_package import config, llm
from telegram_package.domain_layer.reply_method_domain import ReplyMethod
from langchain_text_splitters import RecursiveCharacterTextSplitter

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the main menu with a custom keyboard."""
    await update.message.reply_text(
        """hello world""",
        reply_markup=full_menu_markup,
    )

@authenticator
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE, reply_method: ReplyMethod) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the button press
    # Respond based on the button clicked
    if query.data == '0':
        text = "You selected option 0. Here's some information for you:\n\nsome_text_0"  # Unique text for option 0
        await reply_method.update_previous_message(
            reply_text=text,
            reply_markup=full_menu_markup
        )

    elif query.data == '1':
        text = f"""You selected option 1. \n\nsome_text_1""" # Unique text for option 1
        await reply_method.update_previous_message(
            reply_text=text,
            reply_markup=full_menu_markup
        )
@authenticator
async def text_input_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, reply_method: ReplyMethod) -> None:
    """Handle user's wishlist input."""
    input_text = update.message.text
    result = llm.generate_llm_answer(input_text)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=4024,
        chunk_overlap=0,
        length_function=len,
        is_separator_regex=False,
    )
    texts = text_splitter.create_documents([result])

    for text in texts:
        await reply_method.send_direct_message(
            reply_text=text.page_content,
        )
def register_app(application) -> None:
    """Start the bot."""
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_input_handler))

if __name__ == "__main__":
    from telegram.ext import Application
    application = Application.builder().token(config.TELEGRAM_TOKEN).build()
    register_app(application)
    application.run_polling()