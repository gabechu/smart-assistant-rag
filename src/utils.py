import numpy as np


def batch_cosine_similarity(query_vec: np.ndarray, doc_vecs: np.ndarray) -> np.ndarray:
    dot_products = np.dot(doc_vecs, query_vec)
    norm_query_vec = np.linalg.norm(query_vec)
    norm_doc_vecs = np.linalg.norm(doc_vecs, axis=1)
    return dot_products / (norm_query_vec * norm_doc_vecs)
