import io

def WritePPM(width, height, data, filepath):
    fileWriter = open(filepath, "wb")
    fileWriter.write(b'P6\n')
    fileWriter.write(b'%i %i\n%i\n' % (width, height, 255))
    fileWriter.write(data)