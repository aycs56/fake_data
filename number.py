from tkinter import*

# 處理隨機數生成
import random
# 處理複製的功能
import pyperclip
# 警告視窗
import tkinter.messagebox

# Tk視窗參數設定
win = Tk()
win.title("隨機數字產生器")
# win.geometry(長x寬 +X +Y)
win.geometry("250x450+800+400")
win.config(bg="#323232")

#////////////////////////////////////#

title_text = Label(text="播放數", fg="skyblue", bg="#323232")
# obj.config(font="字型 大小")
title_text.config(font="微軟正黑體 15")
title_text.pack()

# 播放數 文字 與 輸入框
play_range = Label(text="目前中間值", fg="white", bg="#323232")
play_range.pack()
play_entry = Entry()
play_entry.pack()

title_text = Label(text="點讚數", fg="skyblue", bg="#323232")
# obj.config(font="字型 大小")
title_text.config(font="微軟正黑體 15")
title_text.pack()


# 點讚數 文字 與 輸入框
like_range = Label(text="目前中間值", fg="white", bg="#323232")
like_range.pack()
like_entry = Entry()
like_entry.pack()

title_text = Label(text="請輸入評分", fg="skyblue", bg="#323232")
# obj.config(font="字型 大小")
title_text.config(font="微軟正黑體 15")
title_text.pack()

# 評分 文字 與 輸入框
score_entry = Entry()
score_entry.pack()


# 顯示 評分,點讚數,播放數
score_show = Label(text="評分數：", fg="white", bg="#323232")
score_show.pack()
play_show = Label(text="播放數：", fg="white", bg="#323232")
play_show.pack()
like_show = Label(text="點讚數：", fg="white", bg="#323232")
like_show.pack()


def gen_number():
    # 防呆 最低輸入評分,播放數小於點讚
    if score_entry.get() < "70" or score_entry.get() > "95":
        tkinter.messagebox.showerror(title="錯誤",message="你必須輸入 70 ~ 95 的評分")
    if play_entry.get() <= like_entry.get():
        tkinter.messagebox.showerror(title="錯誤",message="輸入的 播放數 不能小於 點讚數")
    if play_entry.get() < "350000" or like_entry.get() < "300000": 
        tkinter.messagebox.showerror(title="錯誤",message="輸入的 播放數 或 點讚數 不能小於 30萬")
    # 評分轉換百分比
    score_val = float(score_entry.get())
    score = str(score_val*0.1)
    pt_val = float(70)
    pt_score = (score_val-pt_val)*0.001
    # 播放數
    play_val = float(play_entry.get())
    play_max = float(play_entry.get())+10000
    play_min = float(play_entry.get())-10000
    # 點讚數
    like_val = float(like_entry.get())
    like_max = float(like_entry.get())+10000
    like_min = float(like_entry.get())-10000

    # random.randint(最小值, 最大值)
    x = float(random.randint(play_min, play_max))
    x = int(x+(play_val*pt_score))
    play = str(x)
    y = float(random.randint(like_min, like_max))
    y = int(y+(like_val*pt_score))
    like = str(y)
    score_show.config(text=""+score)
    play_show.config(text="" + play)
    like_show.config(text="" + like)

def score_copy():
    score = score_show.cget("text")
    pyperclip.copy(score)

def play_copy():
    play = play_show.cget("text")
    pyperclip.copy(play)


def like_copy():
    like = like_show.cget("text")
    pyperclip.copy(like)


# 執行及複製按鈕
null_show = Label(text="", fg="white", bg="#323232")
null_show.pack()
generate_btn = Button(text="執行", command=gen_number)
generate_btn.pack()

null_show = Label(text="", fg="white", bg="#323232")
null_show.pack()
copy_btn = Button(text="複製評分", command=score_copy)
copy_btn.pack()

null_show = Label(text="", fg="white", bg="#323232")
null_show.pack()
copy_btn = Button(text="複製播放數", command=play_copy)
copy_btn.pack()

null_show = Label(text="", fg="white", bg="#323232")
null_show.pack()
copy_btn = Button(text="複製點讚數", command=like_copy,)
copy_btn.pack()

win.mainloop()
