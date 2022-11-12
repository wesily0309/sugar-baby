from tkinter import*
from playsound import playsound
import pytube as pt
cli=0
def plus1():
    global cli
    cli=cli+1
    btn.config(text=str(cli))#改變btn物件中的text
    #設定替換圖片
'''
def sw():
    if (cli%2)==0:
        img=PhotoImage(file="301768731_1764248177260064_5431784438926177699_n.png")
    
    if (cli%2)!=0:
        img=PhotoImage(file="301768731_1764248177260064_5431784438926177699_n2.png")
'''


    


    
win=Tk()#建立視窗
yrbtntxt=StringVar()
cli=0



win.title("pop sugar baby click")
win.geometry('800x400')#視窗必須和圖片等大
win.iconbitmap("aon1z-apggf-001.ico")
#按鈕圖片
cli=0
#img=PhotoImage(file="301768731_1764248177260064_5431784438926177699_n.png")#插入圖片 (揚聲)
if (cli%2)==0:
    img=PhotoImage(file="301768731_1764248177260064_5431784438926177699_n.png")
elif(cli%2)==1:
    img=PhotoImage(file="301768731_1764248177260064_5431784438926177699_n2.png")


#標籤   
lb=Label(win,text="???")
lb.pack()       
#lb.place(x=40, y=50)
#按鈕
btn=Button(win,text='0',compound='top',font =('Arial',20))#font=(字形,大小)
btn.config(padx=0,pady=0)
btn.config(command=plus1)
#btn.config(sticky="center")          #sticky= anchor= anchor="center"
btn.config(image=img)#插入圖片
btn.pack()
#常駐視窗(所有視窗內物件須放在LOOP以上___)
win.mainloop()

#textvariable=yrbtntxt--24
'''''
if (cli%2)==0:
    img=PhotoImage(file="301768731_1764248177260064_5431784438926177699_n.png")
else:
    img=PhotoImage(file="301768731_1764248177260064_5431784438926177699_n2.png")

btn.config(image=img)
'''''



'''
if (cli%2)==0:
    img=PhotoImage(file="301768731_1764248177260064_5431784438926177699_n.png")
    btn.config(image=img)
else:
    img2=PhotoImage(file="301768731_1764248177260064_5431784438926177699_n2.png")
    btn.config(image=img2)
'''
