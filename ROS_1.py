import cv2  # OpenCV 라이브러리를 임포트

# 기본 카메라(0번 장치)를 사용하여 비디오 캡처 객체 생성
capture = cv2.VideoCapture(0)

# 캡처할 비디오 프레임의 너비를 640으로 설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

# 캡처할 비디오 프레임의 높이를 480으로 설정
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:  # 무한 루프 시작
    ret, frame = capture.read()  # 비디오 프레임을 읽어서 ret와 frame에 저장
    cv2.imshow("VideoFrame", frame)  # 읽어온 프레임을 "VideoFrame" 창에 표시
    
    if cv2.waitKey(10) == 27:  # 10밀리초 동안 키 입력을 기다림. ESC 키(ASCII 코드 27)가 입력되면 루프 종료
        break  # 무한 루프 종료

capture.release()  # 비디오 캡처 객체 해제
cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기
