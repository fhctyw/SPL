import numpy as np
from .math import *

class Camera:
    def __init__(self, position=None, look_at=None, up=None, fov=np.pi/4, aspect_ratio=1.0, near_plane=0.1, far_plane=1000.0):
        self.position = position if position is not None else Vector3D(0, 0, 0)
        self.up = up if up is not None else Vector3D(0, 1, 0)
        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.near_plane = near_plane
        self.far_plane = far_plane
        self.look_at_target = look_at if look_at is not None else Vector3D(0, 0, -1)

        self.view_matrix = Matrix44.identity()
        self.projection_matrix = self.calculate_projection_matrix()
        
        if look_at is not None:
            self.look_at(look_at)

    def calculate_projection_matrix(self):
        # Perspective projection matrix
        f = 1.0 / np.tan(self.fov / 2)
        z_range = self.far_plane - self.near_plane
        a = f / self.aspect_ratio
        b = f
        c = (self.far_plane + self.near_plane) / z_range
        d = (-2 * self.far_plane * self.near_plane) / z_range
        return Matrix44(np.array([
            [a, 0, 0,  0],
            [0, b, 0,  0],
            [0, 0, c,  1],
            [0, 0, d,  0]
        ]))

    def look_at(self, target):
        # Adjust the look_at_target if needed
        self.look_at_target = target
        zaxis = (self.position - target).normalize()    # The "forward" vector.
        xaxis = self.up.cross(zaxis).normalize()        # The "right" vector.
        yaxis = zaxis.cross(xaxis)                      # The "up" vector.

        self.view_matrix = Matrix44(np.array([
            [xaxis.x, yaxis.x, zaxis.x, 0],
            [xaxis.y, yaxis.y, zaxis.y, 0],
            [xaxis.z, yaxis.z, zaxis.z, 0],
            [-xaxis.dot(self.position), -yaxis.dot(self.position), -zaxis.dot(self.position), 1]
        ]))

    def move(self, direction, amount):
        # Move the camera in a direction by a certain amount
        translation_vector = direction.normalize() * amount
        self.position += translation_vector
        self.look_at(self.look_at_target)
