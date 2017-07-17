import cv2
import matplotlib.pyplot as plt
그림BGR = cv2.imread("그림파일.jpg")
그림RGB = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2RGB)
plt.imshow(그림RGB, interpolation='bicubic')
plt.show()

