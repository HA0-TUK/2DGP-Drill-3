
from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

# 사각형 이동 함수
def move_rectangle(x, y):
	rect_points = [
		(x, y),
		(x + 350, y),
		(x + 350, y + 460),
		(x - 350, y + 460),
		(x - 350, y),
		(x, y)
	]
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

# 삼각형 이동 함수
def move_triangle(x, y):
	triangle_height = 460
	side = 2 * triangle_height / math.sqrt(3)
	triangle_points = [
		(x, y),                    # 밑면 중앙에서 시작
		(x + side/2, y),           # 오른쪽 아래
		(x, y + triangle_height),  # 위 꼭짓점
		(x - side/2, y),           # 왼쪽 아래
		(x, y)                     # 다시 밑면 중앙
	]
	for i in range(4):
		x1, y1 = triangle_points[i]
		x2, y2 = triangle_points[i+1]
		for t in range(0, 101, 2):
			x_pos = x1 + (x2 - x1) * t / 100
			y_pos = y1 + (y2 - y1) * t / 100
			clear_canvas()
			grass.draw_now(400, 30)
			character.draw_now(x_pos, y_pos)
			update_canvas()
			time.sleep(0.01)

# 원 이동 함수
def move_circle(x, y):
	center_x, center_y = x, y + 230
	radius = 230
	for degree in range(90, 450, 2):
		rad = math.radians(-degree)
		x_pos = center_x + radius * math.cos(rad)
		y_pos = center_y + radius * math.sin(rad)
		clear_canvas()
		grass.draw_now(400, 30)
		character.draw_now(x_pos, y_pos)
		update_canvas()
		time.sleep(0.01)



# 초기 위치
x, y = 400, 90

# 캔버스 및 이미지 로드
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

# 세가지 운동을 번갈아가며 무한 반복
while True:
	move_rectangle(x, y)
	move_triangle(x, y)
	move_circle(x, y)