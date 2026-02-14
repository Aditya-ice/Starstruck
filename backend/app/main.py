from fastapi import FastAPI
from app.api import router

app = FastAPI(title="CupidGraph AI Coach")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

from app.models import UserProfile, CoachingResponse
from app.graph.workflow import app_graph

# In-memory graph runner (for now)
@app.post("/coach", response_model=CoachingResponse)
async def generate_coaching(user_a: UserProfile, user_b: UserProfile):
    # Initialize state
    initial_state = {"user_a": user_a, "user_b": user_b}
    
    # Run graph
    result = await app_graph.ainvoke(initial_state)
    
    return result["advice"]
