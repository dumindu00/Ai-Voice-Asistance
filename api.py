from livekit.agents import llm
import enum
from typing import Annotated
import logging
from db_driver import DatabaseDriver








class AssistantFnc(llm.FunctionContext):
    def __init__(self):
        super().__init__()