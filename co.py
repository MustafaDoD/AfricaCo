import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

countries_capitals = {
    "الجزائر": "الجزائر",
    "أنغولا": "لواندا",
    "بنين": "بورتو نوفو",
    "بوتسوانا": "غابورون",
    "بوركينا فاسو": "واغادوغو",
    "بوروندي": "بوجمبورا",
    "الرأس الأخضر": "برايا",
    "الكاميرون": "ياوندي",
    "جمهورية أفريقيا الوسطى": "بانغي",
    "تشاد": "نجامينا",
    "جزر القمر": "موروني",
    "جمهورية الكونغو الديمقراطية": "كينشاسا",
    "جمهورية الكونغو": "برازافيل",
    "جيبوتي": "جيبوتي",
    "مصر": "القاهرة",
    "غينيا الاستوائية": "مالابو",
    "إريتريا": "اسمرة",
    "إسواتيني": "مبابان",
    "إثيوبيا": "اديس ابابا",
    "الغابون": "ليبرفيل",
    "غامبيا": "بانجول",
    "غانا": "اكرا",
    "غينيا": "كوناكري",
    "غينيا بيساو": "بيساو",
    "كوت ديفوار": "ياموسوكرو",
    "كينيا": "نيروبي",
    "ليسوتو": "ماسيرو",
    "ليبيريا": "مونروفيا",
    "ليبيا": "طرابلس",
    "مدغشقر": "انتاناناريفو",
    "ملاوي": "ليلونغوي",
    "مالي": "باماكو",
    "موريتانيا": "نواكشوط",
    "موريشيوس": "بورت لويس",
    "المغرب": "الرباط",
    "موزمبيق": "مابوتو",
    "ناميبيا": "ويندهوك",
    "النيجر": "نيامي",
    "نيجيريا": "ابوجا",
    "رواندا": "كيغالي",
    "ساو تومي وبرينسيب": "ساو تومي",
    "السنغال": "داكار",
    "سيشل": "فيكتوريا",
    "سيراليون": "فريتاون",
    "الصومال": "مقديشو",
    "جنوب أفريقيا": "بريتوريا",
    "جنوب السودان": "جوبا",
    "السودان": "الخرطوم",
    "تنزانيا": "دودوما",
    "توغو": "لومي",
    "تونس": "تونس العاصمة",
    "أوغندا": "كمبالا",
    "زامبيا": "لوساكا",
    "زيمبابوي": "هراري"
}

# وظيفة لبدء البوت
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('هلو! ارسلي "افريقيا" عشان تبدي التحدي •-•.')

# وظيفة للتحدي
async def africa(update: Update, context: CallbackContext) -> None:
    country = random.choice(list(countries_capitals.keys()))
    context.user_data['country'] = country
    await update.message.reply_text(f'ما هي عاصمة {country}?')

# وظيفة للتحقق من الإجابة
async def check_answer(update: Update, context: CallbackContext) -> None:
    country = context.user_data.get('country')
    if country:
        capital = countries_capitals[country]
        if update.message.text == capital:
            await update.message.reply_text('صحييييح ترربيييتي😼!')
        else:
            await update.message.reply_text(f'نوووب خطأ. العاصمة الصحيحة هي {capital}.')
        del context.user_data['country']
    else:
        await update.message.reply_text('ارسلي "افريقيا" لبدء التحدي.')

def main() -> None:
    application = Application.builder().token("7154304328:AAFXIXAGxQG9b8Myu9U4HygI_T2BDSEoTJI").build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex(r'^افريقيا$'), africa))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))
    
    application.run_polling()

if __name__ == '__main__':
    main()
