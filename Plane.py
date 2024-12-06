from Vec3D import Vec3D

class Plane:

    def __init__(self, point, normal, colour, reflectivity):
        """Initializes a Plane object
    
        point is a Vec3D object representing a point on the plane
        normal is a Vec3D object representing the plane normal
        colour is a Vec3D object representing the colour of the plane
        reflectivity is a float that determines the ratio of diffuse vs specular light reflected of the shape
        """
        self.point = Vec3D(point.x, point.y, point.z)
        self.normal = Vec3D(normal.x, normal.y, normal.z)
        self.normal.Normalize()
        self.colour = Vec3D(colour.x, colour.y, colour.z)
        self.reflectivity = reflectivity
        pass

    def Trace(self, ray):
        """Traces the ray against the plane to test for intersection
        
        ray is a Ray object that represents the ray to trace against the plane

        Should return three different values
        The first is a bool value for if the plane was intersected (True) or not (False)
        The second is a float value representing the distance from the ray origin that the intersection occurs at (t in o + t*d)
        The third is a Vec3D object representing the normal at the intersected position (always the same for a plane)
        """
        hit = False
        distance = 0
        normal = self.normal

        denominator = self.normal.Dot(ray.Direction())
        #Check if the ray is parallel to the plane
        if abs(denominator)<0.0001:
            return hit, distance, normal
        
        rayIntersection = ((self.point - ray.Origin()).Dot(self.normal))/denominator
        #Check if the ray intersects the plane
        if rayIntersection >= 0:
            hit = True
            distance = rayIntersection
            return hit, distance, normal
        #Cheks if the ray is negative
        else:
            return hit, distance, normal

    def Point(self):
        """Getter function for the point the plane contains"""

        return self.point
    
    def Normal(self):
        """Getter function for the normal of the plane"""

        return self.normal

    def Colour(self):
        """Getter function for the colour of the plane"""

        return self.colour

    def Reflectivity(self):
        """Getter function for the reflectivity of the plane"""

        return self.reflectivity
