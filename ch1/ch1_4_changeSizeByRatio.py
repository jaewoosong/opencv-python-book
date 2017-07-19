import cv2
import matplotlib.pyplot as plt
그림BGR = cv2.imread("그림파일.jpg")
그림RGB = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2RGB)
새가로비율, 새세로비율 = 0.3, 1.7 # 좋아하는 숫자를 넣으세요
그림새크기 = cv2.resize(그림RGB, (0, 0), fx=새가로비율, fy=새세로비율)

# 이 아래 부분은 그림을 화면에 출력하기 위한 부분으로, OpenCV 알고리즘과는 상관이 없습니다.
plt.subplot(1, 2, 1) # 1행 2열에서 1번째 열
plt.imshow(그림RGB)

plt.subplot(1, 2, 2) # 1행 2열에서 2번째 열
plt.imshow(그림새크기)

plt.show()

