import tkinter.messagebox as msgbox
from tkinter import *
import random as rd
import tkinter

main = Tk()
main.geometry("300x400+100+100")
main.title("DY&GR Random Date")
main.resizable(False, False)

date_place = []
special_date_place = []
food_type = []
do_list = []

def explain(): # 설명 버튼 커맨드
    global explain_info
    explain_info = msgbox.showinfo("DY&GR Random Date 설명", "세팅 창에서 각 리스트를\n입력하고 원하시는 뽑기를 선택해주세요.\n필수 항목은 반드시 입력을 하셔야하고\n선택 항목은 둘 중 하나만 입력하시면 됩니다.")

def cls(): # 끝내기 버튼 커맨드
    close_answer = msgbox.askquestion("DY&GR Random Date", "프로그램을 종료하시겠습니까?")
    if close_answer == 'yes':
        main.destroy()

def listsetting1(): # 세팅 창
    listsetting =Toplevel(main)
    listsetting.title("리스트 세팅")
    listsetting.geometry("300x400+100+100")
    listsetting.resizable(False, False)
    
    
    def insert_btn1():  
        global date_place
        date_place = insert1_txt.get("1.0", END).split()
        if len(date_place) > 1:
            setting1_complete['text'] = "세팅 O"
            setting1_complete['fg'] = "#6aa2ff"
        else:
            setting1_complete['text'] = "세팅 X"
            setting1_complete['fg'] = "#fb7e7e"        
        insert1_txt.delete("1.0", END)
        print(date_place)
    
    def insert_btn2():
        global special_date_place
        special_date_place = insert2_txt.get("1.0", END).split()
        if len(special_date_place) > 1:
            setting2_complete['text'] = "세팅 O"
            setting2_complete['fg'] = "#6aa2ff"
        else:
            setting2_complete['text'] = "세팅 X"
            setting2_complete['fg'] = "#fb7e7e"
        insert2_txt.delete("1.0", END)
        print(special_date_place)
    
    def insert_btn3():
        global food_type
        food_type = insert3_txt.get("1.0", END).split()
        if len(food_type) > 1:
            setting3_complete['text'] = "세팅 O"
            setting3_complete['fg'] = "#6aa2ff"
        else:
            setting3_complete['text'] = "세팅 X"
            setting3_complete['fg'] = "#fb7e7e"
        insert3_txt.delete("1.0", END)
        print(food_type)
    
    def insert_btn4():
        global do_list
        do_list = insert4_txt.get("1.0", END).split()
        if len(do_list) > 1:
            setting4_complete['text'] = "세팅 O"
            setting4_complete['fg'] = "#6aa2ff"
        else:
            setting4_complete['text'] = "세팅 X"
            setting4_complete['fg'] = "#fb7e7e"
        insert4_txt.delete("1.0", END)
        print(do_list)
    
    
     # 세팅 프레임
    listsetting_frame = Frame(listsetting, relief="solid", bg="#2f2f2f")
    listsetting["bg"] = "#2f2f2f"
    listsetting_frame.grid(row=0,column=0)
    
    
    setting1_frame = LabelFrame(listsetting_frame, text="선택: 평범한 데이트 장소", bg="#2f2f2f", fg="white") 
    setting1_frame.grid(row=0,column=0,sticky=N+E+W+S, pady=7)
    setting1_complete = Label(setting1_frame, text="세팅 전", bg="#2f2f2f", fg="yellow")
    setting1_complete.grid(row=1, column=0) 
    insert1_txt = Text(setting1_frame, width=25, height=1) # setting()_frame 텍스트아레아
    insert1_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert1 = Button(setting1_frame, text="입력", width=7, bg="#acacac",fg="white", command=insert_btn1)
    btn_insert1.grid(row=1,column=2) 
    
    
    setting2_frame = LabelFrame(listsetting_frame, text="선택: 특별한 데이트 장소", bg="#2f2f2f", fg="white")
    setting2_frame.grid(row=2,column=0,sticky=N+E+W+S, pady=7)
    setting2_complete = Label(setting2_frame, text="세팅 전", bg="#2f2f2f", fg="yellow")
    setting2_complete.grid(row=1, column=0)   
    insert2_txt = Text(setting2_frame, width=25, height=1) # setting()_frame 텍스트아레아
    insert2_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert2 = Button(setting2_frame, text="입력", width=7, bg="#acacac",fg="white", command=insert_btn2)
    btn_insert2.grid(row=1,column=2) 
    
    
    setting3_frame = LabelFrame(listsetting_frame, text="필수: 음식 종류", bg="#2f2f2f", fg="white")
    setting3_frame.grid(row=4,column=0,sticky=N+E+W+S, pady=7)
    setting3_complete = Label(setting3_frame, text="세팅 전", bg="#2f2f2f", fg="yellow")
    setting3_complete.grid(row=1, column=0) 
    insert3_txt = Text(setting3_frame, width=25, height=1) # setting()_frame 텍스트아레아
    insert3_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert3 = Button(setting3_frame, text="입력", width=7, bg="#acacac",fg="white", command=insert_btn3)
    btn_insert3.grid(row=1,column=2) 
    
    
    setting4_frame = LabelFrame(listsetting_frame, text="필수: Do 리스트", bg="#2f2f2f", fg="white")
    setting4_frame.grid(row=6,column=0,sticky=N+E+W+S, pady=7)
    setting4_complete = Label(setting4_frame, text="세팅 전", bg="#2f2f2f", fg="yellow")
    setting4_complete.grid(row=1, column=0) 
    insert4_txt = Text(setting4_frame, width=25, height=1) # setting()_frame 텍스트아레아
    insert4_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert4 = Button(setting4_frame, text="입력", width=7, bg="#acacac",fg="white", command=insert_btn4)
    btn_insert4.grid(row=1,column=2) 
    
    
    listsetting.mainloop()

