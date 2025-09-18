
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

#사각운동 함수
def move_square():
    global x, y
    
    # 우하단 이동 
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

    # 우상단 이동
    while y < 600:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)

    # 좌상단 이동
    while x > 0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)

    # 좌하단 이동
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)

    # 중앙복귀
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

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


#무한반복
while True:
    move_square()
    move_circle()