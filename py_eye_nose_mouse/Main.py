from Mart import *
from Character import *
import random
import os
import time
import sys
from Start_End import *
from Game_start import *


# 게임 시작 -----------------------------
time.sleep(1)
print("\033[36m물마셔요 게임을 시작합니다\033[0m\n")

time.sleep(1)
print("\033[36m* 터미널을 최대로 늘려주세요 *\033[0m\n")

time.sleep(2)

# 시작 화면 -----------------------------
time.sleep(1)
start_hi(f"\033[33m==================== 게임설명 ======================\n"
         f"평화로운 헤네시스 였던 곳\n"
         f"이제는 나뭇잎마을이 되어버린곳\n"
         f"웨코문드가 되어 버린 곳\n"
         f"하늘섬이 되어 버린 곳\n"
         f"===================    중 략    ====================\n")

time.sleep(1)

while True:
    print(f"\n\033[33m원하는 메뉴의 번호를 입력한 다음 Enter키를 누르세요. 꼴깍~! \n"
          f"1.게임시작 \n"
          f"2.게임설명 \n"
          f"3.게임종료 \n\033[0m")
    command = input(">> ")
    if command == '1':
        player = player_make()

        print(f'게임을 시작하겠습니다.')
        game(player)

        break
    elif command == '2':
        tutorial()
    elif command == '3':
        print("\033[32m이용해주셔서 감사합니다.\033[0m")
        break
    else:
        print("\033[31m잘못 누르셨습니다.\033[0m\n")


time.sleep(3)
os.system('clear')  # 콘솔창 clear


endding_bye(f'\033[33m 게임 끝났어 {player.name}아(야) 고생했다~!\033[0m')
