import models
import my_pyketmon
from maps import map
from main import choice

all_map = []
all_map = map()

def bag():
    if models.bag_item == []:
        return "가방이 비어있다."
    else:
        print(models.bag_item)

class Move():

    def start(self):

        print("시작위치: ", end="")
        return all_map[models.i]

    def now(self):

        print("현재위치: ", end="")
        return all_map[models.i]

    def map(self):

        print("전체 지도: ", end="")
        return all_map

    def next(self):

        print(f"←{maps.all_map[models.i-1]} {maps.all_map[models.i+1]}→")

        arrow = input()
        if ord(arrow) == 37:
            i =- 1

        elif ord(arrow) == 39:
            i =+ 1

        print("이동합니다: ", end="")
        return all_map[models.i]

def poket():
    if my_pyketmon.my_paket == []:
        return "포켓몬이 없다."
    else:
        return my_pyketmon.my_paket


move = Move()

def move_check():
    move_choice_num = input("1.시작위치 2.현재위치 3.전체 지도 4.맵 이동")

    if move_choice_num == "1":
        move.start()

    elif move_choice_num == "2":
        move.now()

    elif move_choice_num == "3":
        move.map()

    elif move_choice_num == "4":
        move.next()

    else:
        return "없는 번호입니다."

def check(choice):
    return {"1" : bag, "2" : move_check, "3" : poket}.get(choice,'없는 번호입니다.')




result = check(choice)
print(result())