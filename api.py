"""
Temperature Control API Module.

This module provides a function context for the voice assistant to control temperature
settings across different zones of a smart home environment. It enables retrieving and
modifying temperature values through AI callable functions.
"""

import enum
from typing import Annotated
from livekit.agents import llm
import logging

# Configure logger for temperature control operations
logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)


class Zone(enum.Enum):
    """
    Enumeration of available zones in the smart home environment.
    
    Each zone represents a distinct area where temperature can be monitored and controlled.
    Values are represented as snake_case strings for consistent API interaction.
    """
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"


class AssistantFnc(llm.FunctionContext):
    """
    Function context providing temperature control capabilities for the voice assistant.
    
    This class extends the LiveKit Agents FunctionContext to provide temperature
    monitoring and control functions that can be called by the LLM during conversations.
    """
    def __init__(self) -> None:
        """
        Initialize the Assistant Function Context with default temperature values.
        
        Sets up initial temperature values (in Celsius) for all available zones.
        """
        super().__init__()

        # Default temperature values for each zone in Celsius
        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 24,
            Zone.BATHROOM: 23,
            Zone.OFFICE: 21,
        }

    
    @llm.ai_callable(description="get the temperature in a specific room")
    def get_temperature(
        self, zone: Annotated[Zone, llm.TypeInfo(description="The specific zone")]
    ):
        """
        Retrieve the current temperature for a specified zone.
        
        Args:
            zone (Zone): The zone for which to retrieve the temperature.
                         Must be one of the predefined Zone enum values.
        
        Returns:
            str: A formatted string with the zone name and current temperature in Celsius.
        """
        logger.info("get temp - zone %s", zone)
        temp = self._temperature[Zone(zone)]
        return f"The temperature in the {zone} is {temp}C"

    @llm.ai_callable(description="set the temperature in a specific room")
    def set_temperature(
        self,
        zone: Annotated[Zone, llm.TypeInfo(description="The specific zone")],
        temp: Annotated[int, llm.TypeInfo(description="The temperature to set")],
    ):
        """
        Set a new temperature for a specified zone.
        
        Args:
            zone (Zone): The zone for which to set the temperature.
                         Must be one of the predefined Zone enum values.
            temp (int): The temperature value to set in Celsius.
        
        Returns:
            str: A formatted confirmation string with the zone name and new temperature.
        """
        logger.info("set temo - zone %s, temp: %s", zone, temp)
        self._temperature[Zone(zone)] = temp
        return f"The temperature in the {zone} is now {temp}C"