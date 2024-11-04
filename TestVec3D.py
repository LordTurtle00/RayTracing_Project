from math import sqrt
from Vec3D import Vec3D
from TestHelpers import *

oneDivSqrt3 = 1.0 / sqrt(3)
vectors = []
vectors.append(Vec3D(1.0, 0.0, 0.0))
vectors.append(Vec3D(0.0, 1.0, 0.0))
vectors.append(Vec3D(oneDivSqrt3, oneDivSqrt3, oneDivSqrt3))
vectors.append(Vec3D(1.5, 0.0, 2.0))

expectedMemberValues = []
expectedMemberValues.append([1.0, 0.0, 0.0])
expectedMemberValues.append([0.0, 1.0, 0.0])
expectedMemberValues.append([oneDivSqrt3, oneDivSqrt3, oneDivSqrt3])
expectedMemberValues.append([1.5, 0.0, 2.0])

expectedLengths = [1.0, 1.0, 1.0, sqrt(6.25)]

dotVector1 = Vec3D(1.0, 0.0, 0.0)
dotVector2 = Vec3D(0.0, 1.0, 1.0)
expectedDotProducts1 = [1.0, 0.0, oneDivSqrt3, 1.5]
expectedDotProducts2 = [0.0, 1.0, 2 * oneDivSqrt3, 2.0]

crossVector1 = Vec3D(0.0, 0.0, 1.0)
crossVector2 = Vec3D(1.0, 2.0, 3.0)
expectedCrossResults1 = []
expectedCrossResults1.append([0.0, -1.0, 0.0])
expectedCrossResults1.append([1.0, 0.0, 0.0])
expectedCrossResults1.append([oneDivSqrt3, -oneDivSqrt3, 0.0])
expectedCrossResults1.append([0.0, -1.5, 0.0])
expectedCrossResults2 = []
expectedCrossResults2.append([0.0, -3.0, 2.0])
expectedCrossResults2.append([3.0, 0.0, -1.0])
expectedCrossResults2.append([oneDivSqrt3, -2 * oneDivSqrt3, oneDivSqrt3])
expectedCrossResults2.append([-4.0, -2.5, 3.0])

scalar = 2.25
expectedScalarResults = []
expectedScalarResults.append([2.25, 0.0, 0.0])
expectedScalarResults.append([0.0, 2.25, 0.0])
expectedScalarResults.append([2.25 * oneDivSqrt3, 2.25 * oneDivSqrt3, 2.25 * oneDivSqrt3])
expectedScalarResults.append([3.375, 0.0, 4.5])

for index in range(0, len(vectors)):
    print("Starting tests with vector:", expectedMemberValues[index])
    vector = vectors[index]

    print("Checking so that expected member values are returned by X, Y, Z functions")
    ApproximatelyEquals(vector.X(), expectedMemberValues[index][0])
    ApproximatelyEquals(vector.Y(), expectedMemberValues[index][1])
    ApproximatelyEquals(vector.Z(), expectedMemberValues[index][2])

    print("Checking so that the Length function returns the expected value of:", 
        expectedLengths[index])
    ApproximatelyEquals(vector.Length(), expectedLengths[index])

    print("Checking so that the Normalize function returns the expected vector")
    normalized = Vec3D(vector.X(), vector.Y(), vector.Z())
    normalized.Normalize()
    ApproximatelyEquals(normalized.X(), vector.X() / expectedLengths[index])
    ApproximatelyEquals(normalized.Y(), vector.Y() / expectedLengths[index])
    ApproximatelyEquals(normalized.Z(), vector.Z() / expectedLengths[index])

    print("Checking so that the Dot function returns the expected value of:", 
        expectedDotProducts1[index], "when multiplied with { 1.0, 0.0, 0.0 }")
    ApproximatelyEquals(vector.Dot(dotVector1), expectedDotProducts1[index])
    print("Checking so that the Dot function returns the expected value of:", 
        expectedDotProducts2[index], "when multiplied with { 0.0, 1.0, 1.0 }")
    ApproximatelyEquals(vector.Dot(dotVector2), expectedDotProducts2[index])

    print("Checking so that the Cross function returns the expected value of:", 
        expectedCrossResults1[index], "when multiplied with { 0.0, 0.0, 1.0 }")
    crossResult1 = vector.Cross(crossVector1)
    ApproximatelyEquals(crossResult1.X(), expectedCrossResults1[index][0])
    ApproximatelyEquals(crossResult1.Y(), expectedCrossResults1[index][1])
    ApproximatelyEquals(crossResult1.Z(), expectedCrossResults1[index][2])
    print("Checking so that the Cross function returns the expected value of:", 
        expectedCrossResults2[index], "when multiplied with { 1.0, 2.0, 3.0 }")
    crossResult2 = vector.Cross(crossVector2)
    ApproximatelyEquals(crossResult2.X(), expectedCrossResults2[index][0])
    ApproximatelyEquals(crossResult2.Y(), expectedCrossResults2[index][1])
    ApproximatelyEquals(crossResult2.Z(), expectedCrossResults2[index][2])

    for otherVector in vectors:
        print("Checking so that adding the vector with {", otherVector.X(), ",",
            otherVector.Y(), ",", otherVector.Z(), "} returns correctly")
        addedVector = vector + otherVector
        ApproximatelyEquals(addedVector.X(), vector.X() + otherVector.X())
        ApproximatelyEquals(addedVector.Y(), vector.Y() + otherVector.Y())
        ApproximatelyEquals(addedVector.Z(), vector.Z() + otherVector.Z())

        print("Checking so that subtracting {", otherVector.X(), ",", otherVector.Y(),
            ",", otherVector.Z(), "} from the vector returns correctly")
        subtractedVector = vector - otherVector
        ApproximatelyEquals(subtractedVector.X(), vector.X() - otherVector.X())
        ApproximatelyEquals(subtractedVector.Y(), vector.Y() - otherVector.Y())
        ApproximatelyEquals(subtractedVector.Z(), vector.Z() - otherVector.Z())

        print("Checking so that the ComponentMul function with input {", otherVector.X(), 
        ",", otherVector.Y(), ",", otherVector.Z(), "} returns correctly")
        componentmulVector = vector.ComponentMul(otherVector)
        ApproximatelyEquals(componentmulVector.X(), vector.X() * otherVector.X())
        ApproximatelyEquals(componentmulVector.Y(), vector.Y() * otherVector.Y())
        ApproximatelyEquals(componentmulVector.Z(), vector.Z() * otherVector.Z())

    print("Checking so that scalar multiplication returns the expected value of:", 
        expectedScalarResults[index], "when multiplied with:", scalar)
    scalarResult = vector * scalar
    ApproximatelyEquals(scalarResult.X(), expectedScalarResults[index][0])
    ApproximatelyEquals(scalarResult.Y(), expectedScalarResults[index][1])
    ApproximatelyEquals(scalarResult.Z(), expectedScalarResults[index][2])

    print("")
print("All Vec3D tests succeeded")