import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
import random


main = Tk()
main.geometry("300x400+100+100")
main.title("DY&GR Random Date")
main.resizable(False, False)


def explain(): # 설명 버튼 커맨드
    explain_info = msgbox.showinfo("DY&GR Random Date 설명", "세팅 창에서 각 리스트를\n입력하고 원하시는 뽑기를 선택해주세요.")

def close1(): # 끝내기 버튼 커맨드
    close_answer = msgbox.askquestion("DY&GR Random Date", "프로그램을 종료하시겠습니까?")
    if close_answer == 'yes':
        exit()

def start1(): # 시작 버튼 커맨드
    selecting = Tk()
    selecting.geometry("300x400+100+100")
    selecting.title("Random Date selecting")
    selecting.resizable(False, False)


    def selecting1(): # 평범한 데이트 뽑기 창
        select1 = Tk()
        select1.geometry("300x400+100+100")
        select1.title("평범한 데이트 뽑기")
        select1.resizable(False, False)


        select1_frame = Frame(select1, relief="solid", bg="#2f2f2f")
        select1["bg"] = "#2f2f2f"
        select1_frame.pack(expand=True)

        select1.mainloop()

    def selecting2():# 특별한 데이트 뽑기 창
        select2 = Tk()
        select2.geometry("300x400+100+100")
        select2.title("특별한 데이트 뽑기")
        select2.resizable(False, False)


        select2_frame = Frame(select2, relief="solid", bg="#2f2f2f")
        select2["bg"] = "#2f2f2f"
        select2_frame.pack(expand=True)
    
        select2.mainloop()

    def selecting3():# Only Do리스트 뽑기 창
        select3 = Tk()
        select3.geometry("300x400+100+100")
        select3.title("Only Do리스트 뽑기")
        select3.resizable(False, False)


        select3_frame = Frame(select3, relief="solid", bg="#2f2f2f")
        select3["bg"] = "#2f2f2f"
        select3_frame.pack(expand=True)

        select3.mainloop()

 
    # 뽑기 프레임
    selecting_frame = Frame(selecting, relief="solid", bg="#2f2f2f")
    selecting["bg"] = "#2f2f2f"
    selecting_frame.pack(expand=True)

    # 뽑기 버튼
    selecting1_btn = Button(selecting_frame, text="평범한 데이트 뽑기", relief="groove", bg="#979797", fg="#efefef", command=selecting1)
    selecting1_btn.pack(ipadx=45, ipady=15, pady=25)

    selecting2_btn = Button(selecting_frame, text="특별한 데이트 뽑기", relief="groove", bg="#979797", fg="#efefef", command=selecting2)
    selecting2_btn.pack(ipadx=45, ipady=15, pady=25)

    selecting3_btn = Button(selecting_frame, text="Only DO리스트 뽑기", relief="groove", bg="#979797", fg="#efefef", command=selecting3)
    selecting3_btn.pack(ipadx=39, ipady=15, pady=25)


    selecting.mainloop()


def listseting1(): # 세팅 창
    listseting = Tk()
    listseting.title("리스트 세팅")
    listseting.geometry("300x400+100+100")
    listseting.resizable(False, False)


    def insert_btn1():
        pass

    def insert_btn2():
        pass

    def insert_btn3():
        pass

    def insert_btn4():
        pass


    # 세팅 프레임
    listseting_frame = Frame(listseting, relief="solid", bg="#2f2f2f")
    listseting["bg"] = "#2f2f2f"
    listseting_frame.pack(expand=True)


    # 랜덤 숫자 때문에 제한둠 (장소 갯수 바꿀려면 랜덤 숫자와 연동해서 바꿔줘야함)
    seting1_frame = LabelFrame(listseting_frame, text="선택: 평범한 데이트 장소 7곳", bg="#2f2f2f", fg="white") 
    seting1_frame.pack(ipadx=30, ipady=15, padx=15, pady=10)
    insert1_txt = Text(seting1_frame, padx=5, width=25, height=1) # seting()_frame 텍스트아레아
    insert1_txt.pack(side="left")
    btn_insert1 = Button(seting1_frame, text="입력", width=8, command=insert_btn1)
    btn_insert1.pack(side="right")

    seting2_frame = LabelFrame(listseting_frame, text="선택: 특별한 데이트 장소 3곳", bg="#2f2f2f", fg="white")
    seting2_frame.pack(ipadx=30, ipady=15, padx=15, pady=10)
    insert2_txt = Text(seting2_frame, padx=5, width=25, height=1) # seting()_frame 텍스트아레아
    insert2_txt.pack(side="left")
    btn_insert2 = Button(seting2_frame, text="입력", width=8, command=insert_btn2)
    btn_insert2.pack(side="right")

    seting3_frame = LabelFrame(listseting_frame, text="필수: 음식 종류 총 10개", bg="#2f2f2f", fg="white")
    seting3_frame.pack(ipadx=30, ipady=15, padx=15, pady=10)
    insert3_txt = Text(seting3_frame, padx=5, width=25, height=1) # seting()_frame 텍스트아레아
    insert3_txt.pack(side="left")
    btn_insert3 = Button(seting3_frame, text="입력", width=8, command=insert_btn3)
    btn_insert3.pack(side="right")

    seting4_frame = LabelFrame(listseting_frame, text="필수: Do 리스트 총 8개", bg="#2f2f2f", fg="white")
    seting4_frame.pack(ipadx=30, ipady=15, padx=15, pady=10)
    insert4_txt = Text(seting4_frame, padx=5, width=25, height=1) # seting()_frame 텍스트아레아
    insert4_txt.pack(side="left")
    btn_insert4 = Button(seting4_frame, text="입력", width=8, command=insert_btn4)
    btn_insert4.pack(side="right")



    listseting.mainloop()



# 메인 프레임 세팅
main_frame = Frame(main, relief="solid", bg="#2f2f2f")
main["bg"] = "#2f2f2f"
main_frame.pack(expand=True)

explain_btn = Button(main_frame, text="설명", relief="groove", bg="#979797", fg="#efefef", command=explain)
explain_btn.pack(ipadx=45, ipady=15, pady=20)

start_btn = Button(main_frame, text="시작", relief="groove", bg="#979797", fg="#efefef", command=start1)
start_btn.pack(ipadx=45, ipady=15, pady=20)

listseting_btn = Button(main_frame, text="세팅", relief="groove", bg="#979797", fg="#efefef", command=listseting1)
listseting_btn.pack(ipadx=45, ipady=15, pady=20)

close_btn = Button(main_frame, text="끝내기", relief="groove", bg="#979797", fg="#efefef", command=close1)
close_btn.pack(ipadx=39, ipady=15, pady=20)

main.mainloop()