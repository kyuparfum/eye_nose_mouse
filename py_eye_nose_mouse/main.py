from Dungeon import *
from team import *
import random
import os
import time
from random import randint

# 게임 시작 화면입니다. 이거는 나중에 main파일 만들어서 옮기는게 좋을 것 같아요!----------------
print(f"물마셔요 게임을 시작합니다 ")

while True:
    print(f"원하는 메뉴의 번호를 입력한 다음 Enter키를 누르세요. 꼴깍~! \n"
          f"1.게임시작 \n"
          f"2.게임설명 \n"
          f"3.게임종료 \n")
    command = input(">>")
    if command == '1':
        print(f'캐릭터의 이름을 입력해주세요. 꼴깍~!')
        hero = str(input('>>'))
        name = Adventurer_Character(hero)
        hp = 1000
        mp = 100
        power = randint(1, 10)
        speed = randint(1, 10)
        critical = randint(1, 10)
        level = 1
        player = Character(name, hp, mp, power, speed,
                           critical, '모험가일반공격딱대.', level)
        print(f'게임을 시작하겠습니다.')
        # game()
    elif command == '2':
        print(f"튜토리얼진행으로 넘으가기")
    elif command == '3':
        print("이용해주셔서 감사합니다.")
        break
    else:
        print("잘못 누르셨습니다.\n")
