"""
This script is used to generate text using the Gemini API with a chat.
"""

from google import genai


# Create a chat client
client = genai.Client()

# Create a chat client
chat = client.chats.create(model="gemini-3-flash-preview")

# Send a message to the chat
response = chat.send_message("I have 2 dogs in my house.")
print(response.text)

# Send a message to the chat
response = chat.send_message("How many paws are in my house?")
print(response.text)

# Get the history of the chat
for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)
