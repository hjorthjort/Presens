import alchemyapi


class alchemy:

    def __init__(self):
        self.api_connection = alchemyapi.AlchemyAPI()


    def find_keywords(self, text):
        return self.api_connection.keywords("text", text, {'showSourceText': 0})