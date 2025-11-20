from __future__ import annotations
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    cli,
    llm
)
from livekit.agents.multimodal import MultimodalAgent
from livekit.plugins import google
from livekit.plugins import google
from dotenv import load_dotenv
from api import AssistantFnc
import os
from prompts import WELCOME_MESSAGE, INSTRUCTION

from livekit.agents import AgentSession



load_dotenv()


async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)       # waited for connect into the room
    await ctx.wait_for_participant()                   
    
    
    model = google.realtime.RealtimeModel(       
        instructions="INSTRUCTION",
        voice="Charon",
        temperature=0.8,
        modalities=["audio", "text"]
    )
    assistant_fnc = AssistantFnc()
    assistant = MultimodalAgent(model=model, fnc_ctx=assistant_fnc)  
    assistant.start(ctx.room)
    
    
    session = model.sessions[0]
    session.conversation.item.create(
        llm.ChatMessage(
            role="assistant",
            content="WELCOME_MESSAGE"
        )
    )
    
    
#     session = AgentSession(
#     llm=google.realtime.RealtimeModel(
#         model="gemini-2.0-flash-exp",
#         voice="Puck",
#         temperature=0.8,
#         instructions=INSTRUCTION,
#     ),
# )
    
    
    
    
    session.response.create()
    
if __name__=="__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
    
    