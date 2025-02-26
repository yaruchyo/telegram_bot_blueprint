from google import genai
from dotenv import load_dotenv

load_dotenv()

class GeminiLLM:
    def __init__(self, GEMINI_API_KEY):

        self.model_name = 'gemini-2.0-flash'
        self.config = genai.types.GenerateContentConfig(
            temperature=1,
            system_instruction="Generate the answer within 750 characters."
        )

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_llm_answer(self, input_message):

        response = self.client.models.generate_content(
            model=self.model_name,
            config=self.config,
            contents=input_message
        )
        return response.text

    def generate_llm_answer_json(
            self,
            input_message: str,
            translation_class
    ):

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=input_message,

            config={
                'response_mime_type': 'application/json',
                'response_schema': translation_class
            },
        )

        # Use instantiated objects.
        my_recipes: translation_class = response.parsed

        return my_recipes


if __name__ == "__main__":
    llm = GEMINI_LLM()
    answer = llm.generate_llm_answer()
    print(answer)