from tkinter import*
from playsound import playsound
import pytube as pt
cli=0
def host():
    #playsound("kczrq-0asex.mp3")
    cli=cli+1
    btn.config(text=str(cli))
    


#建立視窗
win=Tk()
win.title("代決定")
win.geometry('800x400')#視窗必須和圖片等大
win.iconbitmap("aon1z-apggf-001.ico")
#按鈕圖片
cli=0
img=PhotoImage()#插入圖片 
#標籤   
lb=Label(text="aaaaaaaaaaaa")
lb.pack()       #內容(未決定)
#按鈕
btn=Button(win,text='1')
btn.config(command=host)
btn.pack()
#常駐視窗(所有視窗內物件須放在LOOP以上___)
win.mainloop()