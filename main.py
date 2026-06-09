from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN
from futures import handle_futures
from spot import handle_spot

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دستور /start - نمایش دکمه‌های اصلی"""
    
    # ساخت کیبورد اینلاین با دکمه‌ها
    keyboard = [
        [
            InlineKeyboardButton("📈 فیوچرز", callback_data='futures'),
            InlineKeyboardButton("💰 اسپات", callback_data='spot')
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 به ربات کریپتو خوش اومدی!\n\n"
        "لطفاً یک گزینه رو انتخاب کن:",
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """مدیریت کلیک روی دکمه‌ها"""
    query = update.callback_query
    await query.answer()  # ضروری برای پاسخ به کلیک
    
    choice = query.data
    
    if choice == 'futures':
        await handle_futures(update, context)
    elif choice == 'spot':
        await handle_spot(update, context)

def main():
    """اجرای بات"""
    # ساخت اپلیکیشن
    application = Application.builder().token(BOT_TOKEN).build()
    
    # اضافه کردن Handlerها
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # شروع بات
    print("🤖 بات در حال اجراست...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
