import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    x = np.random.rand(data.shape[1])
    for i in range(num_steps):
        x = np.dot(data, x)
        x /= np.linalg.norm(x)
    l = float(np.dot(np.dot(data, x), x))
    return l, x

 