from PPM import WritePPM
from RayTrace import RayTrace
from Vec3D import Vec3D
from Ray import Ray
from Plane import Plane
from Sphere import Sphere
from PointLight import PointLight
from Camera import PerspectiveCamera

rayDirection = Vec3D(0.0, 0.0, 1.0)
shapes = []
shapes.append(Plane(Vec3D(0.0, 0.0, 650.0), Vec3D(0.0, 0.0, -1.0), Vec3D(1.0, 0.35, 1.0), 0.0)) # in front
shapes.append(Plane(Vec3D(0.0, 0.0, -650.0), Vec3D(0.0, 0.0, 1.0), Vec3D(0.35, 0.35, 1.0), 0.0)) # behind
shapes.append(Plane(Vec3D(650.0, 0.0, 0.0), Vec3D(-1.0, 0.0, 0.0), Vec3D(1.0, 0.35, 0.35), 0.0)) # right
shapes.append(Plane(Vec3D(-650.0, 0.0, 0.0), Vec3D(1.0, 0.0, 0.0), Vec3D(1.0, 0.35, 0.35), 0.0)) # left
shapes.append(Plane(Vec3D(0.0, 650.0, 0.0), Vec3D(0.0, -1.0, 0.0), Vec3D(0.35, 1.0, 0.35), 0.0)) # above
shapes.append(Plane(Vec3D(0.0, -650.0, 0.0), Vec3D(0.0, 1.0, 0.0), Vec3D(0.35, 1.0, 0.35), 0.0)) # below
shapes.append(Sphere(Vec3D(0.0, 0.0, 0.0), 200, Vec3D(0.35, 1.0, 1.0), 0.8))
light = PointLight(Vec3D(0.0, 500.0, -400.0), Vec3D(1.0, 1.0, 1.0))

startRow = 0
startColumn = 0
width = 512
height = 512
channels = 3

PI = 3.14159265359
eyePos = Vec3D(0.0, 0.0, -649.0)
camera = PerspectiveCamera(width, height, PI / 2.0, Vec3D(0.0, 0.0, 1.0), Vec3D(0.0, 1.0, 0.0), eyePos)
nrOfSamplesPerPixelDimension = 2
colourDivFactor = 1.0 / (nrOfSamplesPerPixelDimension**2)
data = bytearray(width * height * channels)

for h in range(startRow, height):
    for w in range(startColumn, width):
        index = h * width * channels + w * channels

        rays = camera.GenerateRaysForTexel(w, h, nrOfSamplesPerPixelDimension)
        colour = Vec3D(0.0, 0.0, 0.0)
        for ray in rays:
            colour = colour + RayTrace(shapes, ray, light, 5)
        
        colour = Vec3D(colour.X() * colourDivFactor, colour.Y() * colourDivFactor, colour.Z() * colourDivFactor)

        data[index + 0] = int(min(colour.X(), 1.0) * 255)
        data[index + 1] = int(min(colour.Y(), 1.0) * 255)
        data[index + 2] = int(min(colour.Z(), 1.0) * 255)

WritePPM(width, height, data, "Test.ppm")