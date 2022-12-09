from tkinter import *
import random as rd

# 메시지창 뛰우기 위해서 불러옴
import tkinter.messagebox as msgbox

# 프로그램 메인 화면
main = Tk()
main.title("Up Down Game")
main.resizable(False, False) # 창 크기 고정
main.geometry("280x350")


# 설명창
def explain():
    msgbox.showinfo("Up Down GAME", "시작 버튼을 눌러 1 ~ 100 까지의 랜덤 숫자중 하나를 맞추세요.")


# 메인 닫기 버튼
def btn_exit1():
    exit_btn_answer1 = msgbox.askquestion('Up Down Game','게임을 종료하시겠습니까?')
    if exit_btn_answer1 == 'yes':
        main.destroy()


# 시작 버튼
def start():
    # main의 하위 창
    startgame = Toplevel(main)
    startgame.title("Game Start")
    startgame.resizable(False, False)
    startgame.geometry("250x300")


    # 전역변수 처리
    global random_number
    global count
    random_number = rd.randint(1,100) # 1 ~ 100 숫자 랜덤 출력
    count = 0 # 몇번 시도 했는지 Counting

    
    # 게임창 닫기 버튼
    def btn_exit2():
        exit_btn_answer2 = msgbox.askquestion('Game Start','게임창을 닫으시겠습니까?')
        if exit_btn_answer2 == 'yes':
            startgame.destroy()


    # 입력 버튼 누르면 실행
    def gamestart():
        
        # 전역변수 처리
        # 이 함수 내에서 count=0를 한다면 입력 버튼 누를 때 마다 count가 0으로 초기화 되어버림.
        global count

        
        while len(insert_txt.get()) != 0:
            inputdata = int(insert_txt.get())
            if 101 > inputdata > random_number:
                count += 1
                game_txt1['text'] = "게임 진행중"
                game_txt2['text'] = str(inputdata) + " 입력 받았습니다."
                game_txt3['text'] = str(count) + " 번째 도전중"   
                game_txt4['text'] = "Down !"
                insert_txt.delete(0, END)

            elif inputdata < random_number:
                count += 1
                game_txt1['text'] = "게임 진행중"
                game_txt2['text'] = str(inputdata) + " 입력 받았습니다."
                game_txt3['text'] = str(count) + " 번째 도전중"           
                game_txt4['text'] = "Up !"
                insert_txt.delete(0, END)

            elif inputdata == random_number:
                count += 1
                game_txt1['text'] = "게임 종료"            
                game_txt2['text'] = str(inputdata) + " 입력 받았습니다."
                game_txt3['text'] = str(count) + " 번째 도전"
                game_txt4['text'] = "정답입니다!"
                insert_txt.delete(0, END)
                break

            elif 100 < inputdata or inputdata < 0:
                msgbox.showerror('Game Start','다시 입력해주세요.\n입력값이 범위를 벗어났습니다.')
                insert_txt.delete(0, END)
                break
                
    # Enter키를 누르면 gamestart() 함수를 실행시키는 함수를 따로 정의, Enter키는 event이기 때문
    def Enterstart(event):
        gamestart()

    # 게임 프레임
    game_frame = Frame(startgame)
    game_frame.pack(fill="both")


    # Log 텍스트 기본 세팅
    gametxt_frame = LabelFrame(game_frame, text="Log")
    gametxt_frame.pack(padx=10, pady=20)

    game_txt1 = Label(gametxt_frame, text="랜덤 번호가 출력되었습니다.", anchor="center", width = 100, fg="blue")
    game_txt1.pack()

    game_txt2 = Label(gametxt_frame, text="숫자를 입력해주세요.", width=100, height=2, fg="blue")
    game_txt2.pack()

    game_txt3 = Label(gametxt_frame, text="0 번째 도전중", width=100, height=2, fg="blue")
    game_txt3.pack()

    game_txt4 = Label(gametxt_frame, text="Up or Down", width=100, height=2, fg="red")
    game_txt4.pack()


    # 입력 프레임
    insert_frame = LabelFrame(game_frame, text="입력")
    insert_frame.pack(padx=10, pady=20,ipadx=10,ipady=10)

    insert_txt = Entry(insert_frame, width=15)
    insert_txt.pack(side="left")

    exit_btn2 = Button(insert_frame, width=5, text="닫기", command=btn_exit2)
    exit_btn2.pack(side='right', padx=10)

    btn_insert = Button(insert_frame, text="입력", width=5, command=gamestart)
    btn_insert.pack(side="right")
    insert_txt.bind('<Return>',Enterstart) # 헷갈리지 않게 이곳에 코드 작성



    startgame.mainloop()



# 메인 프레임
main_frame = Frame(main)
main_frame.pack(fill="both")


# 메인 기능 버튼
explain_btn = Button(main_frame, width=15, text="설명", command=explain)
explain_btn.pack(ipady=15,padx=80, pady=25)
start_btn = Button(main_frame, width=15, text="시작", command=start)
start_btn.pack(ipady=15,padx=80, pady=25)
exit_btn1 = Button(main_frame, width=15, text="닫기", command=btn_exit1)
exit_btn1.pack(ipady=15,padx=80, pady=25)


main.mainloop()