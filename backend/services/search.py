import faiss
import numpy as np
from typing import Tuple, List

def find_similar_documents(query_embedding: np.ndarray, index: faiss.Index, k: int = 3) -> List[int]:
    """
    Find the top k most similar documents to the given embedding using FAISS.

    Args:
        query_embedding (np.ndarray): The embedding vector of the query document
        index (faiss.Index): The FAISS index containing the document embeddings
        k (int): The number of similar documents to retrieve

    Returns:
        List[int]: A list of indices of the top k most similar documents
    """
    try:
        # Convert to numpy array if not already
        if not isinstance(query_embedding, np.ndarray):
            query_embedding = np.array(query_embedding)

        # Ensure the embedding is 2D and float32
        if len(query_embedding.shape) == 1:
            query_embedding = query_embedding.reshape(1, -1)
        query_embedding = query_embedding.astype('float32')

        # Verify dimensions match
        if query_embedding.shape[1] != index.d:
            raise ValueError(f"Query embedding dimension {query_embedding.shape[1]} does not match index dimension {index.d}")

        # Adjust k if it's larger than the number of entries in the index
        k = min(k, index.ntotal)
        
        # Search for the top k nearest neighbors
        distances, indices = index.search(query_embedding, k)
        
        # Convert to Python list and return just the indices
        return indices[0].tolist()

    except Exception as e:
        print(f"Error in find_similar_documents: {str(e)}")
        return []