from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

class sentiment:
    def analyse(self, string, lang = 'fr'):
        client = language.LanguageServiceClient()
        document = types.Document(content=string,type=enums.Document.Type.PLAIN_TEXT, language=lang)
        annotations = client.analyze_sentiment(document=document)
        score = annotations.document_sentiment.score
        return score
