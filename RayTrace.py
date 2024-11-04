def RayTrace(shapes, ray, light, allowedIterations):
    """Performs ray tracing logic and returns a colour based on intersected shapes
    
    shapes should be a list containing Sphere and/or Plane objects that should be used when tracing
    ray is a Ray object containing the ray that should be cast
    light is a PointLight object that should be used when calculating primary shading
    allowedIterations is an integer that determines how many times a ray should reflect
    If allowedIterations starts at 1 then no reflections should be calculated, 2 is one reflection, and so on

    Should return a Vec3D object with the calculated colour of the intersected position
    """
    
    return None