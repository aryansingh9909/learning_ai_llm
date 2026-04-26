"""
This script is used to generate text using the Gemini API with a system instruction.
"""

from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3-flash-preview"
thinking_level = "low"

# System instruction
system_instruction = "You are a software developer. share your experience in the product-based company."

# Contents
contents = "What is the experience of working in the product-based company?"

# Generate content
response = client.models.generate_content(
    model=model,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        thinking_config=types.ThinkingConfig(thinking_level=thinking_level)
    ),
    contents=contents
)

print(response.text)
