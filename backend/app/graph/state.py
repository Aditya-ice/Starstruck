from typing import TypedDict, Annotated
from app.models import UserProfile, CoachingResponse

class AgentState(TypedDict):
    user_a: UserProfile
    user_b: UserProfile
    advice: Annotated[CoachingResponse, "The final coaching output"]
