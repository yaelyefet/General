
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
"""
def send_prompt(prompt, max_tokens=150):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

def create_structured_prompt(context, question):
    return fContext: {context}

Question: {question}

Please provide a detailed answer based on the given context:"""




class GeminiModel:
    def __init__(self,api_key):
        genai.configure(api_key=api_key)
        self.generation_config = {
        #"temperature": 1,
        #"top_p": 0.95,
        #"top_k": 40,
        #"max_output_tokens": 8192,
        }
        self.model = genai.GenerativeModel(
            #model_name="gemini-1.5-flash",
            #model_name="gemini-1.5-pro",
            model_name="gemini-2.0-flash-thinking-exp-1219",#"gemini-2.0-flash-exp",#"gemini-2.0-flash-thinking-exp-1219",#"gemini-2.0-flash-exp",#
            generation_config=self.generation_config,
            # safety_settings = Adjust safety settings
            # See https://ai.google.dev/gemini-api/docs/safety-settings
        )
        self.chat= self.model.start_chat(history=[])
       

    def send_prompt(self,prompt, max_tokens=150):
        response = self.chat.send_message(prompt)    
        return response.text

    def create_structured_prompt(context, question):
        return f"""Context: {context}
                Question: {question}"""

