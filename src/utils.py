import numpy as np
import numpy.typing as npt


def batch_cosine_similarity(
    query_vec: npt.NDArray[np.float32], doc_vecs: npt.NDArray[np.float32]
) -> npt.NDArray[np.float32]:
    dot_products: npt.NDArray[np.float32] = np.dot(doc_vecs, query_vec)
    norm_query_vec: np.float32 = np.linalg.norm(query_vec)
    norm_doc_vecs: np.float32 = np.linalg.norm(doc_vecs, axis=1)
    return dot_products / (norm_query_vec * norm_doc_vecs)
