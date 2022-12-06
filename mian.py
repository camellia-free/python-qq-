import tkinter as tk

# from login import *

win = tk.Tk()  # 建立根窗口
win.geometry('700x530')  # 设置窗口大小
win.title("hello world")
win.iconbitmap('asirm-u8nmt-001.ico')

win["background"] = "#013328"  # 设置窗口背景色
# 设置两个标签
la = tk.Label(win, text='hello')  # 点击登录按钮后将按钮变为登录中
la1 = tk.Label(win, text='账号')
la2 = tk.Label(win, text='密码')
# 将标签放置在根窗口内，使用grid
la1.grid(row=0)
la2.grid(row=1)
la.grid(row=3)
# 为文本标签创建两个输入框控件
en1 = tk.Entry(win)
en2 = tk.Entry(win)
# 对控件进行布局管理，放在文本标签后面
en1.grid(row=0, column=1)
en2.grid(row=1, column=1)


def login():
    la.configure(text="登陆中~")


# text = tk.Label(win, text="hello dear", bg="#013328", fg='#CC8B65', font=('Times', 20, "bold italic"))  # 字体大小是20， 字体是粗斜体
# text.pack()  # 将文本放在根窗口内

# 增加一个按钮用于登录
bu = tk.Button(win, text='登录', command=login)
bu.grid(row=4, column=4)

win.mainloop()
