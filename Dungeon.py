# 인벤토리 클래스 입니다.-----------------------------
inventory = {"회복물약": 1, "완전회복물약": 0, "공격물약": 0, "속도물약": 0}


class Inventory():
    # 아이템을 구매하는 코드

    def addItem(item):
        if item in inventory:
            inventory[item] += 1
            print(item, "구매를 완료하였습니다!")
        # 올바른 값을 입력하지 않은 경우
        else:
            print(item, "를 찾을 수 없습니다.")
    # 현재 가지고 있는 인벤토리를 확인하는 코드

    def showInventory():
        print("현재 인벤토리:")
        for item in inventory:
            if inventory[item] > 0:
                print(item, "x", inventory[item])


# 머리론 코딩이되지만 실행은되지않는다......
player_inventory = Inventory()


# 게임머니 클래스
class Currency:
    def __init__(self, money):
        self.money = money

    def add_money(self, money):
        self.money += money

    def sub_money(self, money):
        self.money += money

    def remove_money(self, money):
        if self.money < money:
            raise ValueError("골드가 부족합니다.")  # 물품대비 돈이 부족할 경우(value가 없는 오류가 발생)
        self.money -= money


my_money = Currency(0)  # 0골드을 가진 화폐 객체 생성

# my_money.add_money(5)  # 5골드 추가
# my_money.remove_money(3)  #3골드 빼기
# print(my_money.money)  # 5골드 출력

# 포션 클래스
# other는 Character(player)


class potion:
    def __init__(self, other):
        self.half_recovery_potion = other.hp + other.hp*1.5
        self.full_recovery_potion = max(other.hp + other.hp*2, other.max_hp)
        self.attack_potion = other.power*1.1
        self.speed_potion = other.speed*1.1

    def use(self, other):
        while True:
            print(f"어떤 물약을 사용 하시겠습니까? \n"
                  f"1. 50% 회복물약 \n"
                  f"2. 완전 회복물약 \n"
                  f"3. 공격 물약  \n"
                  f"4. 속도물약 \n"
                  f"5. 그만 사용하기 \n"
                  f"1. 50% 회복물약\n")

            # use_potion = int(input())로 받아서 활용합니다.
            use_potion = input(">>")
            if use_potion == "1":
                other.hp = self.half_recovery_potion
                print(f"{other.name}의 hp가 50% 회복했습니다.")
            elif use_potion == "2":
                other.hp = self.full_recovery_potion
                print(f"{other.name}의 hp가 완전히 회복했습니다.")
            elif use_potion == "3":
                other.power = self.attack_potion
                print(f"{other.name}의 공격력이 10% 상승합니다.")
            elif use_potion == "4":
                other.speed = self.speed_potion
                print(f"{other.name}의 속도가 10% 상승합니다.")
            elif not use_potion.isdigit():
                print("숫자로만 입력해 주세요.")
            elif use_potion == "5":
                break
            else:
                print("잘못된 선택입니다. 다시 선택 하세요")
                continue
# 1.=half_recovery_potion
# 2.=full_recovery_potion
# 3.=attack_potion
# 4.=speed_potion


# 상점 이용 함수입니다.-----------------------------
def shop():
    potion = ["회복물약", "완전회복물약", "공격물약", "속도물약"]

    print("상점에 진입했습니다. 상점을 이용 하시겠습니다? y: 상점 이용하기 n: 다음층으로")
    print("현재 가진 금액 : ", my_money, "골드")
    ans = input(">>")
    if ans == "y":
        while True:
            print(f"구입하려는 번호를 입력한 다음 Enter키를 누르세요. \n"
                  f"1. 50% 회복물약 - 10gold \n"
                  f"2. 완전회복물약 - 17gold \n"
                  f"3. 공격 물약 - 30gold \n"
                  f"4. 속도 물약 - 30gold ")
            buy_potion()
    elif ans == 'n':
        # 다음층으로 이동
        pass


