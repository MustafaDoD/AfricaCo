import random
from queue import Queue
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

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
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('هلو! ارسلي "افريقيا" عشان تبدي التحدي •-•.')

# وظيفة للتحدي
def africa(update: Update, context: CallbackContext) -> None:
    country = random.choice(list(countries_capitals.keys()))
    context.user_data['country'] = country
    update.message.reply_text(f'ما هي عاصمة {country}?')

# وظيفة للتحقق من الإجابة
def check_answer(update: Update, context: CallbackContext) -> None:
    country = context.user_data.get('country')
    if country:
        capital = countries_capitals[country]
        if update.message.text == capital:
            update.message.reply_text('صحييييح ترربيييتي😼!')
        else:
            update.message.reply_text(f'نوووب خطأ. العاصمة الصحيحة هي {capital}.')
        del context.user_data['country']
    else:
        update.message.reply_text('ارسلي "افريقيا" لبدء التحدي.')

def main() -> None:
    # Create the update queue
    update_queue = Queue()
    
    # Initialize the Updater with the token and update queue
    updater = Updater("7154304328:AAFXIXAGxQG9b8Myu9U4HygI_T2BDSEoTJI", update_queue=update_queue)
    
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'^افريقيا$'), africa))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, check_answer))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
