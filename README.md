# Information
### 탐구 동기
기숙사를 한 학기 동안 지내보며 느낀 불편한 점이 있었다. 바로 공용 샤워실이다. 사용한느데는 문제가 없지만, 들어가기 전에 사용할 수 있는지 확인하기 위해 샤워실 문을 열어, 사람이 안에 있는지, 사용할 샤워 부스는 남아 있는지 확인이 필요했다. 이 문제를 해결해보고자, 정보시간에 배운 프로그래밍을 통해 해결해보고자 하였다.
### 진행과정
교과서 p.122에 있는 예제 18  

```py
a = [['놀이기구', '키제한', '탑승인원', '대기 시간(분)'],
    ['범퍼카', '110cm 이상', 30, 40],
    ['롤러코스터', '120cm 이상', 60, 100],
    ['플룸라이드', '140cm 이상', 8, 120]]
print(a)
print(a[1])
print(a[2][3])
```  

2차원 리스트를 이용하여 샤워실을 만든 뒤 값들을 넣어 만들면 될 것 같다는 생각에 아래와 같은 코드를 짜보았다.

```py
shower_rooms = [
    [0, "문", 0, 3, 0],
    [1, 0, 0, 0, 4],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 0, 5],
    [0, 0, "창문", 0, 0],
]
```
이렇게 보기 편하게 작성을 하고, 출력할 때에는

교과서 p.132 예제 28
```py
for i in range(2, 10) :
  for j in range(1, 10) :
    print(i, "*", "=", 1 * j)
```
위 코드와 같이 중첩for문을 이용하여 1,2,3,4,5 번 샤워 부스를 사용 가능함과 사용중을 표현하였다.
```py
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
```
그리고 상시 작동 가능해야하기에

교과서 p.133 하나 더 알기
```py
whlie True :
  print("!")
```
위 코드처럼 무한 반복을 이용하였다. 또한 

교과서 p.114 예제 12
```py
a = input()
print(a)
b = input("연도: ")
print(b)
```
교과서 예제12처럼 표준입출력을 이용해 샤워실에서 몇 번째 샤워 부스를 이용할 사용자인지, 이용한 사용자인지 확인하였다.
```py
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

```
used1~5 변수를 이용하여 사용 중인 샤워 부스를 사용하지 못하도록 하였다.

교과서 p.110 예제 5
```py
a = 10
b, c = 2.5, "A"
print(a, b, c)
a = a * 2
print(a, b, c)
```
가장 핵심적으로 다중 조건문을 이용하여 프로그램 종료, 시작, 샤워 부스 사용 여부를 결정하였다.
교과서 p.128 예제 22
```py
n = int(input())
if n >= 80 :
  print("A")
elif n >= 60 :
  print("B")
else :
  print("C")
```
그리고 교과서에 알려져있지 않지만 출력 메시지에 색을 입혀 더 잘 읽히도록 했다.
```py
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
```

### 느낀점
프로그래밍을 배워서 어디에 이용할 수 있을지 잘 와닿지 않았다. 하지만, 이렇게 실생활에서 적용시켜보니, 프로그래밍에 대해 더 잘 이해함과 동시에 어느 분야에서 이용될 수 있는지 잘 알게 되었다. 생각보다 코드를 만드는게 어려워서 여러 자료들을 찾아보며, 만드니 힘들었지만, 재미있었고, 다 완성하니 뿌듯했다. 코드 중,
```py
shower_rooms = [
    [0, "문", 0, 3, 0],
    [1, 0, 0, 0, 4],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 0, 5],
    [0, 0, "창문", 0, 0],
]
```
이런 코드가 있었는데, 1,2,3,4,5로 표현한 것까지 좋았지만, 완전히 잘 사용하지 못해 아쉬웠다. 만들다보니 터미널말고 .exe파일로 만들고 싶어서 찾아보던 중, tkinter라는 라이브러리를 알게되었는데, 어렵고 아직 배우지않은 부분이라, 이 부분을 배워, 다음에는 이 라이브러리를 활용하여 UI를 이용한 예약 프로그램을 만들고 싶다.

최종코드
```py
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

```
