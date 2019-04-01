import re
import os
str = "dog runs to cat"
pattern1 = "cat"
pattern2 = "bird"

ptn = r"r[au]n"


print(re.search(pattern1,str))
print(re.search(ptn,str))


print((os.path.isdir("D://test") ==False))


import random

print(random.randint(1000))