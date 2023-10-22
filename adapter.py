class EnglishTextService:
    def translate_to_english(self, text):
        return text

class FrenchTextService:
    def translate_to_french(self, text):
        pass


class EnglishToFrenchAdapter(FrenchTextService):
    def __init__(self, english_text_service):
        self.english_text_service = english_text_service

    def translate_to_french(self, text):
        english_text = self.english_text_service.translate_to_english(text)
        french_text = self.perform_translation(english_text)
        return french_text

    def perform_translation(self, english_text):
        return "Translated to French: " + english_text

def main():
    english_text_service = EnglishTextService()
    english_to_french_adapter = EnglishToFrenchAdapter(english_text_service)
    user_input = input("Enter English text: ")
    french_text = english_to_french_adapter.translate_to_french(user_input)
    print(french_text)

if __name__ == "__main__":
    main()
