import cv2
import numpy as np
import matplotlib.pyplot as plt

그림 = cv2.imread('체스판.png') # 결과를 보기 쉽도록 체스판 그림을 사용했습니다.
그림RGB = cv2.cvtColor(그림, cv2.COLOR_BGR2RGB)
그림흑백 = cv2.cvtColor(그림, cv2.COLOR_BGR2GRAY) # 꼭짓점 추출에는 흑백 그림이 필요합니다.
그림꼭짓점 = cv2.cvtColor(그림, cv2.COLOR_BGR2RGB) # 나중에 꼭짓점을 여기에 표시합니다.

그림흑백 = np.float32(그림흑백) # 넘파이(numpy)를 사용해서 자료형을 부동소수점으로 바꾸어주어야 합니다.
결과 = cv2.cornerHarris(그림흑백, 2, 3, 0.04) # 2, 3, 0.04는 바꿀 수 있는 인자들입니다.
결과 = cv2.dilate(결과, None, iterations=6) # 꼭짓점을 표시하기 위해 확장 (dilate) 연산을 합니다.
그림꼭짓점[결과>0.01*결과.max()]=[255, 0, 0] # 꼭짓점이 빨간색 점으로 그림에 표시됩니다.

# 이 아래 부분은 그림을 화면에 출력하기 위한 부분으로, OpenCV 알고리즘과는 상관이 없습니다.
plt.subplot(1, 2, 1) # 1행 2열에서 1번째 열
plt.imshow(그림RGB)
plt.xticks([]) # x축 좌표 숨김
plt.yticks([]) # y축 좌표 숨김

plt.subplot(1, 2, 2) # 1행 2열에서 2번째 열
plt.imshow(그림꼭짓점)
plt.xticks([]) # x축 좌표 숨김
plt.yticks([]) # y축 좌표 숨김

plt.show()

