class Renderer:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.depth_buffer = [[float('inf') for _ in range(screen_width)] for _ in range(screen_height)]
        self.char_buffer = [[' ' for _ in range(screen_width)] for _ in range(screen_height)]

    def project_vertex(self, vertex, projection_matrix):
        # Transform the vertex by the projection matrix
        projected_vertex = projection_matrix * vertex
        # Normalize the vertex
        if projected_vertex.z != 0:
            projected_vertex.x /= projected_vertex.z
            projected_vertex.y /= projected_vertex.z
        # Map to screen space
        screen_x = int((projected_vertex.x + 1) * (self.screen_width / 2))
        screen_y = int((1 - projected_vertex.y) * (self.screen_height / 2))
        return screen_x, screen_y

    def render(self, scene):
        for mesh in scene.meshes:
            transformed_vertices = [scene.camera.projection_matrix * scene.camera.view_matrix * vertex for vertex in mesh.vertices]
            for face in mesh.faces:
                vertices = [transformed_vertices[index] for index in face]
                self.draw_triangle(vertices)
        self.draw_buffer()


    def project_vertex(self, vertex, projection_matrix, view_matrix):
        # Transform the vertex by the view matrix first (View Transformation)
        view_transformed = view_matrix * vertex
        
        # Then by the projection matrix (Projection Transformation)
        projected_vertex = projection_matrix * view_transformed

        # Homogeneous division to normalize the vertex coordinates (Perspective divide)
        if projected_vertex.w != 0:
            projected_vertex.x /= projected_vertex.w
            projected_vertex.y /= projected_vertex.w
            projected_vertex.z /= projected_vertex.w

        # Screen Mapping (Viewport Transformation)
        screen_x = int((projected_vertex.x + 1) * (self.screen_width / 2))
        screen_y = int((1 - projected_vertex.y) * (self.screen_height / 2))

        # Depth value for depth buffering
        depth = projected_vertex.z

        return screen_x, screen_y, depth

    def render(self, scene):
        # Clear buffers before rendering
        self.clear_buffer()

        # Iterate over all meshes in the scene
        for mesh in scene.meshes:
            # Perform Vertex Transformation using the mesh's world matrix
            world_vertices = [mesh.world_matrix * vertex for vertex in mesh.vertices]
            
            # Perform View Transformation and Projection Transformation
            projected_vertices = [self.project_vertex(v, scene.camera.projection_matrix, scene.camera.view_matrix) for v in world_vertices]
            
            # Rasterize the projected vertices into triangles
            for face in mesh.faces:
                vertices = [projected_vertices[index] for index in face]
                self.draw_triangle(vertices)

        # After all meshes are rendered, output the buffer to the screen
        self.draw_buffer()

    def draw_line(self, start, end, char='*'):
        """Draws a line from start to end using Bresenham's line algorithm"""
        x0, y0 = start
        x1, y1 = end
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy

        while True:
            if 0 <= x0 < self.screen_width and 0 <= y0 < self.screen_height:
                self.char_buffer[y0][x0] = char  # Set the character at this position
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def draw_triangle(self, vertices, char='*'):
        """Draws a triangle given its vertices"""
        # Assume vertices is a list of Vector3D
        points = [self.project_vertex(v) for v in vertices]
        # Draw the edges of the triangle
        self.draw_line(points[0], points[1], char)
        self.draw_line(points[1], points[2], char)
        self.draw_line(points[2], points[0], char)

    def draw_buffer(self):
        """Draws the entire frame buffer to the console"""
        for y in range(self.screen_height):
            for x in range(self.screen_width):
                print(self.char_buffer[y][x], end='')
            print()  # Newline at the end of each row

    def clear_buffer(self):
        """Clears the character and depth buffers"""
        for y in range(self.screen_height):
            for x in range(self.screen_width):
                self.char_buffer[y][x] = ' '
                self.depth_buffer[y][x] = float('inf')
