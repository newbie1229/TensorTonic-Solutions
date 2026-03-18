import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    numerator = np.dot(a,b)
    denorminator = np.linalg.norm(a) * np.linalg.norm(b)
    if denorminator==0:
        return 0
    return numerator/denorminator