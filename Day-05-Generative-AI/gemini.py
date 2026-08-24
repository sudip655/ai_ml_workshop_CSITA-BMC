import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "Set the GEMINI_API_KEY environment variable before running this program."
    )

client = genai.Client(api_key=api_key)

TRIAGE_PROMPT = """You are a helpful AI assistant.
Answer the user's questions clearly and simply.
If the user has a technical problem, provide7
clear step-by-step troubleshooting instructions.
"""


def triage(symptom_description):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=symptom_description,
        config=types.GenerateContentConfig(
            system_instruction=TRIAGE_PROMPT
        )
    )
    return response.text


print(triage("My phone is not turning on. What should I do?"))