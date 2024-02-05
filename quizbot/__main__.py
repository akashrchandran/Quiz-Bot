from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from quizbot import BOT_TOKEN, logger, ENVIRONMENT, PORT
from quizbot.error_handler import error_handler
from quizbot.modules.mcq_qeneration import MCQGenerator


mcq = MCQGenerator()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        "Welcome to QuizBot! I can help you create quizzes from any text you send me. Just send me the text and I'll do the rest!",
        # reply_markup=strat_inline_keyboard,
        # disable_web_page_preview=True,
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        "Helping in need is a good deed! I can help you create quizzes from any text you send me. Just send me the text and I'll do the rest!",
        # reply_markup=help_inline_keyboard,
        # disable_web_page_preview=True
    )

async def generate_mcq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Generating mcq questions...")
    questions = mcq.generate_mcq_questions(update.message.text, 5)
    for question in questions:
        await context.bot.send_poll(
            update.effective_chat.id,
            question.questionText,
            type="quiz",
            options= question.options,
            correct_option_id= question.ansindex,
            is_anonymous=False,
            allows_multiple_answers=False,
        )




def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_mcq))

    application.add_error_handler(error_handler)

    if ENVIRONMENT:
        logger.info("Running in dev -- using polling")
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    else:
        logger.info("Running in prod -- using webhooks")
        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            webhook_url="https://ktulivetrackerbot-akashrchandran.koyeb.app/",
        )


if __name__ == "__main__":
    main()