def strt(): # 시작 버튼 커맨드
    selecting = Toplevel(main)
    selecting.geometry("300x400+100+100")
    selecting.title("Random Date selecting")
    selecting.resizable(False, False)


    def selecting1(): # 평범한 데이트 뽑기 창
        select1 = Toplevel(selecting)
        select1.geometry("300x200+100+100")
        select1.title("평범한 데이트 뽑기")
        select1.resizable(False, False)

        global date_place
        global special_date_place
        global food_type
        global do_list


        select1_frame = Frame(select1, relief="solid", bg="#2f2f2f")
        select1["bg"] = "#2f2f2f"
        select1_frame.pack(expand=True)


        # 텍스트 레이블
        select1label1 = Label(select1_frame, text="데이트 장소: 0", anchor="center", width=100, bg="#2f2f2f", fg="yellow")
        select1label1.pack()
        select1label2 = Label(select1_frame, text="음식 종류: 0", anchor="center", width=100, bg="#2f2f2f", fg="yellow")
        select1label2.pack()
        select1label3 = Label(select1_frame, text="Do: 0", anchor="center", width=100, bg="#2f2f2f", fg="yellow")
        select1label3.pack()


        rd_place = rd.choice(date_place) #장소 랜덤 지정
        select1label1['text'] = "데이트 장소:" + str(rd_place)

        rd_food = rd.choice(food_type) #음식 랜덤 지정        
        select1label2['text'] = "음식 종류:" + str(rd_food)

        rd_do = rd.choice(do_list) #Do 리스트 뽑기
        select1label3['text'] = "Do:" + str (rd_do)

        select1.mainloop()

    def selecting2():# 특별한 데이트 뽑기 창
        select2 = Toplevel(selecting)
        select2.geometry("300x100+100+100")
        select2.title("특별한 데이트 뽑기")
        select2.resizable(False, False)


        global special_date_place


        select2_frame = Frame(select2, relief="solid", bg="#2f2f2f")
        select2["bg"] = "#2f2f2f"
        select2_frame.pack(expand=True)


        # 텍스트 레이블
        select2label1 = Label(select2_frame, text="특별한 데이트 장소: 0", anchor="center", width=100, bg="#2f2f2f", fg="yellow")
        select2label1.pack()


        rd_special_place = rd.choice(special_date_place)
        select2label1['text'] = "특별한 데이트 장소:" + str(rd_special_place)
    
        select2.mainloop()

    def selecting3():# Only Do리스트 뽑기 창
        select3 = Toplevel(selecting)
        select3.geometry("300x100+100+100")
        select3.title("Only Do리스트 뽑기")
        select3.resizable(False, False)

        global do_list


        select3_frame = Frame(select3, relief="solid", bg="#2f2f2f")
        select3["bg"] = "#2f2f2f"
        select3_frame.pack(expand=True)


        # 텍스트 레이블
        select3label1 = Label(select3_frame, text="Do 리스트 번호: 0\nDo: 0", anchor="center", width=100, bg="#2f2f2f", fg="yellow")
        select3label1.pack()


        rd_do = rd.choice(do_list)
        select3label1['text'] = "Do:" + str (rd_do)

        select3.mainloop()

 
    # 뽑기 프레임
    selecting_frame = Frame(selecting, relief="solid", bg="#2f2f2f")
    selecting["bg"] = "#2f2f2f"
    selecting_frame.pack(expand=True)

    # 뽑기 버튼
    selecting1_btn = Button(selecting_frame, text="평범한 데이트 뽑기", relief="flat", bg="#979797", fg="#efefef", command=selecting1)
    selecting1_btn.pack(ipadx=45, ipady=15, pady=25)

    selecting2_btn = Button(selecting_frame, text="특별한 데이트 뽑기", relief="flat", bg="#979797", fg="#efefef", command=selecting2)
    selecting2_btn.pack(ipadx=45, ipady=15, pady=25)

    selecting3_btn = Button(selecting_frame, text="Only DO리스트 뽑기", relief="flat", bg="#979797", fg="#efefef", command=selecting3)
    selecting3_btn.pack(ipadx=39, ipady=15, pady=25)


    selecting.mainloop()


# 메인 프레임 세팅
main_frame = Frame(main, relief="solid", bg="#2f2f2f")
main["bg"] = "#2f2f2f"
main_frame.pack(expand=True)

explain_btn = Button(main_frame, text="설명", relief="flat", bg="#979797", fg="#efefef", command=explain)
explain_btn.pack(ipadx=45, ipady=15, pady=20)

start_btn = Button(main_frame, text="시작", relief="flat", bg="#979797", fg="#efefef", command=strt)
start_btn.pack(ipadx=45, ipady=15, pady=20)

listsetting_btn = Button(main_frame, text="세팅", relief="flat", bg="#979797", fg="#efefef", command=listsetting1)
listsetting_btn.pack(ipadx=45, ipady=15, pady=20)

close_btn = Button(main_frame, text="끝내기", relief="flat", bg="#979797", fg="#efefef", command=cls)
close_btn.pack(ipadx=39, ipady=15, pady=20)

main.mainloop()