import os
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from app.models import CoachingResponse
from app.graph.state import AgentState

# Initialize Claude text model
llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.7)

# System Prompt
SYSTEM_PROMPT = """You are CupidGraph, an elite, data-driven dating coach.
Your goal is to analyze two user profiles and generate a hyper-personalized briefing card for a date.

Your style is:
- Analytical yet witty.
- Specific: Cite specific artists, movies, or repos.
- Constructive: Give actionable advice.

Input Data:
User A (The user receiving advice): {user_a}
User B (The match): {user_b}

Task:
Generate a coaching response that includes:
1. Match Intel: Why they overlap.
2. Conversation Starters: Specific hooks.
3. Minefield Map: Topics to avoid (e.g., conflicting politics or rival coding frameworks).
4. Venue Advice: A specific type of place.
5. Vibe/Outfit: Aesthetic advice.

Output MUST be a valid JSON object matching the CoachingResponse schema.
"""

def coach_node(state: AgentState):
    user_a = state["user_a"]
    user_b = state["user_b"]
    
    parser = PydanticOutputParser(pydantic_object=CoachingResponse)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "Analyze these profiles and generate the briefing.")
    ])
    
    chain = prompt | llm | parser
    
    # Format inputs as string representations for the prompt
    response = chain.invoke({
        "user_a": user_a.model_dump_json(indent=2),
        "user_b": user_b.model_dump_json(indent=2)
    })
    
    return {"advice": response}
