from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
import torch

# Initialize the model
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    print(f"Error loading model: {e}")
    raise

def get_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for a list of texts using the SentenceTransformer model.
    
    Args:
        texts (List[str]): List of texts to generate embeddings for
        
    Returns:
        List[List[float]]: List of embedding vectors
    """
    try:
        if not texts or not all(isinstance(t, str) for t in texts):
            raise ValueError("Input must be a non-empty list of strings")

        # Generate embeddings
        with torch.no_grad():
            embeddings = model.encode(
                texts,
                convert_to_tensor=True,
                show_progress_bar=False,
                normalize_embeddings=True
            )
            
        # Convert to numpy and then to list
        if torch.is_tensor(embeddings):
            embeddings = embeddings.cpu().numpy()
            
        return embeddings.tolist()
        
    except Exception as e:
        print(f"Error generating embeddings: {e}")
        raise