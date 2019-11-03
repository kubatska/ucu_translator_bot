from googletrans import Translator
from google.cloud import translate


def translate_text(text, lang):
    translate_client = translate.Client()
    # text = u'hi'
    target = lang
    translation = translate_client.translate(
        text,
        target_language=target)
    return translation["translatedText"].replace("&#39;", "`")
