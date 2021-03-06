from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os

credential_path = "/home/api/secret.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

class sentiment:
    def analyse(self, string, lang = 'fr'):
        client = language.LanguageServiceClient()
        document = types.Document(content=string,type=enums.Document.Type.PLAIN_TEXT, language=lang)
        annotations = client.analyze_sentiment(document=document)
        score = annotations.document_sentiment.score
        return score
