from tkinter import *
from PIL import ImageTk
from selenium import webdriver
import time

win = Tk()
win.title("Daum Log-in")
win.geometry("400x600")
win.option_add("*Font", "궁서 20")

# 다음 로고
lab_d = Label(win)
img = ImageTk.PhotoImage(file='image.png', master=win)
lab_d.config(image=img)
lab_d.pack()
# id 라벨
lab1 = Label(win)
lab1.config(text="ID")
lab1.pack()

# id 입력창
ent1 = Entry(win)
ent1.insert(0, "temp@temp.com")


def clear(event):
    if ent1.get() == "temp@temp.com":
        ent1.delete(0, len(ent1.get()))


ent1.bind("<Button-1>", clear)
ent1.pack()

# pw 라벨
lab2 = Label(win)
lab2.config(text="Password")
lab2.pack()

# pw 입력창
ent2 = Entry(win)
ent2.config(show="*")
ent2.pack()

# 로그인 버튼
btn = Button(win)
btn.config(text="로그인")


def login():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    url = "https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net%252F"
    driver.get(url)
    time.sleep(5)  # 5초동안 대기합니다.
    xpath1 = "//input[@name='email']"
    driver.find_element(xpath1).send_keys(ent1.get())
    xpath2 = "//input[@name='password']"
    driver.find_element(xpath2).send_keys(ent2.get())
    xpath3 = "//button[@class='btn_g btn_confirm submit']"
    driver.find_element(xpath3).click()
    lab3.config(text="[메시지] 로그인 성공")


btn.config(command=login)
btn.pack()

# 메시지 라벨
lab3 = Label(win)
lab3.pack()

win.mainloop()
