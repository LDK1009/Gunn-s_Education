import cv2
import matplotlib.pyplot as plt

# 이미지 불러오기
img = cv2.imread('./ImgSample.jpg')

# 이미지 정보 출력
print(type(img)) # 이미지 타입 출력
print(img.shape) # 이미지 높이, 너비, 채널수 출력

# 이미지 시각화 
plt.imshow(img) # cv2는 이미지 컬러 정보를 BGR 순으로 가진다. 이에 사진 출력 시 예상과 다르게 출력된다.

# 컬러 순서 정렬 후 시각화
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 이에 cv2로 불러온 컬러 이미지의 BGR 값을 RGB 값으로 정렬한다.
plt.imshow(fix_img) # 색상이 정상적인 이미지가 출력된다.

# 이미지 흑백으로 가져오기
img_gray = cv2.imread('./ImgSample.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray, cmap='gray')

# 이미지 리사이징
new_img = cv2.resize(fix_img, (800, 600))
plt.imshow(new_img)

# 이미지 상하반전
flip_img = cv2.flip(fix_img, 0)
plt.imshow(flip_img)

# 이미지 좌우반전
flip_img = cv2.flip(fix_img, 1)
plt.imshow(flip_img)

# 이미지 상하좌우반전
flip_img = cv2.flip(fix_img, -1)
plt.imshow(flip_img)