import tkinter.ttk as tk
import tkinter.messagebox as msgbox
from tkinter import *


listseting = Tk()
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
listseting_frame = Frame(listseting, relief="solid", bg="#2f2f2f")
listseting["bg"] = "#2f2f2f"
listseting_frame.grid(row=0,column=0)


 # 랜덤 숫자 때문에 제한둠 (장소 갯수 바꿀려면 랜덤 숫자와 연동해서 바꿔줘야함)
seting1_frame = LabelFrame(listseting_frame, text="선택: 평범한 데이트 장소 7곳", bg="#2f2f2f", fg="white") 
seting1_frame.grid(row=0,column=0,sticky=N+E+W+S, pady=7)
seting1_complete = Label(seting1_frame, text="세팅 전", bg="#2f2f2f", fg="yellow")
seting1_complete.grid(row=1, column=0) 
insert1_txt = Text(seting1_frame, width=25, height=1) # seting()_frame 텍스트아레아
insert1_txt.grid(row=1,column=1, padx=5, pady=25) 
btn_insert1 = Button(seting1_frame, text="입력", width=7, bg="#acacac",fg="white", command=insert_btn1)
btn_insert1.grid(row=1,column=2) 


seting2_frame = LabelFrame(listseting_frame, text="선택: 특별한 데이트 장소 3곳", bg="#2f2f2f", fg="white")
seting2_frame.grid(row=2,column=0,sticky=N+E+W+S, pady=7)
seting2_complete = Label(seting2_frame, text="세팅 전", bg="#2f2f2f", fg="yellow")
seting2_complete.grid(row=1, column=0)   
insert2_txt = Text(seting2_frame, width=25, height=1) # seting()_frame 텍스트아레아
insert2_txt.grid(row=1,column=1, padx=5, pady=25) 
btn_insert2 = Button(seting2_frame, text="입력", width=7, bg="#acacac",fg="white", command=insert_btn2)
btn_insert2.grid(row=1,column=2) 


seting3_frame = LabelFrame(listseting_frame, text="필수: 음식 종류 총 10개", bg="#2f2f2f", fg="white")
seting3_frame.grid(row=4,column=0,sticky=N+E+W+S, pady=7)
seting3_complete = Label(seting3_frame, text="세팅 전", bg="#2f2f2f", fg="yellow")
seting3_complete.grid(row=1, column=0) 
insert3_txt = Text(seting3_frame, width=25, height=1) # seting()_frame 텍스트아레아
insert3_txt.grid(row=1,column=1, padx=5, pady=25) 
btn_insert3 = Button(seting3_frame, text="입력", width=7, bg="#acacac",fg="white", command=insert_btn3)
btn_insert3.grid(row=1,column=2) 


seting4_frame = LabelFrame(listseting_frame, text="필수: Do 리스트 총 8개", bg="#2f2f2f", fg="white")
seting4_frame.grid(row=6,column=0,sticky=N+E+W+S, pady=7)
seting4_complete = Label(seting4_frame, text="세팅 전", bg="#2f2f2f", fg="yellow")
seting4_complete.grid(row=1, column=0) 
insert4_txt = Text(seting4_frame, width=25, height=1) # seting()_frame 텍스트아레아
insert4_txt.grid(row=1,column=1, padx=5, pady=25) 
btn_insert4 = Button(seting4_frame, text="입력", width=7, bg="#acacac",fg="white", command=insert_btn4)
btn_insert4.grid(row=1,column=2) 


listseting.mainloop()