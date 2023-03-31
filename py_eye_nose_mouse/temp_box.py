#           # 레지스탕스
#               - 경험치가 2배(반란군의 발악)


# class Resistance_Character(Character):
#     def __init__(self, name, hp, mp, power, speed, critical, defense):
#         super().__init__(name, )
#         return

#               - 법사(배틀메이지) 디버프(Monster def 감소)


# class Magician_Character(Resistance_Character):
#     def __init__(self, name, hp, mp, power, speed, critical, defense):
#         super().__init__(name, )
#         return

#               - 전사() 신체강화(power 증가)


# class Warrior_Character(Resistance_Character):
#     def __init__(self, name, hp, mp, power, speed, critical, defense):
#         super().__init__(name, )
#         return

#               - 도적(메카닉?) 회피율(Player speed 증가)


# class Thief_Character(Resistance_Character):
#     def __init__(self, name, hp, mp, power, speed, critical, defense):
#         super().__init__(name, )
#         return

#               - 궁수(와일드헌터) 명중율에따른 치명타확률 (critical)


# class Archer_Character(Resistance_Character):
#     def __init__(self, name, hp, mp, power, speed, critical, defense):
#         super().__init__(name, )
#         return

#           # 시그너스
#               - 보상(100%)이 2배(여신의 축복)


# class Cygnus_Character(Character):
#     def __init__(self, name, hp, mp, power, speed, critical, defense):
#         super().__init__(name, )
#         return


#           = 레지스탕스
#               - 경험치가 2배(반란군의 발악)
#           = 시그너스
#               - 보상(100%)이 2배(여신의 축복)


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
# 골드는 층수에 비례해서 획득
# 상점 물품 : 회복물약 50%, 회복물약 100%, 공격력 10%up, speed 10%up
#           10골드       17골드        30골드       30골드        30골드
# 공격시 공격 or 아이템사용(물약) or 도망가기(상점가기)
# 1 - 2층 : 리본돼지, 파란리본돼지, 와일드보어
# 3층 : 상점4 - 5층 : 주니어 예티,파이어드레이크,아이스드레이크/ 5층에서 전직 후 전투층 : 상점
# 7 - 8층 : 마뇽, 주니어발록, 발록
# 9층 : 상점
# 10층 : 페어리워터 박 ()
# 게임 시작 화면입니다. 이거는 나중에 main파일 만들어서 옮기는게 좋을 것 같아요!----------------
