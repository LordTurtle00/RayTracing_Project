from Vec3D import Vec3D

class Plane:

    def __init__(self, point, normal, colour, reflectivity):
        """Initializes a Plane object
    
        point is a Vec3D object representing a point on the plane
        normal is a Vec3D object representing the plane normal
        colour is a Vec3D object representing the colour of the plane
        reflectivity is a float that determines the ratio of diffuse vs specular light reflected of the shape
        """

        pass

    def Trace(self, ray):
        """Traces the ray against the plane to test for intersection
        
        ray is a Ray object that represents the ray to trace against the plane

        Should return three different values
        The first is a bool value for if the plane was intersected (True) or not (False)
        The second is a float value representing the distance from the ray origin that the intersection occurs at (t in o + t*d)
        The third is a Vec3D object representing the normal at the intersected position (always the same for a plane)
        """

        return None

    def Point(self):
        """Getter function for the point the plane contains"""

        return None
    
    def Normal(self):
        """Getter function for the normal of the plane"""

        return None

    def Colour(self):
        """Getter function for the colour of the plane"""

        return None

    def Reflectivity(self):
        """Getter function for the reflectivity of the plane"""

        return None
