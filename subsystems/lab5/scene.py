from .camera import Camera

class Scene:
    def __init__(self):
        self.meshes = []  # A list to hold all the meshes that need to be rendered
        self.camera = Camera()  # The camera to view the scene from

    def add_mesh(self, mesh):
        self.meshes.append(mesh)

    def set_camera(self, camera):
        self.camera = camera
