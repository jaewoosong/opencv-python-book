import cv2
import matplotlib.pyplot as plt

그림BGR = cv2.imread("그림파일.jpg")
그림RGB = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2RGB)
그림좌우반전 = cv2.flip(그림RGB, 1) # 1은 좌우 반전, 0은 상하 반전입니다.

# 이 아래 부분은 그림을 화면에 출력하기 위한 부분으로, OpenCV 알고리즘과는 상관이 없습니다.
plt.subplot(1, 2, 1) # 1행 2열에서 1번째 열
plt.imshow(그림RGB)

plt.subplot(1, 2, 2) # 1행 2열에서 2번째 열
plt.imshow(그림좌우반전)

plt.show()

