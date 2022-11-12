from tkinter import*
import requests 

def host():
    import requests 
    garbled=inp.get()
    class Change():
        # 將字典的鍵-值互換，例: {'a': 1, 'b': 2}-> {1: 'a', 2: 'b'}
        def dict_key_val_reverse(convertDict):
            return dict(zip(convertDict.values(), convertDict.keys()))
        #轉換
        def strConvert(message):
            restring = ""
            convertDict = dict(zip(range(33, 127), range(65281, 65375)))
            convertDict.update({32: 12288})
            convertDict = Change.dict_key_val_reverse(convertDict)
            for uchar in message:
                u_code = ord(uchar)
                if u_code in convertDict:
                    u_code = convertDict[u_code]
                restring += chr(u_code)
            return restring

    #主程式
    while True:
        message = str(garbled)    #讓使用者輸入欲翻譯之文字
        message = Change.strConvert(message)    #將全形文字轉換成半形文字
        message = message + ' '     #防止使用者輸入如：'i '(喔) 時，誤將結尾空格捨去、少打
        message = message.replace(' ', '=')     #將所有空格轉換為 '='
        URL = f'https://www.google.com/inputtools/request?text={message}&ime=zh-hant-t-i0&cb=?'
        message = requests.post(url=URL)    #將請求post給上述連結
        print(message.json()[1][0][1][0])   #解析回傳之資料，並print出
        
        
    
    


win=Tk()
win.title("注音鑑翻譯")
win.geometry("600x500")

#按鈕圖片
img=PhotoImage(file="icon.png")#暫時未決定

#按鈕
btn=Button(win)
btn.config(command=host)
btn.config(text="轉換")
btn.pack()
#標籤:輸入注音亂碼(固定)
lb=Label()
lb.config(text="輸入注音亂碼")
lb.pack()
#亂碼詩入藍
inp=Entry()
inp.pack()
#標籤:結果
lb2=Label()
lb2.config(text="結果")
lb2.pack()
#標籤(結果)
lb3=Label()

#設為常駐視窗
win.mainloop()