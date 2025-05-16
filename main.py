from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

import os
import json
import openai  # ✅ This was missing!

# Load variables from .env file
load_dotenv()

# Initialize OpenAI client using the new v1 API
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SignalInput(BaseModel):
    message: str

@app.post("/score-signal")
async def score_signal(payload: SignalInput):
    try:
        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that classifies customer feedback into a structured JSON response."
                },
                {
                    "role": "user",
                    "content": f"""Classify the following customer message and return only JSON in this format:

{{
  "sentiment": "...",
  "customerTier": "...",
  "summary": "..."
}}

Message: "{payload.message}"
"""
                }
            ],
            temperature=0.2,
            max_tokens=150
        )

        content = chat_response.choices[0].message.content.strip()
        return json.loads(content)

    except Exception as e:
        return {"error": str(e)}

class SignalInput(BaseModel):
    message: str

@app.post("/score-signal")
async def score_signal(payload: SignalInput):
    try:
        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that classifies customer feedback into a structured JSON response."
                },
                {
                    "role": "user",
                    "content": f"""Classify the following customer message and return only JSON in this format:

{{
  "sentiment": "...",
  "customerTier": "...",
  "summary": "..."
}}

Message: "{payload.message}"
"""
                }
            ],
            temperature=0.2,
            max_tokens=150
        )

        content = chat_response.choices[0].message.content.strip()
        return json.loads(content)

    except Exception as e:
        return {"error": str(e)}
