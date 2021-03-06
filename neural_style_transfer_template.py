# -*- coding: utf-8 -*-
"""Neural Style Transfer-Template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/nicknochnack/Python-Neural-Style-Transfer/blob/main/Neural%20Style%20Transfer-Template.ipynb

# 0. Import Dependencies and Pretrained Model
"""

import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

"""# 1. Preprocess Image and Load"""

def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

content_image = load_image('test.jpeg')
style_image = load_image('style.jpeg')

"""# 2. Visualize Output"""

content_image.shape

plt.imshow(np.squeeze(style_image))
plt.show()

"""# 3. Stylize Image"""

stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]

plt.imshow(np.squeeze(stylized_image))
plt.show()

cv2.imwrite('generated_img.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))

