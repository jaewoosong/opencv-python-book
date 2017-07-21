import cv2
import matplotlib.pyplot as plt

그림BGR = cv2.imread("그림파일.jpg")
그림RGB = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2RGB)

# 빨간색만 뽑기
그림R = 그림RGB.copy() # 이렇게 해야 제대로 복사가 됩니다.
그림R[:,:,1] = 0 # 1: 초록색 없애기
그림R[:,:,2] = 0 # 2: 파란색 없애기

# 초록색만 뽑기
그림G = 그림RGB.copy() # 이렇게 해야 제대로 복사가 됩니다.
그림G[:,:,0] = 0 # 0: 빨간색 없애기
그림G[:,:,2] = 0 # 2: 파란색 없애기

# 파란색만 뽑기
그림B = 그림RGB.copy() # 이렇게 해야 제대로 복사가 됩니다.
그림B[:,:,0] = 0 # 0: 빨간색 없애기
그림B[:,:,1] = 0 # 1: 초록색 없애기

# 이 아래 부분은 그림을 화면에 출력하기 위한 부분으로, OpenCV 알고리즘과는 상관이 없습니다.
plt.subplot(1, 4, 1) # 1행 2열에서 1번째 열
plt.imshow(그림RGB)
plt.subplot(1, 4, 2) # 1행 2열에서 2번째 열
plt.imshow(그림R)
plt.subplot(1, 4, 3) # 1행 2열에서 2번째 열
plt.imshow(그림G)
plt.subplot(1, 4, 4) # 1행 2열에서 2번째 열
plt.imshow(그림B)
plt.show()

