import os
from dotenv import load_dotenv
from google import genai
from src.vectorization import Vectorizer
from src.retriever import mainRetriever

vc = Vectorizer()


vector_db = vc.hfembedder()
mnr = mainRetriever()

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
while True:
    question = input("Question: ").strip()
    if question.lower() in ["exit", "quit"]:
        print("Stopped.")
        break
    context = mnr.TopKRetriever(question, vector_db, 3)
    sysprompt=f'''
    You are as Senior Ai model advisor
    You have to give the response in more technical
    Response by using the Context efficiently
    this is user query {question} and this is 
    context {context} you have to say response 
    in small general explanation with key important details.
    '''


    response = client.models.generate_content(
        model="gemini-3.1-flash-lite", contents=sysprompt
    )
    print("\nGemini Response\n")
    print(response.text)
