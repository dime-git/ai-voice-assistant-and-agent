"""
LiveKit Voice Assistant Main Application.

This script initializes and runs a voice assistant powered by LiveKit Agents framework.
The assistant can understand natural language, respond with voice, and control
temperature settings via custom function calls.
"""

import asyncio

from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero
from api import AssistantFnc

# Load environment variables from .env file (API keys, LiveKit credentials)
load_dotenv()


async def entrypoint(ctx: JobContext):
    """
    Main entrypoint function for the voice assistant agent.
    
    This function sets up the voice assistant with speech-to-text, text-to-speech,
    language model capabilities, and function context for temperature control.
    It initializes the connection to LiveKit, starts the assistant, and sends
    an initial greeting.
    
    Args:
        ctx (JobContext): The job context provided by LiveKit Agents framework,
                          containing connection details and room information.
    """
    # Configure system prompt for the assistant's personality and behavior
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant created by LiveKit. Your interface with users will be voice. "
            "You should use short and concise responses, and avoiding usage of unpronouncable punctuation."
        ),
    )
    
    # Connect to the LiveKit room with audio subscription
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    
    # Initialize the function context for temperature control capabilities
    fnc_ctx = AssistantFnc()

    # Create the voice assistant with all required components
    assistant = VoiceAssistant(
        # Voice Activity Detection model for detecting when user is speaking
        vad=silero.VAD.load(),
        # Speech-to-Text for converting user's voice to text
        stt=openai.STT(),
        # Language Model for generating responses
        llm=openai.LLM(),
        # Text-to-Speech for converting assistant's responses to voice
        tts=openai.TTS(),
        # Chat context with system instructions
        chat_ctx=initial_ctx,
        # Function context with temperature control capabilities
        fnc_ctx=fnc_ctx,
    )
    
    # Start the assistant in the LiveKit room
    assistant.start(ctx.room)

    # Wait briefly to ensure connection is established
    await asyncio.sleep(1)
    
    # Send an initial greeting to the user
    await assistant.say("Hey, how can I help you today!", allow_interruptions=True)


if __name__ == "__main__":
    # Run the application with the configured entrypoint
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))