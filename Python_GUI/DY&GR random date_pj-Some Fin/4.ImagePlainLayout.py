import tkinter.ttk as tk
import tkinter.messagebox as msgbox
from tkinter import *
import tkinter
import random


main = Tk()
main.geometry("300x400+100+100")
main.title("DY&GR Random Date")
main.resizable(False, False)

date_place = []
special_date_place = []
food_type = []
do_list = []

explainPhoto = PhotoImage(file='DY&GR random date_pj-Some Fin\\.img\\explain.png')
startPhoto = PhotoImage(file='DY&GR random date_pj-Some Fin\\.img\\start.png')
setingPhoto = PhotoImage(file='DY&GR random date_pj-Some Fin\\.img\\Seting.png')
closePhoto = PhotoImage(file='DY&GR random date_pj-Some Fin\\.img\\close.png')


def explain(): # 설명 버튼 커맨드
    global explain_info
    explain_info = msgbox.showinfo("DY&GR Random Date 설명", "세팅 창에서 각 리스트를\n입력하고 원하시는 뽑기를 선택해주세요.")


def listseting1(): # 세팅 창
    listseting = tkinter.Toplevel(main)
    listseting.title("리스트 세팅")
    listseting.geometry("300x400+100+100")
    listseting.resizable(False, False)
    
    
    def insert_btn1():  
        global date_place
        date_place = insert1_txt.get("1.0", END).split()
        if len(date_place) == 7:
            seting1_complete['text'] = "세팅 O"
            seting1_complete['fg'] = "#6aa2ff"
        else:
            seting1_complete['text'] = "세팅 X"
            seting1_complete['fg'] = "#fb7e7e"        
        insert1_txt.delete("1.0", END)
        print(date_place)
    
    def insert_btn2():
        global special_date_place
        special_date_place = insert2_txt.get("1.0", END).split()
        if len(special_date_place) == 3:
            seting2_complete['text'] = "세팅 O"
            seting2_complete['fg'] = "#6aa2ff"
        else:
            seting2_complete['text'] = "세팅 X"
            seting2_complete['fg'] = "#fb7e7e"
        insert2_txt.delete("1.0", END)
        print(special_date_place)
    
    def insert_btn3():
        global food_type
        food_type = insert3_txt.get("1.0", END).split()
        if len(food_type) == 10:
            seting3_complete['text'] = "세팅 O"
            seting3_complete['fg'] = "#6aa2ff"
        else:
            seting3_complete['text'] = "세팅 X"
            seting3_complete['fg'] = "#fb7e7e"
        insert3_txt.delete("1.0", END)
        print(food_type)
    
    def insert_btn4():
        global do_list
        do_list = insert4_txt.get("1.0", END).split()
        if len(do_list) == 8:
            seting4_complete['text'] = "세팅 O"
            seting4_complete['fg'] = "#6aa2ff"
        else:
            seting4_complete['text'] = "세팅 X"
            seting4_complete['fg'] = "#fb7e7e"
        insert4_txt.delete("1.0", END)
        print(do_list)
    
    
     # 세팅 프레임
    listseting_frame = Frame(listseting, relief="solid", bg="#e5e7e9")
    listseting["bg"] = "#e5e7e9"
    listseting_frame.grid(row=0,column=0)
    
    
     # 랜덤 숫자 때문에 제한둠 (장소 갯수 바꿀려면 랜덤 숫자와 연동해서 바꿔줘야함)
    seting1_frame = LabelFrame(listseting_frame, text="선택: 평범한 데이트 장소 7곳", bg="#e5e7e9", fg="black") 
    seting1_frame.grid(row=0,column=0,sticky=N+E+W+S, pady=7)
    seting1_complete = Label(seting1_frame, text="세팅 전", bg="#e5e7e9", fg='green')
    seting1_complete.grid(row=1, column=0) 
    insert1_txt = Text(seting1_frame, width=25, height=1) # seting()_frame 텍스트아레아
    insert1_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert1 = Button(seting1_frame, text="입력", relief='flat', width=7, bg="#a5ff9c",fg="black", command=insert_btn1)
    btn_insert1.grid(row=1,column=2) 
    
    
    seting2_frame = LabelFrame(listseting_frame, text="선택: 특별한 데이트 장소 3곳", bg="#e5e7e9", fg="black")
    seting2_frame.grid(row=2,column=0,sticky=N+E+W+S, pady=7)
    seting2_complete = Label(seting2_frame, text="세팅 전", bg="#e5e7e9", fg='green')
    seting2_complete.grid(row=1, column=0)   
    insert2_txt = Text(seting2_frame, width=25, height=1) # seting()_frame 텍스트아레아
    insert2_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert2 = Button(seting2_frame, text="입력", relief='flat', width=7, bg="#a5ff9c",fg="black", command=insert_btn2)
    btn_insert2.grid(row=1,column=2) 
    
    
    seting3_frame = LabelFrame(listseting_frame, text="필수: 음식 종류 총 10개", bg="#e5e7e9", fg="black")
    seting3_frame.grid(row=4,column=0,sticky=N+E+W+S, pady=7)
    seting3_complete = Label(seting3_frame, text="세팅 전", bg="#e5e7e9", fg='green')
    seting3_complete.grid(row=1, column=0) 
    insert3_txt = Text(seting3_frame, width=25, height=1) # seting()_frame 텍스트아레아
    insert3_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert3 = Button(seting3_frame, text="입력", relief='flat', width=7, bg="#a5ff9c",fg="black", command=insert_btn3)
    btn_insert3.grid(row=1,column=2) 
    
    
    seting4_frame = LabelFrame(listseting_frame, text="필수: Do 리스트 총 8개", bg="#e5e7e9", fg="black")
    seting4_frame.grid(row=6,column=0,sticky=N+E+W+S, pady=7)
    seting4_complete = Label(seting4_frame, text="세팅 전", bg="#e5e7e9", fg='green')
    seting4_complete.grid(row=1, column=0) 
    insert4_txt = Text(seting4_frame, width=25, height=1) # seting()_frame 텍스트아레아
    insert4_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert4 = Button(seting4_frame, text="입력", relief='flat', width=7, bg="#a5ff9c",fg="black", command=insert_btn4)
    btn_insert4.grid(row=1,column=2) 
    
    
    listseting.mainloop()

