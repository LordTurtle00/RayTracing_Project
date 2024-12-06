from Vec3D import Vec3D
from Ray import Ray 
def RayTrace(shapes, ray, light, allowedIterations):
    """Performs ray tracing logic and returns a colour based on intersected shapes
    
    shapes should be a list containing Sphere and/or Plane objects that should be used when tracing
    ray is a Ray object containing the ray that should be cast
    light is a PointLight object that should be used when calculating primary shading
    allowedIterations is an integer that determines how many times a ray should reflect
    If allowedIterations starts at 1 then no reflections should be calculated, 2 is one reflection, and so on

    Should return a Vec3D object with the calculated colour of the intersected position
    """
    closestShape = None
    closestDistance = float("inf")
    closestNormal = None
    for shape in shapes: # Loops through the list of shapes and checks which is closest to the camera
        hit, distance, normal = shape.Trace(ray)

        if hit and distance < closestDistance:
            closestDistance = distance
            closestNormal = normal
            closestShape = shape
            
    if closestShape == None:
        return Vec3D(0, 0, 0)
    
    intersectPoint = ray.origin + ray.direction * closestDistance
    lightVec = light.centerPoint - intersectPoint
    lightDistence = lightVec.Length()
    lightVec.Normalize()

    viewVec = Vec3D(-ray.direction.x, -ray.direction.y, -ray.direction.z)
    viewVec.Normalize()

    shadowRay = Ray(intersectPoint + closestNormal, lightVec)
    isShadow = False

    for shape in shapes: # Loops through the shapes and checks if they cast a shadow
        shadowHit, shadowDistance, _ = shape.Trace(shadowRay)

        if shadowHit and shadowDistance < lightDistence:
            isShadow = True
            break
    
    if isShadow: # If there is a shadow it returns a selected colour
        return Vec3D(0, 0, 0)
    
    else: # Returns the shape's colour if there isn't a shadow
        colour = PhongShading(intersectPoint, viewVec, closestNormal, closestShape, light)

    
    return colour

def PhongShading(hitPoint, viewVec, normal, shape, light):
    lightVec2 = light.centerPoint - hitPoint 
    lightVec2.Normalize()

    diffuse = Vec3D(0.0, 0.0, 0.0)
    specular = Vec3D(0.0, 0.0, 0.0)

    dotNormalLight = normal.Dot(lightVec2)
    if dotNormalLight > 0.0:
        diffuse = shape.Colour().ComponentMul(light.Colour()) * dotNormalLight * (1.0 - shape.Reflectivity())

        reflection = normal * (2 * normal.Dot(lightVec2))-lightVec2
        specular = light.Colour() * shape.Reflectivity() * max(reflection.Dot( viewVec), 0.0)

    return diffuse + specular