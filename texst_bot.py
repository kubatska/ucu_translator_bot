import telebot
from telebot import types
import translate_text

API_TOKEN = '//'

bot = telebot.TeleBot(API_TOKEN)

@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    try:
        r0 = create_item("1", "Manual language", query.query, "")
        r1 = create_item("2", "Українська", query.query, "uk")
        r2 = create_item("3", "English", query.query, "en")
        r3 = create_item("4", "Francias", query.query, "fr")
        r4 = create_item("5", "Espanol", query.query, "es")

        bot.answer_inline_query(query.id, [r0, r1, r2, r3, r4])
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: len(query.query) is 0)
def default_query(inline_query):
    try:
        r = types.InlineQueryResultArticle(
            '1', 'Type your text', types.InputTextMessageContent("hi"))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

def create_item(number, text, text_to_translate, lang):
    if lang == "":
        try:
            lang = text_to_translate[:2].lower()
            types.InlineQueryResultArticle(
            number, text, types.InputTextMessageContent(translate_text.translate_text(text_to_translate[2:], lang)))
        except:
            text_to_translate = "<Translation failed>"
            lang = "en"

    r = types.InlineQueryResultArticle(
            number, text, types.InputTextMessageContent(translate_text.translate_text(text_to_translate, lang)))
    return r

    

def main_loop():
    bot.polling(True)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        exit(0)
