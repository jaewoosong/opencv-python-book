import cv2
import matplotlib.pyplot as plt
그림BGR = cv2.imread("그림파일.jpg")
그림흑백 = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2GRAY)
plt.imshow(그림흑백, cmap='gray', interpolation='bicubic')
plt.show()

