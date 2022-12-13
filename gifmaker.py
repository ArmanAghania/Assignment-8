import os

import imageio

file_list = sorted(os.listdir('C:/Users/Arman/OneDrive/Desktop/DL/Assignment-8/Images'))
print(file_list)
IMAGES = []

for file_name in file_list:
    file_path = 'C:/Users/Arman/OneDrive/Desktop/DL/Assignment-8/Images/' + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave('C:/Users/Arman/OneDrive/Desktop/DL/Assignment-8/output.gif', IMAGES)