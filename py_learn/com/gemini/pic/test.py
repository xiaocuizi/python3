
import random as random
def rndColor1():
    return (random.randint(64, 256), random.randint(64, 256), random.randint(64, 256))

def rndChar():
    return chr(random.randint(65, 90))

print(rndChar())