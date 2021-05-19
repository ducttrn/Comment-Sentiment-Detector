from google_trans_new import google_translator
from langdetect import detect

from main.configs import config


def translate_to_training_language(text: str):
    translator = google_translator()
    translate_text = translator.translate(
        text, lang_tgt=config.TRAINING_LANGUAGE, lang_src=detect(text)
    )

    return translate_text
