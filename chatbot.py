from dotenv import load_dotenv
import openai
import os

# Load the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(user_input):
    """
    Sends user input to OpenAI's API and gets the response.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the OpenAI model
        messages=[{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    print("Welcome to Ivvy Chatbot!")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print(f"Ivvy: {get_response(user_input)}")
