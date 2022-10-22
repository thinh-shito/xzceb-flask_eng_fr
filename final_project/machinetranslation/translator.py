import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version = '2028-05-01',
    authenticator = authenticator
    )

translator.set_service_url(url)

def english_to_french(english_text):
    '''
        Translate english to french
    '''
    try:
        french_text = translator.translate(
                        english_text, model_id='en-fr'
                        ).get_result()

        return french_text["translations"][0]["translation"]
    except:
        return None


def french_to_english(french_text):
    '''
        Translate french to english
    '''
    try:
        english_text = translator.translate(
                        french_text, model_id='fr-en'
                        ).get_result()

        return english_text["translations"][0]["translation"]
    except:
        return None