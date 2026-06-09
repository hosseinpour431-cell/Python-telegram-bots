async def handle_spot(update, context):
    """مدیریت دکمه اسپات"""
    await update.message.edit_text(
        "💰 بخش اسپات\n\n"
        "در حال تحلیل بازار اسپات...\n"
        "اینجا کد اسپات شما اجرا میشه"
    )
    # اینجا کد اسپات خودتون رو بنویسید
