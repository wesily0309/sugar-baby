from tkinter import*
from playsound import playsound
import pytube as pt
cli=0
def plus1():
    global cli
    cli=cli+1
    btn.config(text=str(cli))

    

win=Tk()#建立視窗
yrbtntxt=StringVar()
cli=0



win.title("pop sugar baby click")
win.geometry('800x400')#視窗必須和圖片等大
win.iconbitmap("aon1z-apggf-001.ico")
#按鈕圖片
cli=0
img=PhotoImage("301768731_1764248177260064_5431784438926177699_n.jpg")#插入圖片 (揚聲)
#標籤   
lb=Label(win,text="揚聲製作")
lb.pack()       
#按鈕
btn=Button(win,text='0')
btn.config(command=plus1)
btn.config(width=10,height=5)
#插入圖片預留空位
btn.pack()
#常駐視窗(所有視窗內物件須放在LOOP以上___)
win.mainloop()

#textvariable=yrbtntxt--24