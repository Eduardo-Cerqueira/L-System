"""
Installer les dépendances avec pip :
pip install PIL
pip install opensimplex
"""

from PIL import Image
import opensimplex as simplex

width = 256
height = 256
scale = 24.0
simplex.seed(100)

print('Generating 2D image...')
noise = Image.new('L', (width, height))
for y in range(0, height):
    for x in range(0, width):
        value = simplex.noise2(x / scale, y / scale)
        color = int((value + 1) * 129)
        noise.putpixel((x, y), color)
print('Done')
#noise.save("noise.png")
noise.show()