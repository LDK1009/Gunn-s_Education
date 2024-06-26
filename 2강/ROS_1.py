import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,6,0.01)
# print(t.shape)

y = np.sin(np.pi * 5 * t)
# print(y.shape)



def draw_sin(t, A, f, b):
    y=A*np.sin(np.pi * f * t) +b
    # 그래프의 크기를 가로 12인치, 세로 6인치로 설정합니다.
    plt.figure(figsize=(12, 6))
    # t와 y 데이터 시리즈를 사용하여 라인 그래프를 그립니다.
    plt.plot(t, y)
    # 그래프에 그리드를 추가하여 가로세로 축의 선을 표시합니다.
    plt.grid()
    # 그래프를 화면에 표시합니다.
    plt.show()
    
draw_sin()