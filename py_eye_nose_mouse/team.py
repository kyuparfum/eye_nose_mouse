from random import random
import os
import time
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
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.max_hp = hp
        self.max_mp = mp
        self.power = power
        self.speed = speed
        self.critical = critical
        self.defense = defense


class Character():  # 전직시 nomal_attack
    def __init__(self, name, hp, mp, power, speed, critical, defense, normal_attack_name, level):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.max_hp = hp
        self.max_mp = mp
        self.power = power
        self.speed = speed
        self.critical = critical
        self.defense = defense
        self.normal_attack_name = normal_attack_name
        self.level = level
        level = 1
        # self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 일반공격(1)'))
        if active == 1:
            self.normal_attack(target)
        elif active < 0 or active > 1:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def normal_attack(self, target):  # 일반공격
        damage = random.randint(self.power*0.8, self.power*1.2)
        target.hp -= damage
        print(
            f"{self.name}의 {self.normal_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'================={self.name}상태정보=====================')
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")
        print(f"{self.name}의 상태: HP {self.mp}/{self.max_mp}")
        print(f'========================================================')


#           # 모험가
#               - 2연타 가능(맞은데 또 맞아라!)


class Adventurer_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        super().__init__(name, hp, mp, power, speed, critical,
                         defense)

    def magic_attack(self, target):  # 마법공격
        damage = random.randint(self.power*1.8, self.power*2.2)
        self.mp -= 10
        target.hp -= damage
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def Adventurer_Skill(self, target):
        self.magic_attack_name = print(f'맞은데 또 맞아라!')
        damage = random.randint(self.power*0.8, self.power*1.2)
        target.hp -= damage*2
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")
        # 노말어택 2번나가기

#               - 법사(썬,콜) 디버프(Monster def 감소)


class Magician_Character(Adventurer_Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense, level):
        super().__init__(name, hp, mp, power, speed, critical, defense, level)
        self.level = level
        level = player.level
        return

#               - 전사(파이터) 신체강화(power 증가)


class Warrior_Character(Adventurer_Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense, level):
        super().__init__(name, hp, mp, power, speed, critical, defense, level)
        return

#               - 도적(나이트로드) 회피율(Player speed 증가)


class Thief_Character(Adventurer_Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        super().__init__(name, )
        return

#               - 궁수(보우마스터) 명중율에따른 치명타확률 (critical)


class Archer_Character(Adventurer_Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        super().__init__(name, )
        return

#           # 레지스탕스
#               - 경험치가 2배(반란군의 발악)


class Resistance_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        super().__init__(name, )
        return

#               - 법사(배틀메이지) 디버프(Monster def 감소)


class Magician_Character(Resistance_Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        super().__init__(name, )
        return

#               - 전사() 신체강화(power 증가)


class Warrior_Character(Resistance_Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        super().__init__(name, )
        return

#               - 도적(메카닉?) 회피율(Player speed 증가)


class Thief_Character(Resistance_Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        super().__init__(name, )
        return

#               - 궁수(와일드헌터) 명중율에따른 치명타확률 (critical)


class Archer_Character(Resistance_Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        super().__init__(name, )
        return

#           # 시그너스
#               - 보상(100%)이 2배(여신의 축복)


class Cygnus_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        super().__init__(name, )
        return
#               - 법사(플레임위자드) 디버프(Monster def 감소)
#               - 전사(소울마스터) 신체강화(power 증가)
#               - 도적(나이트워커) 회피율(Player speed 증가)
#               - 궁수(윈드브레이커) 명중율에따른 치명타확률 (critical)
#           # 직업군 버프
#           = 모험가
#               - 2연타 가능(맞은데 또 맞아라!)
#           = 레지스탕스
#               - 경험치가 2배(반란군의 발악)
#           = 시그너스
#               - 보상(100%)이 2배(여신의 축복)

#           # 레벨업, 보상(골드, 아이템)
#               - 레벨상승
#               - 보상(골드, 아이템) 분배


# 게임 시작
name = input("캐릭터의 이름을 입력하세요: ")
player = Character(name, 100, 200, 10, 20, 30, 50, 10)
monster = Monster("슬라임", 50, 5, 10, 11, 12, 13)
while True:
    player.show_status()
    player.attack_box(monster)
    if monster.hp == 0:
        print("\33[33m승리했습니다!\33[0m")
        break

    if player.hp == 0:
        print("\33[91m 패배했습니다...\33[0m")
        break
# (self, name, hp, mp, power, speed, critical, defense, normal_attack_name, magic_attack_name):
# (self, name, hp, mp, power, speed, critical, defense):
#     - 몬스터 사냥 성공시 보상에 따른 게임 진행이 되어야 합니다.
#           #탑오르기?층오르기?
#               - 층마다 레벨업 및 아이템보상
#               - 팀장님 짱
#               - 보상 : 골드랑 회복물약
#                   보상은 골드/회복물약/골드+회복물약 중 확률적으로 얻음 (시그너스 제외)
#               - 회복물약은 1개씩만 제공
#               - 골드는 최대 1개 제공, 골드 3개당 물약 1 개 구매가능 (상점)
#           !몬스터! 강함의 차이?
#             # 고블린
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
