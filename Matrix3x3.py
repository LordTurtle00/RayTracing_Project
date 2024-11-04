from Vec3D import Vec3D
from math import cos, sin

class Matrix3x3:
    columns = [Vec3D(1.0, 0.0, 0.0), Vec3D(0.0, 1.0, 0.0), Vec3D(0.0, 0.0, 1.0)]


    def __init__(self, column1, column2, column3):
        self.columns[0] = column1
        self.columns[1] = column2
        self.columns[2] = column3

    def TransformVector(self, vector):
        x = vector.Dot(self.columns[0])
        y = vector.Dot(self.columns[1])
        z = vector.Dot(self.columns[2])
        
        return Vec3D(x, y, z)

def RotationMatrix(angle, axis):
    cosTheta = cos(angle)
    sinTheta = sin(angle)
    oneMinCos = 1 - cosTheta
    oneMinSin = 1 - sinTheta
    x = axis.X()
    y = axis.Y()
    z = axis.Z()

    column1_x = cosTheta + (x**2)*oneMinCos
    column1_y = x*y*oneMinCos - z*sinTheta  
    column1_z = x*z*oneMinCos + y*sinTheta 
    column1 = Vec3D(column1_x, column1_y, column1_z)

    column2_x = x*y*oneMinCos + z*sinTheta
    column2_y = cosTheta + (y**2)*oneMinCos
    column2_z = y*z*oneMinCos - x*sinTheta
    column2 = Vec3D(column2_x, column2_y, column2_z)

    column3_x = x*z*oneMinCos - y*sinTheta
    column3_y = y*z*oneMinCos + x*sinTheta
    column3_z = cosTheta + (z**2)*oneMinCos
    column3 = Vec3D(column3_x, column3_y, column3_z)

    return Matrix3x3(column1, column2, column3)
