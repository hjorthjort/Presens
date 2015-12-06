import alchemyapi_python.alchemyapi

class alchemy:

    def __init__(self):
        self.api_connection = alchemyapi_python.alchemyapi.AlchemyAPI()


    def find_keywords(self, text):
        return self.api_connection.keywords("text", text, {'keywordExtractMode': 'strict'})