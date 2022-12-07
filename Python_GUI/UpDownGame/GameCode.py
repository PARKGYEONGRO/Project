# import로 random 모듈 불러오기
import random as rd

# 변수 Random_number에 randint()함수를 사용해서 1이상 100이하의 정수를 랜덤으로 할당해주기
Random_number = rd.randint(1,100)

# 사용자의 입력을 간단하게 받을 수 있게 start() 함수를 정의해줌
def start():
    # 함수 안의 n1변수는 지역 변수라서 전역 변수로 사용할 수 있게 global 키워드 사용
    global n1
    # 사용자의 입력을 받아 정수로 변환하여 n1 변수에 할당한다.
    n1 = int(input('1이상 100이하의 숫자를 입력하세요: '))

# 정의해준 start() 함수 실행
start()    

# n1 변수에 할당된 값이 정수가 아니면 반복 X
while n1 != int:
    if Random_number == n1:
        print('정답입니다!')
        # 정답이면 while문 탈출
        break
    
    # 정답이 아니라면 n1과 Random_number의 값을 비교하여 UP인지 DOWN인지 출력해준후 다시 입력받기
    
    
    # 범위를 정확하게 지정해줘야함
    
    # 범위 잘못 지정 예
    # random_number가 10이고 n1이 -1 이라면
    # 우리의 의도는 범위 외 숫자면 사용자에게 다시 입력을 요청해야하는데
    # 코드 상으로 elif 문에 해당되어 의도를 벗어나게됨
    # elif random_number > n1:
    # else:
    
    elif Random_number > n1 > 0:
        print('UP')
        start()
    elif Random_number < n1 < 101:
        print('DOWN')
        start()
    else:
        print('범위 밖 숫자 | 다시 입력해주세요.')
        start()