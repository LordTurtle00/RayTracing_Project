class Vec3D:

    def __init__(self, x, y, z):
        """Initializes a Vec3D object
        
        x is the x component of the vector
        y is the y component of the vector
        z is the z component of the vector
        """

        pass

    def __add__(self, other):
        """Performs vector addition
        
        other is a Vec3D object in the equation self + other
        
        Does not change self or other, instead returning a new Vec3D object
        """

        return None

    def __sub__(self, other):
        """Performs vector subtraction
        
        other is a Vec3D object in the equation self - other
        
        Does not change self or other, instead returning a new Vec3D object
        """
        
        return None

    def __mul__(self, other):
        """Performs scalar multiplication
        
        other is a float in the equation self * other
        
        Does not change self or other, instead returning a new Vec3D object
        """
        
        return None

    def Dot(self, other):
        """Calculates the dot product of self and other
        
        other is a Vec3D object

        returns a single float value with the calculated result
        """
        
        return None

    def Cross(self, other):
        """Calculates the cross product of self and other
        
        other is a Vec3D object

        returns a Vec3D object with the calculated result
        """

        return None

    def ComponentMul(self, other):
        """Performs componentwise multiplication between two vectors
        
        other is a Vec3D object

        Does not change self or other, instead returning a new Vec3D object
        """

        return None

    def Length(self):
        """Returns the length of the vector"""

        return None

    def Normalize(self):
        """Normalizes self, does not return a vector"""
        


    def X(self):
        """Getter function for the x component of the vector"""

        return None

    def Y(self):
        """Getter function for the y component of the vector"""

        return None

    def Z(self):
        """Getter function for the z component of the vector"""

        return None
