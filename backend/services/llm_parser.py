from typing import Dict, Any

def parse_query(query: str) -> Dict[str, Any]:
    """
    Parse the query string into structured format using keyword matching.
    """
    query = query.lower()
    result = {
        "interests": [],
        "vibe": ""
    }
    
    # Common interests from our mock data
    interests = ["film", "hiking", "philosophy", "ai", "ethics", "cats",
                "music", "painting", "art", "entrepreneurship", "jazz",
                "writing", "baking"]
    
    # Extract interests
    for interest in interests:
        if interest in query:
            result["interests"].append(interest)
    
    # Extract vibe
    vibe_keywords = {
        "tarantino": "quirky, introspective",
        "analytical": "analytical, dry humor",
        "bohemian": "bohemian, artistic",
        "intense": "intense, focused",
        "melancholic": "melancholic, thoughtful"
    }
    
    for keyword, vibe in vibe_keywords.items():
        if keyword in query:
            result["vibe"] = vibe
            break
    
    # If no specific vibe found, use a general one
    if not result["vibe"]:
        result["vibe"] = "general"
        
    return result
