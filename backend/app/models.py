from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    name: str = Field(..., description="Name of the user")
    music_tastes: List[str] = Field(default_factory=list, description="Top genres/artists from Spotify")
    movie_ratings: List[Dict] = Field(default_factory=list, description="Recent ratings from Letterboxd")
    coding_style: Dict = Field(default_factory=dict, description="GitHub metrics")
    professional_profile: Dict = Field(default_factory=dict, description="LinkedIn summary and skills")
    personality_traits: List[str] = Field(default_factory=list, description="Derived personality traits")

class CoachingResponse(BaseModel):
    match_intel: str = Field(..., description="Why these two matched")
    conversation_starters: List[str] = Field(..., description="Top 5 specific openers")
    topics_to_avoid: List[str] = Field(..., description="Topics that might cause friction")
    venue_advice: str = Field(..., description="Where to go and why")
    outfit_suggestion: str = Field(..., description="Vibe check for outfit")
