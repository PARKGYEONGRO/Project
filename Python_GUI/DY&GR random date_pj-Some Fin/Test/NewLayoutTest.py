from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as msgbox
import random

main=Tk()
main.geometry('300x400')
main.configure(bg='#83cf7b')#12c4c0')
main.resizable(0,0)
main.title('DY&GR Random Date')


date_place = []
special_date_place = []
food_type = []
do_list = []

sf3=Frame(main,width=300,height=400,bg='#83cf7b')
sf3.place(x=0,y=0)

def home():
    f1.destroy()
    sf1.destroy()
    sf2.destroy()
    sf3.destroy()
    toggle_mainin()

def nomaldate():
    f1.destroy()
    global sf1
    global date_place
    global special_date_place
    global food_type
    global do_list

    sf1=Frame(main,width=300,height=400,bg='#83cf7b')
    sf1.place(x=0,y=0)

    select1_frame = Frame(sf1, relief="solid", bg="#83cf7b")
    select1_frame.pack(expand=True)

    select1label1 = Label(select1_frame, text="데이트 장소 번호: 0\n데이트 장소: 0", anchor="center", width=100, bg="#83cf7b", fg='gray17')
    select1label1.pack()
    select1label2 = Label(select1_frame, text="음식종류 번호: 0\n음식 종류: 0", anchor="center", width=100, bg="#83cf7b", fg='gray17')
    select1label2.pack()
    select1label3 = Label(select1_frame, text="Do 리스트 번호: 0\nDo: 0", anchor="center", width=100, bg="#83cf7b", fg='gray17')
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
    toggle_mainin()

def specialdate():
    f1.destroy()
    global sf2
    global special_date_place

    sf2=Frame(main,width=300,height=400,bg='#83cf7b')
    sf2.place(x=0,y=0)

    select2_frame = Frame(sf2, relief="solid", bg="#2f2f2f")
    select2_frame.pack(expand=True)


    # 텍스트 레이블
    select2label1 = Label(select2_frame, text="특별한 데이트 장소 번호: 0\n특별한 데이트 장소: 0", anchor="center", width=100, bg="#2f2f2f", fg="yellow")
    select2label1.pack()


    special_date_number = random.randint(1,3)
    if special_date_number == 1:
        select2label1['text'] = "특별한 데이트 장소 번호:" + str(special_date_number) + "\n특별한 데이트 장소:" + str(special_date_place[0])
    elif special_date_number == 2:
        select2label1['text'] = "특별한 데이트 장소 번호:" + str(special_date_number) + "\n특별한 데이트 장소:" + str(special_date_place[1])
    elif special_date_number == 3:
        select2label1['text'] = "특별한 데이트 장소 번호:" + str(special_date_number) + "\n특별한 데이트 장소:" + str(special_date_place[2])

def onlydolist():
    f1.destroy()
    global do_list
    global sf3
    sf3=Frame(main,width=300,height=400,bg='#83cf7b')
    sf3.place(x=0,y=0)


    select3_frame = Frame(sf3, relief="solid", bg="#2f2f2f")
    select3_frame.pack(expand=True)


    # 텍스트 레이블
    select3label1 = Label(select3_frame, text="Do 리스트 번호: 0\nDo: 0", anchor="center", width=100, bg="#2f2f2f", fg="yellow")
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

def close():
    closemsgbox = msgbox.askquestion("종료","종료하시겠습니까?")
    if closemsgbox == 'yes':
        quit()

def default_home():
    f2=Frame(main,width=900,height=455,bg='#83cf7b')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Home',fg='white',bg='#83cf7b')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
 

