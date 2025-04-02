import os
from dotenv import load_dotenv

# Load environment variables from .env file
print("Attempting to load .env file...")
load_dotenv()

# Check if environment variables are loaded
print("\nEnvironment Variables:")
print(f"LIVEKIT_URL: {os.environ.get('LIVEKIT_URL')}")
print(f"LIVEKIT_API_KEY: {os.environ.get('LIVEKIT_API_KEY')}")
print(f"LIVEKIT_API_SECRET: {os.environ.get('LIVEKIT_API_SECRET', '[Secret masked for security]')}")
print(f"OPENAI_API_KEY: {os.environ.get('OPENAI_API_KEY', '[Secret masked for security]')[:10]}...")

# Check if the values match what's in the .env file
with open('.env', 'r') as f:
    env_content = f.read()
    print("\nContent of .env file:")
    print(env_content)

print("\nIf the environment variables above don't match the content of the .env file,")
print("then there might be an issue with loading the environment variables.") 