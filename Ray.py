from Vec3D import Vec3D

class Ray:
    origin = Vec3D(0.0, 0.0, 0.0)
    direction = Vec3D(0.0, 0.0, 0.0)

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
        self.direction.Normalize()

    def Origin(self):
        return self.origin

    def Direction(self):
        return self.direction