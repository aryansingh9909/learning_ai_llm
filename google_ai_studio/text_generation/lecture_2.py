"""
This script is used to generate text using the Gemini API with thinking.
"""

from google import genai
from google.genai import types

client = genai.Client()

contents = "How does AI work?"
thinking_level = "low"
model = "gemini-3-flash-preview"


response = client.models.generate_content(
    model=model,
    contents=contents,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level=thinking_level)
    ),
)

print(response.text)
