# # from random import randint, random
# import random
# import os
# import time
# from random import randint
# - 규칙
#     - 협업을 위해 코드 컨벤션을 정해야 합니다.
#     - 기능별로 파일을 나눠 작업해야 합니다.
#     - 함수, 클래스를 사용해 중복된 코드 사용을 최소화해야 합니다.
# - 기능
#     - 플레이어의 직업이 있고 직업별 특수 능력이 있어야 합니다.
#           - 계열 : 모험가(5+n), 레지스탕스(5+n), 시그너스(5+n)
#           - 특수능력 : 직업별로 기술?(전사,도적,법사,궁수)추가
# 모체니깐 기본만다넣기


class Monster():
    def __init__(self, name, hp, power, speed, normal_attack_name):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.power = power
        self.speed = speed
        self.normal_attack_name = normal_attack_name

    def normal_attack(self, target):  # 일반공격
        m_damage = random.randint(self.power*0.8, self.power*1.2)
        target.hp -= m_damage
        print(
            f"{self.name}의 {self.normal_attack_name}! {target.name}에게 {m_damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'================={self.name}상태정보=====================')
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")
        print(f'========================================================')


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
        target.hp -= damage
        print(
            f"{self.name}의 {self.normal_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'================={self.name}상태정보=====================')
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")
        print(f"{self.name}의 상태: MP {self.mp}/{self.max_mp}")
        print(f'========================================================')


#           # 모험가
#               - 2연타 가능(맞은데 또 맞아라!)


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
        damage = random.randint(self.power*2, self.power*3)
        self.mp -= 10
        target.hp -= damage
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def Adventurer_Skill(self, target):
        self.magic_attack_name = print(f'맞은데 또 맞아라!')
        magic_name = '맞은데 또 맞아라!'
        damage = random.randint(self.power*1, self.power*2)
        target.hp -= damage*2
        print(
            f"{self.name}의\33[32m {magic_name}발동!\33[0m {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")
        # 노말어택 2번나가기

#               - 법사(썬,콜) 디버프(Monster def 감소)


class Magician_Character(Adventurer_Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(self, name, hp, mp, power, speed, critical,
                         normal_attack_name, level)

    def Magician_Skill(self, target):
        self.magic_attack_name = print(f'6,000만 볼트 뇌룡')
        damage = random.randint(self.power*1, self.power*2)
        target.hp -= damage*2
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

#               - 전사(파이터)


class Warrior_Character(Adventurer_Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(self, name, hp, mp, power, speed, critical,
                         normal_attack_name, level)

    def Warrior_Skill(self, target):
        self.magic_attack_name = print(f'천본앵경엄(せんぼんざくらかげよし)')
        damage = random.randint(self.power*1, self.power*2)
        target.hp -= damage*2
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

#               - 도적(나이트로드) 회피율(Player speed 증가)


class Thief_Character(Adventurer_Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(self, name, hp, mp, power, speed, critical,
                         normal_attack_name, level)

    def Thief_Skill(self, target):
        self.magic_attack_name = print(f'나선환!(らせんがん)!')
        damage = random.randint(self.power*1, self.power*2)
        target.hp -= damage*2
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

#               - 궁수(보우마스터) 명중율에따른 치명타확률 (critical)


class Archer_Character(Adventurer_Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(self, name, hp, mp, power, speed, critical,
                         normal_attack_name, level)

    def Archer_Skill(self, target):
        self.magic_attack_name = print(f'하일리히 프파일 (Heilig Pfeil)')
        damage = random.randint(self.power*1, self.power*2)
        target.hp -= damage*2
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")


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


# 게임 시작
# class Character():  # 전직시 normal_attack
#     def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level):
# self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name

hp = 1000
mp = 100
power = randint(1, 10)
speed = randint(1, 10)
critical = randint(1, 10)
level = 1
# player = Character(name, hp, mp, power, speed, critical, '모험가일반공격딱대.', level)
# Adventurer = Adventurer_Character(player.name, player.hp, player.mp, player.power,
#                                   player.speed, player.critical, '살려주면좋겠다~!', player.level, '나는 죽지 않는다.')
# Magician = Magician_Character(player.name, player.hp, player.mp, player.power,
#                               player.speed, player.critical, '100만 볼트 방전', player.level, '6,000만 볼트 뇌룡')
# Warrior = Warrior_Character(player.name, player.hp, player.mp, player.power,
#                             player.speed, player.critical, '천본앵((せんぼんざくら)', player.level, '천본앵경엄(せんぼんざくらかげよし)!')
# Thief = Thief_Character(player.name, player.hp, player.mp, player.power,
#                         player.speed, player.critical, '치도리(き千鳥)', player.level, '나선환!(らせんがん)!')
# Archer = Archer_Character(player.name, player.hp, player.mp, player.power,
#                           player.speed, player.critical, '영자병장(靈子兵裝)', player.level, '하일리히 프파일 (Heilig Pfeil)')


# name, hp, power, speed선공율, normal_attack_name):
monster_low = Monster("리본돼지", 50, 5, 10, "애교부리기 !")
monster_low = Monster("파란리본돼지", 60, 7, 10, "귀여운 애교부리기 !")
monster_low = Monster("와일드보어", 80, 15, 12, "몸통박치기 !")
monster_middle = Monster("주니어예티", 100, 10, 10, "내려찍기 !")
monster_middle = Monster("파이어드레이크", 110, 10, 12, "화염방사 !")
monster_middle = Monster("아이스드레이크", 130, 20, 12, "냉동펀치 !")
monster_high = Monster("마뇽", 140, 15, 15, "오로라 브레스 !")
monster_high = Monster("주니어발록", 150, 20, 15, "파이어 볼 !")
monster_high = Monster("발록", 160, 30, 15, "떨어트리기 !")
monster_boss = Monster("페어리워터_박", 300, 100, 30, "여러분 물 마셔요~!(꼴깍)")


# (self, name, hp, mp, power, speed, critical, , normal_attack_name, magic_attack_name):
# (self, name, hp, mp, power, speed, critical, ):
#     - 몬스터 사냥 성공시 보상에 따른 게임 진행이 되어야 합니다.
#           #탑오르기?층오르기?
#               - 층마다 레벨업 및 아이템보상
#               - 팀장님 짱
#               - 보상 : 골드랑 회복물약
#                   보상은 골드/회복물약/골드+회복물약 중 확률적으로 얻음 (시그너스 제외)
#               - 회복물약은 1개씩만 제공
#               - 골드는 최대 1개 제공, 골드 3개당 물약 1 개 구매가능 (상점)
#           !몬스터! 강함의 차이?
#             # 고블린 (1층 ~)
#               - 고블린(ㄹㅇ잔몹)
#               - 홉고블린(ㄹㅇ잔몹)
#               - 고블린로드(ㄹㅇ잔몹 중에서 나는 보스)
#             # 드레이크
#               - 카파드레이크(일반몬)
#               - 레드드레이크(일반몬)
#               - 아이스드레이크(일반몬)
#               - 다크드레이크(일반몬)
#             # 발록
#               - 주니어발록(필드몬)
#               - 발록(보스몬)
#             # 물의요정(혜린님)
#               - 페어리워터(울트라전설보스몬)=나랑비슷하게쎔....?


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
#
#
#                               정해야할게뭘까요?ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ도와주세요 ㅠㅠㅠㅠㅠㅠㅠㅠ
#                               메이플스토리 : 직업이무지하게많고 몬스터도넘쳐흘립니다. 레벨 및 전직
#
#                       투표소 1. : 0 , 2. : 0           투표완료 : 마우스위치( )


# 만들어야 할 코드들
#       - 캐릭터 직업, 스킬, 몬스터직업&스킬 -> 2명 진규,현식
#       - 던전 및 상점 구현 (골드로 회복물약사기, 골드3개당 회복물약 1개) -> 3명 소진,혜린,명흠
#       - 메인 전투 -> 보류
#           -
#
#     깃허브여기로쓸게요 https://github.com/kyuparfum/eye_nose_mouse
