import cv2 as cv
import matplotlib.pyplot as plt

print("Please enter photo name with .jpg")
photo_name=input()
photo = cv.imread(photo_name)

photo = cv.cvtColor(photo, cv.COLOR_RGB2GRAY)

img = cv.adaptiveThreshold(photo, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 2)

plt.figure(figsize=(6,4))
plt.imshow(img, cmap='gray')

plt.show()
