import cv2
import matplotlib.pyplot as plt

그림BGR = cv2.imread("그림파일.jpg")
그림RGB = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2RGB)
그림좌우반전 = cv2.flip(그림RGB, 1) // 1은 좌우 반전, 0은 상하 반전입니다.
plt.imshow(그림좌우반전, interpolation='bicubic')
plt.show()

