from __future__ import annotations
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    cli,
    llm
)
from livekit.agents.multimodal import MultimodalAgent
from livekit.agents import MultimodalAgent

from livekit.plugins import google
from dotenv import load_dotenv
from api import AssistantFnc
import os

load_dotenv()


async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)
    await ctx.wait_for_participant(
        model = google.realtime.RealtimeModel(
            instructions="",
            voice="Charon",
            temperature=0.8,
            modalities=["audio", "text"]
        )
        assistant_fnc = AssistantFnc()
        assistant = MultimodalAgent(model=model, fnc_ctx=assistant_fnc)  
    )