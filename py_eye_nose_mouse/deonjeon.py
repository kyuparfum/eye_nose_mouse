# 인벤토리 클래스 입니다.-----------------------------
inventory = {"회복물약": 1, "완전회복물약": 0, "공격물약": 0, "방어물약": 0, "속도물약": 0}


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

    # 아이템 사용하는 메소드 넣기


player_inventory = Inventory()

# 화폐를 만들어 보겠습니다.....-소진


# 게임 시작 화면입니다. 이거는 나중에 main파일 만들어서 옮기는게 좋을 것 같아요!----------------
print("ooo게임을 시작합니다 ")
print("게임 캐릭터명을 입력하세요")

id = str(input(""))

print(" 마왕성의 탑에 오신 것을 환영합니다. ")

while True:
    print("원하는 메뉴의 번호를 입력한 다음 Enter키를 누르세요.")
    print("1.게임시작")
    print("2.게임설명")
    print("3.게임종료")
    command = input(">>")
    if command == '1':
        print("탑에 입장하기")
    elif command == '2':
        print("튜토리얼진행으로 넘으가기")
    elif command == '3':
        print("이용해주셔서 감사합니다.")
        break
    else:
        print("잘못 누르셨습니다.\n")


# 상점 이용 함수입니다.-----------------------------
def shop():
    potion = ["회복물약", "완전회복물약", "공격물약", "방어물약", "속도물약"]

    print("상점에 진입했습니다. 상점을 이용 하시겠습니다? y: 상점 이용하기 n: 다음층으로")
    ans = input(">>")
    if ans == "y":
        while True:
            print("구입하려는 번호를 입력한 다음 Enter키를 누르세요.")
            print("1. 50% 회복물약 - 10gold")
            print("2. 완전회복물약 - 17gold")
            print("3. 공격 물약 - 30gold")
            print("4. 방어 물약 - 30gold")
            print("5. 속도 물약 - 30gold")
            buy_choice = input(">>")
            while True:
                if buy_choice == "1":
                    # 포션클래스의 구매메소드?!
                    print("회복물약은 체력을 50% 증가시켜줍니다. 구매하시겠습니까?")
                    print("y.예 n.아니오(상점으로 돌아가기)")
                    buy_ans = input(">>")
                    # 돈 빠져나가기
                    # Character의 inventory로 50%회복물약이 들어오고 -10gold
                    if buy_ans == "y":
                        player_inventory.addItem("회복물약")
                        print("상점으로 돌아가시겠습니까?")
                        print("1.상점으로 돌아가기 2.탑으로 이동하기)")
                        shop_ans = input(">>")
                        if shop_ans == '1':
                            break
                        elif shop_ans == '2':
                            print('탑으로 이동')
                        # 사고나서 바로 취식가능
                    elif buy_ans == "n":
                        break
                    else:
                        print("잘못 입력하셨습니다. y/n 중 선택해 주세요.")
                        print("")
                        continue
    elif ans == 'n':
        # 다음층으로 이동
        pass


# 존댓말함수(글씨만쓰면다냐............ 구현도해라....! (반말아닙니다.))
print(f"{self.name}의 {self.hp}!")


#     - 몬스터 사냥 성공시 보상에 따른 게임 진행이 되어야 합니다.
#           #탑오르기?층오르기?
#               - 층마다 레벨업 및 아이템보상
#               - 팀장님 짱
#               - 보상 : 골드랑 회복물약
#                   보상은 골드/회복물약/골드+회복물약 중 확률적으로 얻음 (시그너스 제외)
#               - 회복물약은 최대 1개 획득
#
#       - 던전 및 상점 구현 (골드로 회복물약사기, 골드3개당 회복물약 1개)

#               기본캐릭터로 시작 > 모험가, 레지, 시그 종족버프 설명 거기서 종족만 택1 >
#               > n층 돌파시 직업선택 > n층 돌파시 전직
#
# 1층 격파 -> 레벨업 -> 2층 격파 ->레벨업 ...총 25층
# 골드는 층수에 비례해서 획득
# 상점은 5층마다 등장
# 상점 물품 : 회복물약 50%, 회복물약 100%, 공격력 10%up, 방어력 10%up, speed 10%up
#           10골드       17골드        30골드       30골드        30골드
#  1층~10층 0~5골드. 11층 ~ 20층 5~10골드, 21~25층 11~15골드
# 10층마다 필드몬, 25층은 보스방 (혜린님방)
# 공격시 공격 or 아이템사용(물약) or 도망가기(상점가기)
