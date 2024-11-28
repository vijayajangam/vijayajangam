import numpy as np

def sigmoid(x):
    """Sigmoid activation function."""
    return 1 / (1 + np.exp(-x))

def perceptron(weights, feature_vector, use_sigmoid=True):
    """
    Implements a perceptron with weighted summation followed by an activation function.
    
    Parameters:
        weights (list): List of weights for the perceptron.
        feature_vector (list): Input feature vector.
        use_sigmoid (bool): Flag to use sigmoid activation or threshold.
        
    Returns:
        output (float): The output of the perceptron after activation.
    """
    # Calculate weighted sum
    weighted_sum = np.dot(weights, feature_vector)
    
    if use_sigmoid:
        # Apply sigmoid activation function
        output = sigmoid(weighted_sum)
    else:
        # Apply threshold activation function
        threshold = 0.5
        output = 1 if weighted_sum >= threshold else 0
    
    return output

def euclidean_distance(vec1, vec2):
    """
    Calculates the Euclidean distance between two vectors.
    
    Parameters:
        vec1 (list): First vector.
        vec2 (list): Second vector.
        
    Returns:
        distance (float): The Euclidean distance between vec1 and vec2.
    """
    return np.sqrt(np.sum((np.array(vec1) - np.array(vec2)) ** 2))

# User input for perceptron
weights_input = input("Enter weights separated by spaces: ")
weights = list(map(float, weights_input.split()))

feature_vector_input = input("Enter feature vector separated by spaces: ")
feature_vector = list(map(float, feature_vector_input.split()))

# User choice for activation function
activation_choice = input("Use sigmoid activation? (yes/no): ").strip().lower()
use_sigmoid = True if activation_choice == 'yes' else False

# Calculate perceptron output
output = perceptron(weights, feature_vector, use_sigmoid)
print(f"Perceptron output: {output}")

# User input for Euclidean distance calculation
vec1_input = input("Enter first vector for distance calculation (separated by spaces): ")
vec1 = list(map(float, vec1_input.split()))

vec2_input = input("Enter second vector for distance calculation (separated by spaces): ")
vec2 = list(map(float, vec2_input.split()))

# Calculate Euclidean distance
distance = euclidean_distance(vec1, vec2)
print(f"Euclidean distance between the vectors: {distance}")
