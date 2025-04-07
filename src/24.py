import numpy as np

def sample_data(num_samples):
    """
    Generate a sample of data.
    
    Args:
        num_samples (int): Number of samples to generate.
        
    Returns:
        np.array: A 1D array representing the generated data.
    """
    # Assuming a uniform distribution for demonstration purposes
    data = np.random.uniform(0, 100, num_samples)
    return data

# Example usage
sampled_data = sample_data(10000)
print(sampled_data)
