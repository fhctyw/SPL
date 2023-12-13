import numpy as np

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)
    
    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def normalize(self):
        len = self.length()
        if len > 0:
            return self * (1.0 / len)
        return Vector3D(self.x, self.y, self.z)


class Matrix44:
    def __init__(self, matrix=None):
        self.matrix = matrix if matrix is not None else np.identity(4)
    
    @staticmethod
    def identity():
        return Matrix44()

    @staticmethod
    def from_translation(x, y, z):
        mat = np.identity(4)
        mat[3, 0] = x
        mat[3, 1] = y
        mat[3, 2] = z
        return Matrix44(mat)
    
    @staticmethod
    def from_x_rotation(theta):
        c, s = np.cos(theta), np.sin(theta)
        return Matrix44(np.array([
            [1, 0,  0, 0],
            [0, c, -s, 0],
            [0, s,  c, 0],
            [0, 0,  0, 1]
        ]))

    # Implement from_y_rotation and from_z_rotation similarly

    def __mul__(self, other):
        if isinstance(other, Matrix44):
            return Matrix44(np.dot(self.matrix, other.matrix))
        elif isinstance(other, Vector3D):
            x, y, z, _ = np.dot(self.matrix, [other.x, other.y, other.z, 1])
            return Vector3D(x, y, z)
        else:
            raise ValueError("Unsupported multiplication")

    def transpose(self):
        return Matrix44(self.matrix.T)
