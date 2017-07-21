import cv2
import matplotlib.pyplot as plt

그림 = cv2.imread('그림파일.jpg')
그림RGB = cv2.cvtColor(그림, cv2.COLOR_BGR2RGB)
모서리추출 = cv2.Canny(그림, 100, 200) # 100, 200은 변경 가능한 인자값입니다.

# 이 아래 부분은 그림을 화면에 출력하기 위한 부분으로, OpenCV 알고리즘과는 상관이 없습니다.
plt.subplot(1, 2, 1) # 1행 2열에서 1번째 열
plt.imshow(그림RGB)
plt.xticks([]) # x축 좌표 숨김
plt.yticks([]) # y축 좌표 숨김

plt.subplot(1, 2, 2) # 1행 2열에서 2번째 열
plt.imshow(모서리추출, cmap='gray')
plt.xticks([]) # x축 좌표 숨김
plt.yticks([]) # y축 좌표 숨김

plt.show()

