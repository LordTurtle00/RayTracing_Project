from math import sqrt
from Vec3D import Vec3D
from Ray import Ray
from Plane import Plane
from TestHelpers import *

data = []
data.append((Plane(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, -10.0), Vec3D(0.0, 0.0, 1.0)), True, 10.0))
data.append((Plane(Vec3D(0.0, 0.0, 10.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, -10.0), Vec3D(0.0, 0.0, 1.0)), True, 20.0))
data.append((Plane(Vec3D(10.0, 0.0, 0.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, -10.0), Vec3D(0.0, 0.0, 1.0)), True, 10.0))
data.append((Plane(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, -10.0), Vec3D(0.0, 0.0, -1.0)), False, 0.0))
data.append((Plane(Vec3D(-10.0, 0.0, 0.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, -10.0), Vec3D(0.0, 0.0, -1.0)), False, 0.0))
data.append((Plane(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, -10.0), Vec3D(1.0, 0.0, 0.0)), False, 0.0))
data.append((Plane(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, -10.0), Vec3D(-1.0, 0.0, 0.0)), False, 0.0))
data.append((Plane(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, -10.0), Vec3D(0.0, 1.0, 0.0)), False, 0.0))
data.append((Plane(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, -10.0), Vec3D(0.0, -1.0, 0.0)), False, 0.0))
data.append((Plane(Vec3D(10.0, 0.0, 0.0), Vec3D(-1.0, 0.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(1.0, 0.0, 0.0)), True, 10.0))
data.append((Plane(Vec3D(15.0, -5.0, 0.0), Vec3D(-1.0, 0.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(1.0, 0.0, 0.0)), True, 15.0))
data.append((Plane(Vec3D(15.0, 0.0, 12.34), Vec3D(-1.0, 0.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(1.0, 0.0, 0.0)), True, 15.0))
data.append((Plane(Vec3D(10.0, 0.0, 0.0), Vec3D(-1.0, 0.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(5.0, 0.0, 0.0), Vec3D(1.0, 0.0, 0.0)), True, 5.0))
data.append((Plane(Vec3D(10.0, 0.0, 0.0), Vec3D(-1.0, 0.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(-1.0, 0.0, 0.0)), False, 0.0))
data.append((Plane(Vec3D(10.0, 0.0, 0.0), Vec3D(-1.0, 0.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 1.0, 0.0)), False, 0.0))
data.append((Plane(Vec3D(10.0, 0.0, 0.0), Vec3D(-1.0, 0.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, -1.0, 0.0)), False, 0.0))
data.append((Plane(Vec3D(10.0, 0.0, 0.0), Vec3D(-1.0, 0.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.0, 1.0)), False, 0.0))
data.append((Plane(Vec3D(10.0, 0.0, 0.0), Vec3D(-1.0, 0.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.0, -1.0)), False, 0.0))
data.append((Plane(Vec3D(0.0, 10.0, 0.0), Vec3D(0.0, -1.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 1.0, 0.0)), True, 10.0))
data.append((Plane(Vec3D(-5.0, 15.0, 0.0), Vec3D(0.0, -1.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 1.0, 0.0)), True, 15.0))
data.append((Plane(Vec3D(0.0, 15.0, 12.34), Vec3D(0.0, -1.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 1.0, 0.0)), True, 15.0))
data.append((Plane(Vec3D(0.0, 10.0, 0.0), Vec3D(0.0, -1.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 5.0, 0.0), Vec3D(0.0, 1.0, 0.0)), True, 5.0))
data.append((Plane(Vec3D(0.0, 10.0, 0.0), Vec3D(0.0, -1.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, -1.0, 0.0)), False, 0.0))
data.append((Plane(Vec3D(0.0, 10.0, 0.0), Vec3D(0.0, -1.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(1.0, 0.0, 0.0)), False, 0.0))
data.append((Plane(Vec3D(0.0, 10.0, 0.0), Vec3D(0.0, -1.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(-1.0, 0.0, 0.0)), False, 0.0))
data.append((Plane(Vec3D(0.0, 10.0, 0.0), Vec3D(0.0, -1.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.0, 1.0)), False, 0.0))
data.append((Plane(Vec3D(0.0, 10.0, 0.0), Vec3D(0.0, -1.0, 0.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.0, -1.0)), False, 0.0))
data.append((Plane(Vec3D(0.0, 0.0, 1.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.707106, 0.707106)), True, sqrt(2)))
data.append((Plane(Vec3D(0.0, 0.0, 1.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, -0.707106, 0.707106)), True, sqrt(2)))
data.append((Plane(Vec3D(0.0, 0.0, 1.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.707106, 0.0, 0.707106)), True, sqrt(2)))
data.append((Plane(Vec3D(0.0, 0.0, 1.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(-0.707106, 0.0, 0.707106)), True, sqrt(2)))
data.append((Plane(Vec3D(0.0, 0.0, 1.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, 0.707106, -0.707106)), False, 0))
data.append((Plane(Vec3D(0.0, 0.0, 1.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.0, -0.707106, -0.707106)), False, 0))
data.append((Plane(Vec3D(0.0, 0.0, 1.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(0.707106, 0.0, -0.707106)), False, 0))
data.append((Plane(Vec3D(0.0, 0.0, 1.0), Vec3D(0.0, 0.0, -1.0), Vec3D(0.0, 0.0, 0.0), 0.0), Ray(Vec3D(0.0, 0.0, 0.0), Vec3D(-0.707106, 0.0, -0.707106)), False, 0))

for collection in data:
    plane = collection[0]
    ray = collection[1]
    expectedHit = collection[2]
    expectedDistance = collection[3]
    expectedNormal = plane.Normal()

    print("Testing plane with point:", Vec3DToString(plane.Point()))
    print("and normal:", plane.Normal())
    print("Against ray with origin:", Vec3DToString(ray.Origin()))
    print("and direction:", Vec3DToString(ray.Direction()))
    expectedReturn = (expectedHit, expectedDistance, Vec3DToString(expectedNormal))
    print("Expected return values:", expectedReturn)

    hit, distance, normal = plane.Trace(ray)
    assert hit == expectedHit
    
    if hit == True:
        ApproximatelyEquals(distance, expectedDistance)
        ApproximatelyEquals(normal.X(), expectedNormal.X())
        ApproximatelyEquals(normal.Y(), expectedNormal.Y())
        ApproximatelyEquals(normal.Z(), expectedNormal.Z())

    print("")
print("All plane tests succeeded")