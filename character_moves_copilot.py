from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 90 #초기위치

grass.draw_now(400, 30)
character.draw_now(x, y)
import time


# 사각형 경로 좌표 정의 (시작점이 x, y)
rect_points = [
	(x, y),
	(x + 350, y),
	(x + 350, y + 460),
	(x - 350, y + 460),
	(x - 350, y),
	(x, y)
]




# 사각형 경로 전체를 시작점(x, y) 기준으로 이동
for i in range(0, 5):
	x1, y1 = rect_points[i]
	x2, y2 = rect_points[i+1]
	for t in range(0, 101, 2):
		x_pos = x1 + (x2 - x1) * t / 100
		y_pos = y1 + (y2 - y1) * t / 100
		clear_canvas()
		grass.draw_now(400, 30)
		character.draw_now(x_pos, y_pos)
		update_canvas()
		time.sleep(0.01)





# 원운동 1회 (시작점 x, y에서 시계방향, 시작점이 원의 아래쪽)
center_x, center_y = x, y + 230
radius = 230
for degree in range(90, 630, 2):  # 270도에서 시작, 360도 회전
	rad = math.radians(-degree)
	x_pos = center_x + radius * math.cos(rad)
	y_pos = center_y + radius * math.sin(rad)
	clear_canvas()
	grass.draw_now(400, 30)
	character.draw_now(x_pos, y_pos)
	update_canvas()
	time.sleep(0.01)