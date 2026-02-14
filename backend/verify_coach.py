import asyncio
import os
from dotenv import load_dotenv
from app.models import UserProfile
from app.graph.workflow import app_graph

# Load env (make sure .env exists with ANTHROPIC_API_KEY)
load_dotenv()

async def main():
    print("🚀 Starting AI Coach Verification...")
    
    # Mock Data
    alice = UserProfile(
        name="Alice",
        music_tastes=["Indie Pop", "Alt Rock", "Phoebe Bridgers", "The National"],
        movie_ratings=[
            {"title": "Everything Everywhere All At Once", "rating": 5},
            {"title": "Her", "rating": 4.5}
        ],
        coding_style={"languages": ["Python", "TypeScript"], "commits_per_week": 15},
        professional_profile={"title": "Senior Software Engineer", "skills": ["System Design", "React"]},
        personality_traits=["Creative", "Introspective", "Empathetic"]
    )

    bob = UserProfile(
        name="Bob",
        music_tastes=["Classic Rock", "Jazz", "Radiohead", "Miles Davis"],
        movie_ratings=[
            {"title": "Inception", "rating": 5},
            {"title": "Her", "rating": 5}
        ],
        coding_style={"languages": ["Rust", "Go"], "commits_per_week": 40},
        professional_profile={"title": "Backend Developer", "skills": ["Distributed Systems", "Rust"]},
        personality_traits=["Logical", "Driven", "Audiophile"]
    )

    print(f"Analyzing match: {alice.name} + {bob.name}...")
    
    try:
        result = await app_graph.ainvoke({"user_a": alice, "user_b": bob})
        advice = result["advice"]
        
        print("\n✅ Coaching Advice Generated Successfully!")
        print("-" * 50)
        print(f"🎯 Match Intel: {advice.match_intel}")
        print(f"💬 Opener: {advice.conversation_starters[0]}")
        print(f"🚫 Avoid: {advice.topics_to_avoid[0]}")
        print(f"📍 Venue: {advice.venue_advice}")
        print(f"👔 Outfit: {advice.outfit_suggestion}")
        print("-" * 50)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
