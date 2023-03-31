# from random import randint, random

import random
# import os
# import time
# - 규칙
#     - 협업을 위해 코드 컨벤션을 정해야 합니다.
#     - 기능별로 파일을 나눠 작업해야 합니다.
#     - 함수, 클래스를 사용해 중복된 코드 사용을 최소화해야 합니다.
# - 기능
#     - 플레이어의 직업이 있고 직업별 특수 능력이 있어야 합니다.
#           - 계열 : 모험가(5+n), 레지스탕스(5+n), 시그너스(5+n)
#           - 특수능력 : 직업별로 기술?(전사,도적,법사,궁수)추가

#           # 직업군
#               - 법사(플레임위자드) 디버프(Monster def 감소)
#               - 전사(소울마스터) 신체강화(power 증가)
#               - 도적(나이트워커) 회피율(Player speed 증가)
#               - 궁수(윈드브레이커) 명중율에따른 치명타확률 (critical)
#           # 직업군 버프
#           = 모험가
#               - 2연타 가능(맞은데 또 맞아라!)

#           # 레벨업, 보상(골드, 아이템)
#               - 레벨상승
#               - 보상(골드, 아이템) 분배

# 몬스터 모체 -----------------------------


class Monster():
    def __init__(self, name, hp, power, speed, normal_attack_name):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.power = power
        self.speed = speed
        self.normal_attack_name = normal_attack_name

    def normal_attack(self, target):  # 일반공격
        m_damage = random.randint(self.power-5, self.power+5)
        target.hp = max(target.hp - m_damage, 0)
        print(
            f"{self.name}의 {self.normal_attack_name}! {target.name}에게 {m_damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"\033[33m================ {self.name}의 상태정보=====================\n"
              f"{self.name}의 상태: HP {self.hp}/{self.max_hp}\n"
              f"================= {self.name}의 상태정보 끝 ==================\033[0m")

# 플레이어 모체 -----------------------------


class Character():  # 전직시 normal_attack
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.max_hp = hp
        self.max_mp = mp
        self.power = power  # 고정값?줄까요?
        self.speed = speed
        self.critical = critical
        # self.normal_attack_name = self.power * randint(1, self.power * 10)
        self.normal_attack_name = normal_attack_name
        self.level = level

    def attack_box(self, target):
        active = int(input('공격선택 일반공격(1)'))
        if active == 1:
            self.normal_attack(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 1:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def normal_attack(self, target):  # 일반공격
        damage = random.randint(self.power*2, self.power*3)
        target.hp = max(target.hp - damage, 0)
        print(
            f"{self.name}의 \033[93m{self.normal_attack_name}!\033[0m {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'\033[33m================= {self.name}의 상태정보 =====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 : 나는 배짱이 \n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f"================= {self.name}의 상태정보 끝 ==================\033[0m")


# 모험가 -----------------------------
# 2연타 가능(맞은데 또 맞아라!)


class Adventurer_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(name, hp, mp, power, speed,
                         critical, normal_attack_name, level)
        self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 :\n 일반공격(1) \n 마법공격(2)'))
        if active == 1:
            self.normal_attack(target)
        elif active == 2:
            self.Adventurer_Skill(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 2:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def magic_attack(self, target):  # 마법공격
        if self.mp >= 10:
            damage = random.randint(self.power*2, self.power*3)
            self.mp -= 10
            target.hp = max(target.hp - damage, 0)
            print(
                f"{self.name}의 \033[93m{self.magic_attack_name}!\033[0m {target.name}에게 {damage}의 데미지를 입혔습니다.")
            if target.hp == 0:
                print(f"{target.name}이(가) 쓰러졌습니다.")
        else:
            # 마나가 부족할 경우
            print("\033[32m마나가 부족하여 마법공격을 할 수 없습니다.\033[0m")

    def Adventurer_Skill(self, target):
        self.magic_attack_name = print(f'\033[32m 맞은데 또 맞아라!\033[0m ')
        magic_name = '맞은데 또 맞아라!'
        damage = random.randint(self.power*1, self.power*2)
        target.hp = max(target.hp - damage*2, 0)
        print(
            f"{self.name}의\033[32m {magic_name}발동!\033[0m {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'\033[33m================= {self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 : 숨겨진 직업 \n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f"================= {self.name}의 상태정보 끝 ==================\033[0m")

# 법사 -----------------------------
# 6,000만 볼트 뇌룡


class Magician_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(name, hp, mp, power, speed,
                         critical, normal_attack_name, level)
        self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 :\n 일반공격(1) \n 마법공격(2)'))
        if active == 1:
            self.normal_attack(target)
        elif active == 2:
            self.Adventurer_Skill(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 2:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def magic_attack(self, target):  # 마법공격
        if self.mp >= 10:
            damage = random.randint(self.power*2, self.power*3)
            self.mp -= 10
            target.hp = max(target.hp - damage, 0)
            print(
                f"{self.name}의 \033[93m{self.magic_attack_name}!\033[0m {target.name}에게 {damage}의 데미지를 입혔습니다.")
            if target.hp == 0:
                print(f"{target.name}이(가) 쓰러졌습니다.")
        else:
            # 마나가 부족할 경우
            print("\033[32m마나가 부족하여 마법공격을 할 수 없습니다.\033[0m")

    def Magician_Skill(self, target):
        self.magic_attack_name = print(f'\033[34m6,000만 볼트 뇌룡\033[0m')
        damage = random.randint(self.power*1, self.power*2)
        target.hp = max(target.hp - damage*2, 0)
        print(
            f"{self.name}의 \033[34m{self.magic_attack_name}\033[0m! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'\033[33m================= {self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 : 마법사(갓에넬) \n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f"================= {self.name}의 상태정보 끝 ==================\033[0m")


# 전사 -----------------------------
# 천본앵경엄(せんぼんざくらかげよし)
class Warrior_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(name, hp, mp, power, speed,
                         critical, normal_attack_name, level)
        self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 :\n 일반공격(1) \n 마법공격(2)'))
        if active == 1:
            self.normal_attack(target)
        elif active == 2:
            self.Adventurer_Skill(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 2:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def magic_attack(self, target):  # 일반공격
        if self.mp >= 10:
            damage = random.randint(self.power*2, self.power*3)
            self.mp -= 10
            target.hp = max(target.hp - damage, 0)
            print(
                f"{self.name}의 \033[93m{self.magic_attack_name}!\033[0m {target.name}에게 {damage}의 데미지를 입혔습니다.")
            if target.hp == 0:
                print(f"{target.name}이(가) 쓰러졌습니다.")
        else:
            # 마나가 부족할 경우
            print("\033[32m마나가 부족하여 마법공격을 할 수 없습니다.\033[0m")

    def Warrior_Skill(self, target):
        self.magic_attack_name = print(f'\033[91m천본앵경엄(せんぼんざくらかげよし)\033[0m')
        damage = random.randint(self.power*1, self.power*2)
        target.hp = max(target.hp - damage*2, 0)
        print(
            f"{self.name}의 \033[91m{self.magic_attack_name}\033[0m! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'\033[33m================= {self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 :  전사(바쿠야)\n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f"================= {self.name}의 상태정보 끝 ==================\033[0m")


# 도적(나이트로드)  -----------------------------
# 회피율(Player speed 증가)

class Thief_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(name, hp, mp, power, speed,
                         critical, normal_attack_name, level)
        self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 :\n 일반공격(1) \n 마법공격(2)'))
        if active == 1:
            self.normal_attack(target)
        elif active == 2:
            self.Adventurer_Skill(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 2:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def magic_attack(self, target):  # 일반공격
        if self.mp >= 10:
            damage = random.randint(self.power*2, self.power*3)
            self.mp -= 10
            target.hp = max(target.hp - damage, 0)
            print(
                f"{self.name}의 \033[93m {self.magic_attack_name}!\033[0m  {target.name}에게 {damage}의 데미지를 입혔습니다.")
            if target.hp == 0:
                print(f"{target.name}이(가) 쓰러졌습니다.")
        else:
            # 마나가 부족할 경우
            print("\033[32m마나가 부족하여 마법공격을 할 수 없습니다.\033[0m")

    def Thief_Skill(self, target):
        self.magic_attack_name = print(f'\033[36m나선환!(らせんがん)!\033[0m')
        damage = random.randint(self.power*1, self.power*2)
        target.hp = max(target.hp - damage*2, 0)
        print(
            f"{self.name}의 \033[36m{self.magic_attack_name}\033[0m! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'\033[33m================= {self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 : 도적(나스케(나루토 사스케)) \n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f"================= {self.name}의 상태정보 끝 ==================\033[0m")


# 궁수(보우마스터)  -----------------------------
# 명중율에따른 치명타확률 (critical)

class Archer_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(name, hp, mp, power, speed,
                         critical, normal_attack_name, level)
        self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 :\n 일반공격(1) \n 마법공격(2)'))
        if active == 1:
            self.normal_attack(target)
        elif active == 2:
            self.Adventurer_Skill(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 2:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def magic_attack(self, target):  # 일반공격
        if self.mp >= 10:
            damage = random.randint(self.power*2, self.power*3)
            self.mp -= 10
            target.hp = max(target.hp - damage, 0)
            print(
                f"{self.name}의 \033[32m {self.magic_attack_name}!\033[0m  {target.name}에게 {damage}의 데미지를 입혔습니다.")
            if target.hp == 0:
                print(f"{target.name}이(가) 쓰러졌습니다.")
        else:
            # 마나가 부족할 경우
            print("\033[32m마나가 부족하여 마법공격을 할 수 없습니다.\033[0m")

    def Archer_Skill(self, target):
        self.magic_attack_name = print(
            f'\033[34m하일리히 프파일 (Heilig Pfeil)\033[0m')
        damage = random.randint(self.power*1, self.power*2)
        target.hp = max(target.hp - damage*2, 0)
        print(
            f"{self.name}의 \033[34m{self.magic_attack_name}\033[0m! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'\033[33m================= {self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 :  궁수(유하바하)\n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f"================= {self.name}의 상태정보 끝 ==================\033[0m")


# 몬스터 목록  -----------------------------
monster_level_1 = [Monster("리본돼지", 50, 5, 10, "\033[95m애교부리기 !\033[0m")]
monster_level_2 = [Monster("파란리본돼지", 60, 7, 10, "\033[95m귀여운 애교부리기 !\033[0m")]
monster_level_3 = [Monster("와일드보어", 80, 15, 12, "\033[97m몸통박치기 !\033[0m")]
monster_level_4 = [Monster("주니어예티", 100, 10, 10, "\033[90m내려찍기 !\033[0m")]
monster_level_5 = [Monster("파이어드레이크", 110, 10, 12, "\033[31m화염방사 !\033[0m")]
monster_level_6 = [Monster("아이스드레이크", 130, 20, 12, "\033[34m냉동펀치 !\033[0m")]
monster_level_7 = [Monster("마뇽", 140, 15, 15, "\033[35m오로라 브레스 !\033[0m")]
monster_level_8 = [Monster("주니어발록", 150, 20, 15, "\033[32m파이어 볼 !\033[0m")]
monster_level_9 = [Monster("발록", 160, 30, 15, "\033[30m떨어트리기 !\033[0m")]
monster_level_10 = Monster("페어리워터_박", 300, 100, 30,
                           "\033[34m여러분 물 마셔요~!(꼴깍)\033[0m")

monster_dic = {
    "level_low": monster_level_1 + monster_level_2 + monster_level_3,
    "level_middle": monster_level_4 + monster_level_5 + monster_level_6 + monster_level_7 + monster_level_8 + monster_level_9,
    "level_boss": monster_level_3 + monster_level_6 + monster_level_9
}


#     - 몬스터 사냥 성공시 보상에 따른 게임 진행이 되어야 합니다.
#           #탑오르기?층오르기?
#               - 층마다 레벨업 및 아이템보상
#               - 팀장님 짱
#               - 보상 : 골드랑 회복물약
#                   보상은 골드/회복물약/골드+회복물약 중 확률적으로 얻음 (시그너스 제외)
#               - 회복물약은 1개씩만 제공
#               - 골드는 최대 1개 제공, 골드 3개당 물약 1 개 구매가능 (상점)


#     - 몬스터와 1:N or N:M 전투가 가능해야 합니다.
#           - 전투 입장시 Monster객체 수 1~n 랜덤생성, 타겟팅해서 공격가능하게
#           - 입력되는 몬스터이름은 대표몬스터의 이름
#           - 전투입장시 대표몬스터 1마리와 하위 몬스터 1~n마리 등장
#               ex) 주니어발록과의 전투 시작!
#                   주니어발록(필드몬, 대표몬스터), 카파드레이크(일반몬), 홉고블린(ㄹㅇ잔몹)
#
#               기본캐릭터로 시작 > 모험가, 레지, 시그 종족버프 설명 거기서 종족만 택1 >
#               > n층 돌파시 직업선택 > n층 돌파시 전직
#

# 만들어야 할 코드들
#       - 캐릭터 직업, 스킬, 몬스터직업&스킬 -> 2명 진규,현식
#       - 던전 및 상점 구현 (골드로 회복물약사기, 골드3개당 회복물약 1개) -> 3명 소진,혜린,명흠
#       - 메인 전투 -> 보류
#
#     깃허브여기로쓸게요 https://github.com/kyuparfum/eye_nose_mouse
