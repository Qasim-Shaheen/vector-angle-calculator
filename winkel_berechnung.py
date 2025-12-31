import numpy as np

def calculate_angle(a,b):
    denominator = np.linalg.norm(a) * np.linalg.norm(b)
    product = np.dot(a,b)
    cos_alpha = product / denominator
    angle = np.arccos(cos_alpha) # Gibt den Winkel in radiant an
    angle_degree = np.degrees(angle) # Wandelt den winkel von rad zu degree 
    return angle_degree

vector_a1 = float(input("Vector a (x-value): "))
vector_a2 = float(input("Vector a (y-value): "))
vector_a3 = float(input("Vector a (z-value): "))
vector_a = np.array([vector_a1,vector_a2,vector_a3])
print("")

vector_b1 = float(input("Vector b (x-value): "))
vector_b2 = float(input("Vector b (y-value): "))
vector_b3 = float(input("Vector b (z-value): "))
vector_b = np.array([vector_b1,vector_b2,vector_b3])
    
print("\n The angle between the vectors is :", calculate_angle(vector_a,vector_b),"degree")