
from tracemalloc import start
from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

#캐릭터 사각 운동, 삼각 운동, 원운동을 무한 반복
x, y = 400, 90 #초기위치

#원운동 변수
radius = 255
center_x, center_y = 400, 345


def move_to_point(start, end):
        global x, y
        speed = 200  # 픽셀/초
        delay_time = 0.01  # 초
        sx, sy = start
        ex, ey = end
        distance = math.sqrt((ex - sx) ** 2 + (ey - sy) ** 2)
        steps = int(distance / (speed * delay_time))
        if steps == 0:
            steps = 1
        dx = (ex - sx) / steps
        dy = (ey - sy) / steps

        for step in range(steps):
            clear_canvas_now()
            grass.draw_now(400, 30)
            x += dx
            y += dy
            character.draw_now(x, y)
            delay(delay_time)

        x, y = ex, ey 


#사각운동 함수
def move_square():
    global x, y
    #꼭짓점
    start = (x, y)
    Bright = (x+400,y)
    Tright = (x+400,y+510)
    Tleft = (x-400,y+510)
    Bleft = (x-400,y)
    move_to_point(start, Bright)
    move_to_point(Bright, Tright)
    move_to_point(Tright, Tleft)
    move_to_point(Tleft, Bleft)
    move_to_point(Bleft, start)


#원운동 함수
def move_circle():
    for degree in range(270, -90, -2):
        clear_canvas_now()
        grass.draw_now(400, 30)

        rad = degree / 360 * 2 * math.pi
        cx = center_x + radius * math.cos(rad)
        cy = center_y + radius * math.sin(rad)
        character.draw_now(cx, cy)
        delay(0.01)


def move_triangle():
    global x, y
    # 정삼각형 높이
    height = 550
    side = height / math.sin(math.radians(60))
    # 꼭짓점 계산
    start = (x, y)
    left = (x - (side / 2), y)
    right = (x + (side / 2), y)
    top = (x, y + height)

    # 삼각형의 각 변을 따라 이동
    move_to_point(start, right)
    move_to_point(right, top)
    move_to_point(top, left)
    move_to_point(left, start)


#무한반복
while True:
    move_square()    
    move_triangle()
    move_circle()