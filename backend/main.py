from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import sys
from pathlib import Path
import numpy as np
import faiss
from fastapi import APIRouter

# Add the backend directory to Python path
backend_dir = Path(__file__).resolve().parent
if str(backend_dir) not in sys.path:
    sys.path.append(str(backend_dir))

from services.llm_parser import parse_query
from services.embeddings import get_embeddings
from services.search import find_similar_documents
from data.mock_data import mock_data

load_dotenv()

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchQuery(BaseModel):
    query: str

class MatchResponse(BaseModel):
    matches: list
    explanation: str

@app.post("/search", response_model=MatchResponse)
async def search(query: SearchQuery):
    try:
        # Step 1: Parse natural language query into filters
        filter_query = parse_query(query.query)
        
        if not filter_query:
            raise HTTPException(status_code=400, detail="Could not parse query")

        if not filter_query.get('interests') and not filter_query.get('vibe'):
            raise HTTPException(status_code=400, detail="No interests or vibe found in query")

        # Step 2: Convert query and mock data to text embeddings
        try:
            # Prepare query text
            interests = ", ".join(filter_query.get('interests', []))
            vibe = filter_query.get('vibe', '')
            query_text = f"Interests: {interests}. Vibe: {vibe}"

            # Prepare mock data texts
            mock_texts = [
                f"Interests: {', '.join(user['interests'])}. Vibe: {user['vibe']}"
                for user in mock_data
            ]

            # Generate embeddings
            query_embedding = get_embeddings([query_text])[0]
            mock_embeddings = get_embeddings(mock_texts)

        except Exception as e:
            print(f"Error generating embeddings: {e}")
            raise HTTPException(status_code=500, detail="Error generating embeddings")

        try:
            # Create FAISS index
            embeddings = np.array(mock_embeddings).astype('float32')
            dimension = len(query_embedding)
            index = faiss.IndexFlatL2(dimension)
            index.add(embeddings)

            # Find similar profiles
            match_indices = find_similar_documents(query_embedding, index)
            
            if not match_indices:
                return {
                    "matches": [],
                    "explanation": "No matches found for your query"
                }

            matches = [mock_data[idx] for idx in match_indices if idx < len(mock_data)]

        except Exception as e:
            print(f"Error performing similarity search: {e}")
            raise HTTPException(status_code=500, detail="Error performing similarity search")

        # Generate explanation
        interests_str = ", ".join(filter_query.get('interests', []))
        vibe_str = filter_query.get('vibe', 'general')
        explanation = (
            f"Found {len(matches)} matches based on "
            f"{'interests: ' + interests_str if interests_str else ''}"
            f"{' and ' if interests_str and vibe_str else ''}"
            f"{'vibe: ' + vibe_str if vibe_str else ''}"
        )
        
        return {
            "matches": matches,
            "explanation": explanation
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

app.include_router(router)