# CupidGraph Backend

## Setup
1. Install dependencies:
   ```bash
   cd backend
   pip install poetry
   poetry install
   ```
2. Set up environment variables:
   Copy `.env.example` to `.env` and add your `ANTHROPIC_API_KEY`.

## Running the API
```bash
poetry run uvicorn app.main:app --reload
```

## Verifying the Coach
Run the verification script to generate a sample coaching response:
```bash
poetry run python verify_coach.py
```
