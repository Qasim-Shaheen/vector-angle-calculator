import numpy as np

def calculate_angle(a,b):
    denominator = np.linalg.norm(a) * np.linalg.norm(b)
    product = np.dot(a,b)
    cos_alpha = product / denominator
    angle = np.arccos(cos_alpha) # Gibt den Winkel in radiant an
    angle_degree = np.degrees(angle) # Wandelt den winkel von rad zu degree 
    return angle_degree

vector_a1 = float(input("Enter x-component for Vector A: "))
vector_a2 = float(input("Enter y-component for Vector A: "))
vector_a3 = float(input("Enter z-component for Vector A: "))
vector_a = np.array([vector_a1,vector_a2,vector_a3])
print("")

vector_b1 = float(input("Enter x-component for Vector B: "))
vector_b2 = float(input("Enter y-component for Vector B: "))
vector_b3 = float(input("Enter z-component for Vector B: "))
vector_b = np.array([vector_b1,vector_b2,vector_b3])
    
print("\n The angle between the vectors is :", calculate_angle(vector_a,vector_b),"degree")
