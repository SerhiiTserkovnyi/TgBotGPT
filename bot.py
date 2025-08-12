from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *

TOKEN = "8020694296:AAHopy_qVMB64EhsGXQG4pp91pgG7wl_Yps"

# тут будемо писати наш код :)

async def start(update, context):
    msg = load_message("main")
    await send_photo(update, context, "main")
    await send_text(update, context, msg)
    await show_main_menu(update, context, {
        "start": "Головне меню",
        "profile": "Генерація Tinder - профілю 😎",
        "opener": "Повідомлення для знайомства 🥰",
        "message": "Листування від вашого імені 😈",
        "date": "Листування із зірками 🔥",
        "gpt": "Поставити запитання чату GPT 🧠"
    })

async def gpt(update, context):
    dialog.mode = "gpt"
    await send_photo(update, context, "gpt")
    msg = load_message("gpt")
    await send_text(update, context, msg)

async def gpt_dialog(update, context):
    text = update.message.text
    prompt = load_prompt("gpt")
    answer = await chatgpt.send_question(prompt, text)
    await send_text(update, context, answer)

async def date(update, context):
    dialog.mode = "date"
    msg = load_message("date")
    await send_photo(update, context, "date")
    await send_text_buttons(update, context, msg, {
        "date_grande": "Аріана Гранде",
        "date_robbie": "Марго Роббі",
        "date_zendaya": "Зендея",
        "date_gosling": "Райан Гослінг",
        "date_hardy": "Том Харді",
    })

async def hello(update, context):
    if dialog.mode == "gpt":
        await  gpt_dialog(update, context)


dialog = Dialog()
dialog.mode = None

chatgpt = ChatGptService(token="javcgkmmT5+ss2PGB5P+5fVNiZS1Y37csPkiyneYEQqWgFZwiUCeCBH1bE5yi4f+9LpUxs9/KCp4PU/t17wLL6HyHca5lQCATBbNq2c2UQl36EgxotUYme4TY2cnEx3RJKz7nRE4Grj3BbRc+EhDC8XswylqW+4gVHxZgocpzyvfRMk35So5p2DBP12VlJ8gvCQlYiEGTGWta6aQCnlKH34/yug2q7yoXf0HJWQ4p3Rf3C068=")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("gpt", gpt))
app.add_handler(CommandHandler("date", date))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
# app.add_handler(CallbackQueryHandler(buttons_handler))
app.run_polling()
