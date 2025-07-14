# ANSI 색상 코드 정의
RESET = "\033[0m"       # 모든 속성 초기화
BLACK = "\033[30m"      # 검정
RED = "\033[31m"        # 빨강
GREEN = "\033[32m"      # 초록
YELLOW = "\033[33m"     # 노랑
BLUE = "\033[34m"       # 파랑
MAGENTA = "\033[35m"    # 마젠타 (자홍색)
CYAN = "\033[36m"       # 시안 (청록색)
WHITE = "\033[37m"      # 흰색

BRIGHT_RED = "\033[91m" # 밝은 빨강 (더 진한 색상)
BRIGHT_GREEN = "\033[92m"

used1, used2, used3, used4, used5 = "no", "no", "no", "no", "no"

shower_rooms = [
    [0, "문", 0, 3, 0],
    [1, 0, 0, 0, 4],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 0, 5],
    [0, 0, "창문", 0, 0],
]

print("샤워실 배치도:")
for row in shower_rooms:
    for i in range(len(row)):
        if row[i] == 0:
            row[i] = " " * 10
        elif row[i] == 1:
            row[i] = "1번 샤워 부스 (사용 가능)"
        elif row[i] == 2:
            row[i] = "2번 샤워 부스 (사용 가능)"
        elif row[i] == 3:
            row[i] = "3번 샤워 부스 (사용 가능)"
        elif row[i] == 4:
            row[i] = "4번 샤워 부스 (사용 가능)"
        elif row[i] == 5:
            row[i] = "5번 샤워 부스 (사용 가능)"
    print(row)

while True:
    answer = input("샤워실을 사용하시겠습니까? (y/n): ")
    if answer == "y":
        print("샤워실을 사용합니다.")
        num = int(input("몇 번째 샤워 부스를 사용하시겠습니까? (1-5): "))
        if 1 <= num <= 5:
            if num == 1 and used1 == "no":
                shower_rooms[1][0] = f"{num}번 샤워 부스 (사용 중)"  # 사용 중으로 변경
                print(f"{RED}{num}번 샤워 부스를 사용 중으로 변경했습니다.{RESET}")
                used1 = "yes"
            elif num == 2 and used2 == "no":
                shower_rooms[3][0] = f"{num}번 샤워 부스 (사용 중)"  # 사용 중으로 변경
                print(f"{RED}{num}번 샤워 부스를 사용 중으로 변경했습니다.{RESET}")
                used2 = "yes"
            elif num == 3 and used3 == "no":
                shower_rooms[0][3] = f"{num}번 샤워 부스 (사용 중)"  # 사용 중으로 변경
                print(f"{RED}{num}번 샤워 부스를 사용 중으로 변경했습니다.{RESET}")
                used3 = "yes"
            elif num == 4 and used4 == "no":
                shower_rooms[1][4] = f"{num}번 샤워 부스 (사용 중)"  # 사용 중으로 변경
                print(f"{RED}{num}번 샤워 부스를 사용 중으로 변경했습니다.{RESET}")
                used4 = "yes"
            elif num == 5 and used5 == "no":
                shower_rooms[3][4] = f"{num}번 샤워 부스 (사용 중)"  # 사용 중으로 변경
                print(f"{RED}{num}번 샤워 부스를 사용 중으로 변경했습니다.{RESET}")
                used5 = "yes"
            else:
                print(f"{RED}이미 사용 중인 샤워 부스입니다. 다른 부스를 선택해주십시오.{RESET}")
                continue
        elif num < 1 or num > 5:
            print("잘못된 번호입니다. 1에서 5 사이의 번호를 입력하세요.")
            continue
    elif answer == "n":
        print("몇 번째 샤워 부스를 이용하셨나요? (1-5): ")
        num = int(input())
        if 1 <= num <= 5:
            if num == 1:
                used1 = "no"
                shower_rooms[1][0] = f"{num}번 샤워 부스 (사용 가능)"  # 사용 가능으로 변경
            elif num == 2:
                used2 = "no"
                shower_rooms[3][0] = f"{num}번 샤워 부스 (사용 가능)"  # 사용 가능으로 변경
            elif num == 3:
                used3 = "no"
                shower_rooms[0][3] = f"{num}번 샤워 부스 (사용 가능)"  # 사용 가능으로 변경
            elif num == 4:
                used4 = "no"
                shower_rooms[1][4] = f"{num}번 샤워 부스 (사용 가능)"  # 사용 가능으로 변경
            elif num == 5:
                used5 = "no"
                shower_rooms[3][4] = f"{num}번 샤워 부스 (사용 가능)"  # 사용 가능으로 변경
        else:
            print("잘못된 입력입니다. y 또는 n을 입력하세요.")
            continue
        print(f"{GREEN}{num}번 샤워 부스를 비어있음으로 변경했습니다.{RESET}")

    elif answer == "break":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. y 또는 n을 입력하세요.")
        continue

    print("현재 샤워실 상태:")
    for row in shower_rooms:
        print(row)