from Vec3D import Vec3D
import math
class Sphere:

    def __init__(self, centerPoint, radius, colour, reflectivity):
        """Initializes a Sphere object
    
        centerPoint is a Vec3D object representing the center point of the sphere
        radius is a float representing the radius of the sphere
        colour is a Vec3D object representing the colour of the plane
        reflectivity is a float that determines the ratio of diffuse vs specular light reflected of the shape
        """
        self.centerPoint = Vec3D(centerPoint.x, centerPoint.y, centerPoint.z)
        self.radius = radius
        self.colour = Vec3D(colour.x, colour.y, colour.z) 
        self.reflectivity = reflectivity
        pass

    def Trace(self, ray):
        """Traces the ray against the sphere to test for intersection
        
        ray is a Ray object that represents the ray to trace against the sphere

        Should return three different values
        The first is a bool value for if the sphere was intersected (True) or not (False)
        The second is a float value representing the distance from the ray origin that the intersection occurs at (t in o + t*d)
        The third is a Vec3D object representing the normal at the intersected position
        """
        originToCenter = self.centerPoint - ray.origin # Calculates the direction of L
        closestApproach = originToCenter.Dot(ray.direction) # Calculates the dot produkt S
        originToCenterDot = originToCenter.Dot(originToCenter) # L squered
        closestApproachSquared = closestApproach**2 # S squered
        sphereDiamemter = self.radius**2

        if closestApproach < 0 and originToCenterDot > sphereDiamemter: # Checks if the sphere is behinde the origin point
            return False, 0, Vec3D(0,0,0)
        
        m = originToCenterDot - closestApproachSquared
        if m > sphereDiamemter: # Checks if the ray is outside the sphere
            return False, 0, Vec3D(0,0,0)
        
        q = math.sqrt(sphereDiamemter-m)
        if originToCenterDot > sphereDiamemter:
            distance = closestApproach - q
        else:
            distance = closestApproach + q
        
        intersection = ray.origin + ray.direction * distance
        normal = intersection - self.centerPoint
        normal.Normalize() #Normalizes the normal value

        return True, distance, normal

    def CenterPoint(self):
        """Getter function for the center point of the sphere"""

        return self.centerPoint

    def Radius(self):
        """Getter function for the radius of the sphere"""

        return self.radius

    def Colour(self):
        """Getter function for the colour of the sphere"""

        return self.colour

    def Reflectivity(self):
        """Getter function for the reflectivity of the sphere"""

        return self.reflectivity
