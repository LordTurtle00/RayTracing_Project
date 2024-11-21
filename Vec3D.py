from math import sqrt

class Vec3D:

    def __init__(self, x, y, z):
        """Initializes a Vec3D object
        
        x is the x component of the vector
        y is the y component of the vector
        z is the z component of the vector
        """
        self.x = x
        self.y = y
        self.z = z


        pass

    def __add__(self, other):
        """Performs vector addition
        
        other is a Vec3D object in the equation self + other
        
        Does not change self or other, instead returning a new Vec3D object
        """

        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Performs vector subtraction
        
        other is a Vec3D object in the equation self - other
        
        Does not change self or other, instead returning a new Vec3D object
        """
        
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """Performs scalar multiplication
        
        other is a float in the equation self * other
        
        Does not change self or other, instead returning a new Vec3D object
        """

        return Vec3D(self.x * other, self.y * other, self.z * other)

    def Dot(self, other):
        """Calculates the dot product of self and other
        
        other is a Vec3D object

        returns a single float value with the calculated result
        """
        
        return self.x * other.x + self.y * other.y + self.z * other.z

    def Cross(self, other):
        """Calculates the cross product of self and other
        
        other is a Vec3D object

        returns a Vec3D object with the calculated result
        """

        return Vec3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def ComponentMul(self, other):
        """Performs componentwise multiplication between two vectors
        
        other is a Vec3D object

        Does not change self or other, instead returning a new Vec3D object
        """

        return Vec3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def Length(self):
        """Returns the length of the vector"""

        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def Normalize(self):
        """Normalizes self, does not return a vector"""
        length = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        self.x = self.x / length
        self.y = self.y / length
        self.z = self.z / length
        return self

    def X(self):
        """Getter function for the x component of the vector"""

        return self.x

    def Y(self):
        """Getter function for the y component of the vector"""

        return self.y

    def Z(self):
        """Getter function for the z component of the vector"""

        return self.z
