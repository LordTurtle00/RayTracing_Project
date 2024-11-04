from Vec3D import Vec3D
from Ray import Ray
from Matrix3x3 import *

class PerspectiveCamera:
    forward = Vec3D(0.0, 0.0, 0.0)
    up = Vec3D(0.0, 0.0, 0.0)
    right = Vec3D(0.0, 0.0, 0.0)
    eyePos = Vec3D(0.0, 0.0, 0.0)

    widthStep = 0.0
    heightStep = 0.0
    topLeft = Vec3D(0.0, 0.0, 0.0)

    def __init__(self, width, height, horizontalFOV, forward, up, eyePos):
        self.forward = forward
        self.forward.Normalize()
        self.up = up
        self.up.Normalize()
        self.right = up.Cross(forward)
        self.right.Normalize()
        self.eyePos = eyePos

        aspectRatio = width / height
        leftMost = RotationMatrix(-horizontalFOV / 2.0, up).TransformVector(forward)
        rightMost = RotationMatrix(horizontalFOV / 2.0, up).TransformVector(forward)
        self.widthStep = (leftMost - rightMost).Length() / width
        self.heightStep = self.widthStep / aspectRatio
        self.topLeft = leftMost + up * self.heightStep * (height / 2)

    def GenerateRaysForTexel(self, texelCoordX, texelCoordY, nrOfRaysPerDimension):
        toReturn = []

        internalWidthStep = self.widthStep / (1 + nrOfRaysPerDimension)
        internalHeightStep = self.heightStep / (1 + nrOfRaysPerDimension)
        localTopLeft = self.topLeft + self.right * self.widthStep * texelCoordX
        localTopLeft = localTopLeft - self.up * self.heightStep * texelCoordY

        for h in range(1, nrOfRaysPerDimension + 1):
            for w in range(1, nrOfRaysPerDimension + 1):
                rayDirection = localTopLeft + self.right * internalWidthStep * w
                rayDirection = rayDirection - self.up * internalHeightStep * h
                rayDirection.Normalize()
                toReturn.append(Ray(self.eyePos, rayDirection))

        return toReturn
