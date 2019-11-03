from telebot import types
import translate_text


def create_item(number, text, text_to_translate, lang):
    if lang == "":
        try:
            lang = text_to_translate[:2].lower()
            r = types.InlineQueryResultArticle(
                number, text, types.InputTextMessageContent(translate_text.translate_text(text_to_translate[2:], lang)))
            return r
        except:
            text_to_translate = "<Translation failed>"
            lang = "en"

    r = types.InlineQueryResultArticle(
        number, text, types.InputTextMessageContent(translate_text.translate_text(text_to_translate, lang)))
    return r