# 물품 구매 함수 -------------------
def buy_potion():
    potion_list = [
        {"name": "회복물약", "effect": "체력을 50% 증가", "price": 10},
        {"name": "완전회복물약", "effect": "체력을 100% 증가", "price": 17},
        {"name": "공격물약", "effect": "공격력을 10% 증가", "price": 30},
        {"name": "속도물약", "effect": "속도를 10% 증가", "price": 30},
    ]
    buy_choice = input(">>")
    while True:
        a = int(buy_choice) - 1
        print(
            f"{potion_list[a]['name']}은 {potion_list[a]['effect']}시켜줍니다. 구매하시겠습니까?")
        print("y.예 n.아니오(상점으로 돌아가기)")
        buy_ans = input(">>")
        if buy_ans == "y":
            player_inventory.addItem(f"{potion_list[a]['name']}")
            my_money.remove_money(potion_list[a]["price"])
            print(f"상점으로 돌아가시겠습니까?"
                  f"1.상점으로 돌아가기 2.탑으로 이동하기")
            shop_ans = input(">>")
            if shop_ans == "1":
                break
            elif shop_ans == "2":
                print('탑으로 이동')
            # 사고나서 바로 취식가능
        elif buy_ans == "n":
            break
        else:
            print("잘못 입력하셨습니다. y/n 중 선택해 주세요.")
            print("")
            continue


# def game():
#     level = 0
#     floor = 0

#     while True:
#         if level <= 5:
#             print(f'탑의 {floor}층에 도착하였습니다.')
#             # 전투진행코드
#             if hp > 0:
#                 # 다음단계 진행 여부
#                 level += 1
#                 floor += 1
#             elif hp <= 0:
#                 # 재도전 여부?!
#             elif 5 < level <= 10:
#             # 위와 동일
#             # 상점?

#     #탑에 진입 전투 진행
#     #전투 승리시 lever +1, 층수 +1
#     #전투 종료 후 다음단계 진행 여부

# 탑에 입장하기
# 몇 층인지, 어떤 몬스터가 나오는지 등 정보제공
# 전투
# 전투보상은 레벨업과 골드 (1층~10층 0~5골드. 11층 ~ 20층 5~10골드, 21~25층 11~15골드 + 층마다 일정확률로 회복포션 1개)
# 5층마다 상점 도착
# 상점은 각종 포션 구입
# 마지막 10층 보스방
# 층마다 lv up
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
#
# 탑에 입장하기
# 1층 - 5층 고블린
# 5층 상점
# 6 - 10층
# 10층 상점
# 11 - 15층
# 15층 상점
# 16 - 20층
# 20층 상점
# 21층 - 25층
# 축 꼭대기 도착 하

# 존댓말함수(글씨만쓰면다냐............ 구현도해라....! (반말아닙니다.))
# print(f"{self.name}의 {self.hp}!")
#
#     - 몬스터 사냥 성공시 보상에 따른 게임 진행이 되어야 합니다.
#           #탑오르기?층오르기?
#               - 층마다 레벨업 및 아이템보상
#               - 팀장님 짱
#               - 보상 : 골드랑 회복물약
#                   보상은 골드/회복물약/골드+회복물약 중 확률적으로 얻음 (시그너스 제외)
#               - 회복물약은 최대 1개 획득
#
#       - 던전 및 상점 구현 (골드로 회복물약사기, 골드3개당 회복물약 1개)
#
#               기본캐릭터로 시작 > 모험가, 레지, 시그 종족버프 설명 거기서 종족만 택1 >
#               > n층 돌파시 직업선택 > n층 돌파시 전직
#
# 1층 격파 -> 레벨업 -> 2층 격파 ->레벨업 ...총 25층
# 골드는 층수에 비례해서 획득
# 상점은 5층마다 등장
# 상점 물품 : 회복물약 50%, 회복물약 100%, 공격력 10%up, speed 10%up
#           10골드       17골드        30골드       30골드        30골드
#  1층~10층 0~5골드. 11층 ~ 20층 5~10골드, 21~25층 11~15골드
# 10층마다 필드몬, 25층은 보스방 (혜린님방)
# 공격시 공격 or 아이템사용(물약) or 도망가기(상점가기)
# 1 - 2층 : 리본돼지, 파란리본돼지, 와일드보어
# 3층 : 상점4 - 5층 : 주니어 예티,파이어드레이크,아이스드레이크/ 5층에서 전직 후 전투층 : 상점
# 7 - 8층 : 마뇽, 주니어발록, 발록
# 9층 : 상점
# 10층 : 페어리워터 박 ()
