import cv2
import matplotlib.pyplot as plt
그림BGR = cv2.imread("그림파일.jpg")
그림RGB = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2RGB)
새가로, 새세로 = 900, 300 # 좋아하는 숫자를 넣으세요
그림새크기 = cv2.resize(그림RGB, (새가로, 새세로))
plt.imshow(그림새크기, interpolation='bicubic')
plt.show()

