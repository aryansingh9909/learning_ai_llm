"""
This script is used to generate text using the Gemini API with a chat and stream.
"""

from google import genai

# Create a chat client
client = genai.Client()
chat = client.chats.create(model="gemini-3-flash-preview")

# Send a message to the chat
response = chat.send_message_stream("I have 2 dogs in my house.")
for chunk in response:
    print(chunk.text, end="")

# Send a message to the chat
response = chat.send_message_stream("How many paws are in my house?")
for chunk in response:
    print(chunk.text, end="")

# Get the history of the chat
for message in chat.get_history():
    print(f'role - {message.role}', end=": ")
    print(message.parts[0].text)