def start1(): # 시작 버튼 커맨드
    selecting = tkinter.Toplevel(main)
    selecting.geometry("300x400+100+100")
    selecting.title("Random Date selecting")
    selecting.resizable(False, False)


    def selecting1(): # 평범한 데이트 뽑기 창
        select1 = tkinter.Toplevel(selecting)
        select1.geometry("300x200+100+100")
        select1.title("평범한 데이트 뽑기")
        select1.resizable(False, False)

        global date_place
        global special_date_place
        global food_type
        global do_list


        select1_frame = Frame(select1, relief="solid", bg="#e5e7e9")
        select1["bg"] = "#e5e7e9"
        select1_frame.pack(expand=True)


        # 텍스트 레이블
        select1label1 = Label(select1_frame, text="데이트 장소 번호: 0\n데이트 장소: 0", anchor="center", width=100, bg="#e5e7e9", fg="black")
        select1label1.pack()
        select1label2 = Label(select1_frame, text="음식종류 번호: 0\n음식 종류: 0", anchor="center", width=100, bg="#e5e7e9", fg="black")
        select1label2.pack()
        select1label3 = Label(select1_frame, text="Do 리스트 번호: 0\nDo: 0", anchor="center", width=100, bg="#e5e7e9", fg="black")
        select1label3.pack()


        place_number = random.randint(1,7) #1~7 사이의 장소 랜덤 숫자 지정
        if place_number == 1:
            select1label1['text'] = "데이트 장소 번호:" + str(place_number) + "\n데이트 장소:" + str(date_place[0])
        elif place_number == 2:
            select1label1['text'] = "데이트 장소 번호:" + str(place_number) + "\n데이트 장소:" + str(date_place[1])
        elif place_number == 3:
            select1label1['text'] = "데이트 장소 번호:" + str(place_number) + "\n데이트 장소:" + str(date_place[2])
        elif place_number == 4:
            select1label1['text'] = "데이트 장소 번호:" + str(place_number) + "\n데이트 장소:" + str(date_place[3])
        elif place_number == 5:
            select1label1['text'] = "데이트 장소 번호:" + str(place_number) + "\n데이트 장소:" + str(date_place[4])
        elif place_number == 6:
            select1label1['text'] = "데이트 장소 번호:" + str(place_number) + "\n데이트 장소:" + str(date_place[5])
        elif place_number == 7:
            select1label1['text'] = "데이트 장소 번호:" + str(place_number) + "\n데이트 장소:" + str(date_place[6])

        food_number = random.randint(1,10) #1~10 사이의 음식 랜덤 숫자 지정        
        if food_number == 1:
            select1label2['text'] = "음식종류 번호:" + str(food_number) + "\n음식 종류:" + str(food_type[0])
        elif food_number == 2:
            select1label2['text'] = "음식종류 번호:" + str(food_number) + "\n음식 종류:" + str(food_type[1])
        elif food_number == 3:
            select1label2['text'] = "음식종류 번호:" + str(food_number) + "\n음식 종류:" + str(food_type[2])
        elif food_number == 4:
            select1label2['text'] = "음식종류 번호:" + str(food_number) + "\n음식 종류:" + str(food_type[3])
        elif food_number == 5:
            select1label2['text'] = "음식종류 번호:" + str(food_number) + "\n음식 종류:" + str(food_type[4])
        elif food_number == 6:
            select1label2['text'] = "음식종류 번호:" + str(food_number) + "\n음식 종류:" + str(food_type[5])
        elif food_number == 7:
            select1label2['text'] = "음식종류 번호:" + str(food_number) + "\n음식 종류:" + str(food_type[6])
        elif food_number == 8:
            select1label2['text'] = "음식종류 번호:" + str(food_number) + "\n음식 종류:" + str(food_type[7])
        elif food_number == 9:
            select1label2['text'] = "음식종류 번호:" + str(food_number) + "\n음식 종류:" + str(food_type[8])
        elif food_number == 10:
            select1label2['text'] = "음식종류 번호:" + str(food_number) + "\n음식 종류:" + str(food_type[9])
            
        do_number = random.randint(1,8) #Do 리스트 뽑기
        if do_number == 1:
            select1label3['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[0])
        elif do_number == 2:
            select1label3['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[1])
        elif do_number == 3:
            select1label3['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[2])
        elif do_number == 4:
            select1label3['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[3])
        elif do_number == 5:
            select1label3['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[4])
        elif do_number == 6:
            select1label3['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[5])
        elif do_number == 7:
            select1label3['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[6])
        elif do_number == 8:
            select1label3['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[7])


        select1.mainloop()

    def selecting2():# 특별한 데이트 뽑기 창
        select2 = tkinter.Toplevel(selecting)
        select2.geometry("300x100+100+100")
        select2.title("특별한 데이트 뽑기")
        select2.resizable(False, False)


        global special_date_place


        select2_frame = Frame(select2, relief="solid", bg="#e5e7e9")
        select2["bg"] = "#e5e7e9"
        select2_frame.pack(expand=True)


        # 텍스트 레이블
        select2label1 = Label(select2_frame, text="특별한 데이트 장소 번호: 0\n특별한 데이트 장소: 0", anchor="center", width=100, bg="#e5e7e9", fg="black")
        select2label1.pack()


        special_date_number = random.randint(1,3)
        if special_date_number == 1:
            select2label1['text'] = "특별한 데이트 장소 번호:" + str(special_date_number) + "\n특별한 데이트 장소:" + str(special_date_place[0])
        elif special_date_number == 2:
            select2label1['text'] = "특별한 데이트 장소 번호:" + str(special_date_number) + "\n특별한 데이트 장소:" + str(special_date_place[1])
        elif special_date_number == 3:
            select2label1['text'] = "특별한 데이트 장소 번호:" + str(special_date_number) + "\n특별한 데이트 장소:" + str(special_date_place[2])
    
        select2.mainloop()

    def selecting3():# Only Do리스트 뽑기 창
        select3 = tkinter.Toplevel(selecting)
        select3.geometry("300x100+100+100")
        select3.title("Only Do리스트 뽑기")
        select3.resizable(False, False)

        global do_list


        select3_frame = Frame(select3, relief="solid", bg="#e5e7e9")
        select3["bg"] = "#e5e7e9"
        select3_frame.pack(expand=True)


        # 텍스트 레이블
        select3label1 = Label(select3_frame, text="Do 리스트 번호: 0\nDo: 0", anchor="center", width=100, bg="#e5e7e9", fg="black")
        select3label1.pack()


        do_number = random.randint(1,8)
        if do_number == 1:
            select3label1['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[0])
        elif do_number == 2:
            select3label1['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[1])
        elif do_number == 3:
            select3label1['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[2])
        elif do_number == 4:
            select3label1['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[3])
        elif do_number == 5:
            select3label1['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[4])
        elif do_number == 6:
            select3label1['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[5])
        elif do_number == 7:
            select3label1['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[6])
        elif do_number == 8:
            select3label1['text'] = "Do 리스트 번호:" + str(do_number) + "\nDo:" + str (do_list[7])


        select3.mainloop()

 
    # 뽑기 프레임
    selecting_frame = Frame(selecting, relief="solid", bg="#e5e7e9")
    selecting["bg"] = "#e5e7e9"
    selecting_frame.pack(expand=True)

    # 뽑기 버튼
    selecting1_btn = Button(selecting_frame, text="평범한 데이트 뽑기", relief='flat', bg="#a5ff9c", fg="black", command=selecting1)
    selecting1_btn.pack(ipadx=45, ipady=15, pady=25)

    selecting2_btn = Button(selecting_frame, text="특별한 데이트 뽑기", relief='flat', bg="#a5ff9c", fg="black", command=selecting2)
    selecting2_btn.pack(ipadx=45, ipady=15, pady=25)

    selecting3_btn = Button(selecting_frame, text="Only DO리스트 뽑기", relief='flat', bg="#a5ff9c", fg="black", command=selecting3)
    selecting3_btn.pack(ipadx=39, ipady=15, pady=25)


    selecting.mainloop()


def close1(): # 끝내기 버튼 커맨드
    close_answer = msgbox.askquestion("DY&GR Random Date", "프로그램을 종료하시겠습니까?")
    if close_answer == 'yes':
        main.destroy()


# 메인 프레임 세팅
main_frame = Frame(main, relief="solid", bg="#e5e7e9")
main["bg"] = "#e5e7e9"
main_frame.pack(expand=True)

explain_btn = Button(main_frame, image=explainPhoto, relief="flat", bg="#e5e7e9", command=explain)
explain_btn.pack(pady=18)

start_btn = Button(main_frame, image=startPhoto, relief="flat", bg="#e5e7e9", command=start1)
start_btn.pack(pady=18)

listseting_btn = Button(main_frame, image=setingPhoto, relief="flat", bg="#e5e7e9", command=listseting1)
listseting_btn.pack(pady=18)

close_btn = Button(main_frame, image=closePhoto, relief="flat", bg="#e5e7e9", command=close1)
close_btn.pack(pady=18)

main.mainloop()