import cv2
import matplotlib.pyplot as plt

그림BGR = cv2.imread("그림파일.jpg")
그림RGB = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2RGB)
세로, 가로, 채널 = 그림RGB.shape

대각선 = int(((가로*가로 + 세로*세로)**0.5)) # 정수여야 합니다.
회전중심 = int(가로/2), int(세로/2) # 역시 정수여야 합니다.
회전각도 = 135 # 마음대로 정하세요    
새세로, 새가로 = 세로, 가로

그림회전 = cv2.getRotationMatrix2D(회전중심, 회전각도, 1) # 1은 확대/축소값입니다.    
회전결과 = cv2.warpAffine(그림RGB, 그림회전, (새세로, 새가로))

# 이 아래 부분은 그림을 화면에 출력하기 위한 부분으로, OpenCV 알고리즘과는 상관이 없습니다.
plt.subplot(1, 2, 1) # 1행 2열에서 1번째 열
plt.imshow(그림RGB)

plt.subplot(1, 2, 2) # 1행 2열에서 2번째 열
plt.imshow(회전결과)

plt.show()

