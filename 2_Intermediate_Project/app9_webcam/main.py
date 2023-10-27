import cv2
import numpy as np

# array = cv2.imread("2_Intermediate_Project/app9_webcam/image.png")

# # print(array.shape)
# print(type(array))

a = np.array(
    [
        [[255, 0, 0], [255, 255, 255], [255, 255, 255], [187, 41, 160]],
        [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
        [[255, 255, 255], [0, 0, 0], [47, 255, 173], [255, 255, 255]],
    ]
)


cv2.imwrite("2_Intermediate_Project/app9_webcam/image2.png", a)
