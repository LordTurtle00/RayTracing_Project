from Vec3D import Vec3D

class PointLight:
    centerPoint = Vec3D(0.0, 0.0, 0.0)
    colour = Vec3D(0, 0, 0)

    def __init__(self, centerPoint, colour):
        self.centerPoint = centerPoint
        self.colour = colour

    def CenterPoint(self):
        return self.centerPoint

    def Colour(self):
        return self.colour