import time
import sys


def start_hi(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # Adjust this value to control the typing speed


def endding_bye(text_2):
    for char in text_2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


# 게임 설명 -----------------------------


def tutorial():
    allbreak = True
    while True:
        start_hi(f"\n\033[33m============================= 게임방법 =============================\n"
                 f"당신은 몬스터를 무찌르고자 탑에 올랐습니다.\n"
                 f"번호를 입력하여 공격할 몬스터를 선택하고 공격을 할 수 있습니다.\n"
                 f"상점에서는 탑을 오르는데 도움이 되는 다양한 상품을 팔고 있습니다.\n"
                 f"당신의 힘으로 이 세상을 구해주세요.\n"
                 f"=============================    중략    =============================\n\033[0m")

        start_hi(f"\033[33m\n============================= 게임 tip ===============================\n"
                 f"상점은 3층과 9층에서 등장합니다\n"
                 f"5층에 도달하면 5가지 직업 중 하나를 고를 수 있습니다.\n"
                 f"10층의 강력한 보스몬스터를 잡으면 탑을 클리어합니다.\n"
                 f"==============================    끝    ==============================\n\033[0m")
        while True:
            print('시작 화면으로 돌아가시겠습니까?\n 1.예 2.다시보기')
            a = input('>> ')
            if a == '1':
                allbreak = False
                break
            elif a == '2':
                break
            else:
                print("잘못된 선택입니다. 다시 선택 하세요")
                continue
        if allbreak == False:
            break
