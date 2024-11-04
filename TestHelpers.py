from Vec3D import Vec3D

def ApproximatelyEquals(calculatedValue, expectedValue):
    delta = 0.001
    upper = calculatedValue >= expectedValue - delta
    lower = calculatedValue <= expectedValue + delta
    assert upper and lower

def Vec3DToString(vector):
    toReturn = "{ "
    toReturn += str(vector.X()) + ", "
    toReturn += str(vector.Y()) + ", "
    toReturn += str(vector.Z()) + " }"

    return toReturn