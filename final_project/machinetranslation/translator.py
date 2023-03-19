import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

version = '2018-05-01'
authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{version}',
    authenticator=authenticator
)
language_translator.set_disable_ssl_verification(True)
language_translator.set_service_url(f'{url}')

def englishToFrench(englishText):
    #write the code here
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    print(json.dumps(frenchText, indent=2, ensure_ascii=False))    
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    englishText = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    print(json.dumps(englishText, indent=2, ensure_ascii=False))   
    return englishText

englishToFrench("Hello, how are you")
frenchToEnglish("Bonjour")