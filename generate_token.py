import os
from dotenv import load_dotenv
from livekit.agents import cli

load_dotenv()

# Get credentials from .env file
api_key = os.environ.get('LIVEKIT_API_KEY')
api_secret = os.environ.get('LIVEKIT_API_SECRET')

# Choose a room name
room_name = "my-test-room"
participant_name = "user1"

# Generate token using the cli module which handles version compatibility
token = cli.generate_token(
    room_name=room_name,
    identity=participant_name,
    api_key=api_key,
    api_secret=api_secret
)

# Print the information
print("\nRoom Name:", room_name)
print("\nYour LiveKit Token:")
print(token)
print("\nWebSocket URL:", os.environ.get('LIVEKIT_URL'))
print("\nFor Manual Connection in Playground:")
print("1. URL field:", os.environ.get('LIVEKIT_URL'))
print("2. Token field: (Copy the token above)") 