from datetime import date
import random


print("-"*20)
print("        Menu        ")
print("1번: 평범한 데이트 뽑기\n2번: 특별한 데이트 뽑기\n3번: Do 뽑기\n4번: 장소 리스트\n5번: 특별한 장소 리스트\n6번: 음식 종류 리스트\n7번: Do 리스트\nA: 평범한 데이트 장소 정하기\nB: 특별한 데이트 장소 정하기\nC: 음식 정류 정하기\nD: Do 정하기\n0번: 프로그램 종료")
print("-"*20)


while True:
    inputdata = input("번호를 입력하세요: ")


# 리스트 선언
    if inputdata == "A":
        date_place = list(input("7개의 장소 입력: ").split())
        print(date_place)

    elif inputdata == "B":
        special_date_place = list(input("3개의 장소 입력: ").split())
        print(special_date_place)

    elif inputdata == "C":
        food_type = list(input("10개의 음식 종류 입력: ").split())
        print(food_type)

    elif inputdata == "D":
        do_list = list(input("무엇을 할 지 8개 입력: ").split())
        print(do_list)



# 출력
    if inputdata == "1": #1번: 평범한 데이트 뽑기
        place_number = random.randint(1,7) #1~7 사이의 장소 랜덤 숫자 지정
        if place_number == 1:
            print("데이트 장소 번호: {}".format(place_number))
            print("데이트 장소: ",date_place[0])
        elif place_number == 2:
            print("데이트 장소 번호: {}".format(place_number))
            print("데이트 장소: ",date_place[1])
        elif place_number == 3:
            print("데이트 장소 번호: {}".format(place_number))
            print("데이트 장소: ",date_place[2])
        elif place_number == 4:
            print("데이트 장소 번호: {}".format(place_number))
            print("데이트 장소: ",date_place[3])
        elif place_number == 5:
            print("데이트 장소 번호: {}".format(place_number))
            print("데이트 장소: ",date_place[4])
        elif place_number == 6:
            print("데이트 장소 번호: {}".format(place_number))
            print("데이트 장소: ",date_place[5])
        elif place_number == 7:
            print("데이트 장소 번호: {}".format(place_number))
            print("데이트 장소: ",date_place[6])

        food_number = random.randint(1,10) #1~10 사이의 음식 랜덤 숫자 지정        
        if food_number == 1:
            print("음식 종류 번호: {}".format(food_number))
            print("음식 종류: ",food_type[0])
        elif food_number == 2:
            print("음식 종류 번호: {}".format(food_number))
            print("음식 종류: ",food_type[1])
        elif food_number == 3:
            print("음식 종류 번호: {}".format(food_number))
            print("음식 종류: ",food_type[2])
        elif food_number == 4:
            print("음식 종류 번호: {}".format(food_number))
            print("음식 종류: ",food_type[3])
        elif food_number == 5:
            print("음식 종류 번호: {}".format(food_number))
            print("음식 종류: ",food_type[4])
        elif food_number == 6:
            print("음식 종류 번호: {}".format(food_number))
            print("음식 종류: ",food_type[5])
        elif food_number == 7:
            print("음식 종류 번호: {}".format(food_number))
            print("음식 종류: ",food_type[6])
        elif food_number == 8:
            print("음식 종류 번호: {}".format(food_number))
            print("음식 종류: ",food_type[7])
        elif food_number == 9:
            print("음식 종류 번호: {}".format(food_number))
            print("음식 종류: ",food_type[8])
        elif food_number == 10:
            print("음식 종류 번호: {}".format(food_number))
            print("음식 종류: ",food_type[9])
            
        do_number = random.randint(1,8) #Do 리스트 뽑기
        if do_number == 1:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do: ",do_list[0])
        elif do_number == 2:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do: ",do_list[1])
        elif do_number == 3:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do: ",do_list[2])
        elif do_number == 4:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do: ",do_list[3])
        elif do_number == 5:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do: ",do_list[4])
        elif do_number == 6:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do: ",do_list[5])
        elif do_number == 7:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do: ",do_list[6])
        elif do_number == 8:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do: ",do_list[7])
        
        break

    elif inputdata == "2": #2번: 특별한 데이트 뽑기
        special_date_number = random.randint(1,3)
        if special_date_number == 1:
            print("특별한 데이트 번호: {}".format(special_date_number))
            print("특별한 데이트 장소:", special_date_place[0])
        elif special_date_number == 2:
            print("특별한 데이트 번호: {}".format(special_date_number))
            print("특별한 데이트 장소:", special_date_place[1])
        elif special_date_number == 3:
            print("특별한 데이트 번호: {}".format(special_date_number))
            print("특별한 데이트 장소:", special_date_place[2])

        break

    elif inputdata == "3": #3번: Do 리스트 뽑기
        do_number = random.randint(1,8)
        if do_number == 1:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do:",do_list[0])
        elif do_number == 2:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do:",do_list[1])
        elif do_number == 3:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do:",do_list[2])
        elif do_number == 4:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do:",do_list[3])
        elif do_number == 5:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do:",do_list[4])
        elif do_number == 6:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do:",do_list[5])
        elif do_number == 7:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do:",do_list[6])
        elif do_number == 8:
            print("Do 리스트 번호: {}".format(do_number))
            print("Do:",do_list[7])

        break



    elif inputdata == "4": #4번: 장소 리스트 공개
        print(date_place)

    elif inputdata == "5": #5번: 특별한 데이트 장소 리스트 공개
        print(special_date_place)

    elif inputdata == "6": #6번: 음식 종류 리스트 공개
        print(food_type)

    elif inputdata == "7": #7번: Do 리스트 공개
        print(do_list)


    elif inputdata == "0": #0번: 프로그램 종료
        print("프로그램을 종료합니다.")
        quit()


    else: #다른 번호를 입력하면 pass로 무시함.
        pass
