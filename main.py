from config import OPENAI_API_KEY,GEMINI_API_KEY
from prompt_utils import GeminiModel
from rag_model import RAGModel
#import openai

def main():
    print("start")
    g1 = GeminiModel(GEMINI_API_KEY)
    res=g1.send_prompt("what is the whether today in israel?")
    print(res)
    #openai.api_key = OPENAI_API_KEY

    # Example usage of direct prompting
    """
    prompt = create_structured_prompt(
        context="The Earth orbits around the Sun.",
        question="What is the relationship between the Earth and the Sun?"
    )
    response = send_prompt(prompt)
    print("Direct Prompt Response:", response)
    
    # Example usage of RAG model
    documents = [
        "The Earth is the third planet from the Sun.",
        "Mars is often called the Red Planet.",
        "Jupiter is the largest planet in our solar system."
    ]
    rag = RAGModel(documents)
    rag_response = rag.query("What color is Mars often described as?")
    print("RAG Model Response:", rag_response)
"""
if __name__ == "__main__":
    main()
