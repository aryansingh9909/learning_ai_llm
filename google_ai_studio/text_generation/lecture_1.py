"""
This script is used to generate text using the Gemini API.
"""

from google import genai


# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

# Generate content using the model "gemini-3-flash-preview"
response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents="Explain how AI works in a few words"
)


text = response.text
response_id = getattr(response, "response_id", None)
model_version = getattr(response, "model_version", None)

candidates = getattr(response, "candidates", None) or []
finish_reason = getattr(candidates[0], "finish_reason", None) if candidates else None

usage = getattr(response, "usage_metadata", None)
prompt_tokens = getattr(usage, "prompt_token_count", None) if usage else None
output_tokens = getattr(usage, "candidates_token_count", None) if usage else None
total_tokens = getattr(usage, "total_token_count", None) if usage else None
thoughts_tokens = getattr(usage, "thoughts_token_count", None) if usage else None


# Print the response
print("text:", text)
print("response_id:", response_id)
print("model_version:", model_version)
print("finish_reason:", finish_reason)
print(
    "tokens:",
    {"prompt": prompt_tokens, "output": output_tokens, "thoughts": thoughts_tokens, "total": total_tokens},
)