def listsetting():
    global listsetting_frame

    f1.destroy()
    def insert_btn1():  
        global date_place
        date_place = insert1_txt.get("1.0", END).split()
        if len(date_place) == 7:
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
        if len(special_date_place) == 3:
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
        if len(food_type) == 10:
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
        if len(do_list) == 8:
            setting4_complete['text'] = "세팅 O"
            setting4_complete['fg'] = "#6aa2ff"
        else:
            setting4_complete['text'] = "세팅 X"
            setting4_complete['fg'] = "#fb7e7e"
        insert4_txt.delete("1.0", END)
        print(do_list)
    
    
     # 세팅 프레임
    listsetting_frame = Frame(f1, relief="solid", bg="#83cf7b")
    listsetting_frame.grid(row=0,column=0)
    
    
     # 랜덤 숫자 때문에 제한둠 (장소 갯수 바꿀려면 랜덤 숫자와 연동해서 바꿔줘야함)
    setting1_frame = LabelFrame(listsetting_frame, text="선택: 평범한 데이트 장소 7곳", bg="#83cf7b", fg='black') 
    setting1_frame.grid(row=1,column=0,sticky=N+E+W+S, pady=24)
    setting1_complete = Label(setting1_frame, text="세팅 전", bg="#83cf7b", fg="yellow")
    setting1_complete.grid(row=1, column=0) 
    insert1_txt = Text(setting1_frame, width=25, height=1) # setting()_frame 텍스트아레아
    insert1_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert1 = Button(setting1_frame, text="입력", width=7, relief="flat", bg='#e5e7e9',fg='black', command=insert_btn1)
    btn_insert1.grid(row=1,column=2) 
    
    
    setting2_frame = LabelFrame(listsetting_frame, text="선택: 특별한 데이트 장소 3곳", bg="#83cf7b", fg='black')
    setting2_frame.grid(row=3,column=0,sticky=N+E+W+S, pady=2)
    setting2_complete = Label(setting2_frame, text="세팅 전", bg="#83cf7b", fg="yellow")
    setting2_complete.grid(row=1, column=0)   
    insert2_txt = Text(setting2_frame, width=25, height=1) # setting()_frame 텍스트아레아
    insert2_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert2 = Button(setting2_frame, text="입력", width=7, relief="flat", bg='#e5e7e9',fg='black', command=insert_btn2)
    btn_insert2.grid(row=1,column=2) 
    
    
    setting3_frame = LabelFrame(listsetting_frame, text="필수: 음식 종류 총 10개", bg="#83cf7b", fg='black')
    setting3_frame.grid(row=5,column=0,sticky=N+E+W+S, pady=2)
    setting3_complete = Label(setting3_frame, text="세팅 전", bg="#83cf7b", fg="yellow")
    setting3_complete.grid(row=1, column=0) 
    insert3_txt = Text(setting3_frame, width=25, height=1) # setting()_frame 텍스트아레아
    insert3_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert3 = Button(setting3_frame, text="입력", width=7, relief="flat", bg='#e5e7e9',fg='black', command=insert_btn3)
    btn_insert3.grid(row=1,column=2) 
    
    
    setting4_frame = LabelFrame(listsetting_frame, text="필수: Do 리스트 총 8개", bg="#83cf7b", fg='black')
    setting4_frame.grid(row=7,column=0,sticky=N+E+W+S, pady=2)
    setting4_complete = Label(setting4_frame, text="세팅 전", bg="#83cf7b", fg="yellow")
    setting4_complete.grid(row=1, column=0) 
    insert4_txt = Text(setting4_frame, width=25, height=1) # setting()_frame 텍스트아레아
    insert4_txt.grid(row=1,column=1, padx=5, pady=25) 
    btn_insert4 = Button(setting4_frame, text="입력", width=7, relief="flat", bg='#e5e7e9',fg='black', command=insert_btn4)
    btn_insert4.grid(row=1,column=2) 
    toggle_mainin()
   

def toggle_mainin():
    global f1
    f1=Frame(main,width=200,height=500,bg='#e4f9e0')
    f1.place(x=0,y=0)
    
    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= 'black'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= 'black'

        myButton1 = Button(f1,text=text,
                       width=28,
                       height=2,
                       fg='black',
                       border=0,
                       bg=fcolor,
                       activeforeground='black',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'HOME','#0f9d9a','#e4f9e0',home)
    bttn(0,117,'ListSetting','#0f9d9a','#e4f9e0',listsetting)
    bttn(0,154,'Nomal Date','#0f9d9a','#e4f9e0',nomaldate)
    bttn(0,191,'Special Date','#0f9d9a','#e4f9e0',specialdate)
    bttn(0,228,'Only DoList','#0f9d9a','#e4f9e0',onlydolist)
    bttn(0,265,'CLOSE','#0f9d9a','#e4f9e0',close)

    #
    def dele():
        f1.destroy()
        b2=Button(main,image=img1,
               command=toggle_mainin,
               border=0,
               bg='#83cf7b',
               activebackground='#83cf7b')
        b2.place(x=5,y=8)

    global img2
    img2 = ImageTk.PhotoImage(Image.open("Tkinter study\\ToggleMenu\\close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#e4f9e0',
           activebackground='#e4f9e0').place(x=5,y=10)
    

default_home()

img1 = ImageTk.PhotoImage(Image.open("Tkinter study\\ToggleMenu\\menu.png"))

global b2
b2=Button(main,image=img1,
       command=toggle_mainin,
       border=0,
       bg='#83cf7b',
       activebackground='#83cf7b')
b2.place(x=5,y=8)


def close():
    closemsgbox = msgbox.askquestion("종료","종료하시겠습니까?")
    if closemsgbox == 'yes':
        quit()

main.mainloop()