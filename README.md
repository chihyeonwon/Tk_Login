# Tk_Login
tkinter 라이브러리와 Python 언어를 사용해서 다음, 카카오 자동 로그인 프로그램 만들기   

## 25년 업무용 프로그램 개발 시작

위젯에 대한 설명   
사용자가 프로그램을 쓰기 쉽게 라벨을 붙임으로써 다른 위젯이 어떤 것인지 설명할 수 있습니다.   
프로그램이 어떤 상태인지에 대해서도 설명할 수 있습니다.   
## 창 생성

창을 생성하고 창의 제목, 크기, 세부옵션을 설정하고 실행합니다.   
```python
from tkinter import *
win = Tk()
win.title("Daum Log-in")
win.geometry("400x300")
win.option_add("*Font", "궁서 20")

win.mainloop()
```
  
## 다음로고 이미지 추가   

이미지 추가를 위해서 필요한 모듈을 import 한다.   
```python
from PIL import ImageTk
```

다음로고를 넣을 라벨을 생성하고 img 객체를 생성하고 image의 값으로 준다.   
```python  
# 다음 로고
lab_d = Label(win)
img = ImageTk.PhotoImage(file='image.png', master=win)
lab_d.config(image=img)
lab_d.pack()  
```

## ID,PW 라벨과 ID, PW 입력창 생성   

Label 함수를 사용해서 lab1 변수 이름의 라벨을 만들어주고 라벨을 배치합니다.   
```python
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
```
  
#### 아이디 입력창을 클릭하기 전   
![login](https://user-images.githubusercontent.com/58906858/151758951-270a8094-ef1d-47bf-a8d6-a28ca0bbae6e.png)
#### 아이디 입력창을 클릭한 후 기본문자열이 삭제됨을 알 수 있다.   
![login_delete](https://user-images.githubusercontent.com/58906858/151759115-bb726b38-6e62-4414-878c-b177ce19d488.png)
  

  
  
  
  
id 입력창은 bind함수로 좌클릭(Button-1)이 되었을 때만 clear함수를 실행하도록 구현하고 clear함수는 기본이메일형식일 때 좌클릭이 되면 기본이메일 문자열의 길이만큼 삭제하도록 구현한다.   

pw 입력창은 show 옵션으로 "*"을 줘서 입력하는 문자가 모두 *로 보이도록 구현한다.   
  
## 로그인 버튼 구현   
  
로그인 버튼 구현은 크롬브라우저의 버전과 같은 크롬드라이버를 다운로드하여 사용한다. 필요한 모듈을 import한다.   
```python
from selenium import webdriver
import time
```

버튼 구현 최종 코드는 다음과 같다.   
```
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
```
login 함수에 대한 설명   

5:7행 다운로드한 크롬드라이버를 현재 파일과 동일한 위치에 두고 옵션을 설정한다.       
8행 다음카카오 로그인 페이지의 url을 url 변수에 넣고   
9행 url 변수를 driver의 get함수에 넣어준다.   
10행 불러올 때 로딩 대기시간을 주지않으면 오류가 발생하므로 5초의 대기시간을 준다.   
11행 xpath1 변수에 id 입력창을 크롤링해서 저장한다.   
12행 driver의 find_element함수로 xpath1을 주고 send_keys 함수로 id 입력창에서 입력한 문자를 받아와서 입력한다.   
13행 xpath2 변수에 pw 입력창을 크롤링해서 저장한다.   
14행 driver의 find_element함수로 xpath1을 주고 send_keys 함수로 pw 입력창에서 입력한 문자를 받아와서 입력한다.   
15행 xpath3 변수에 로그인 버튼을 크롤링해서 저장한다.   
16행 로그인 버튼을 눌렀을 때 클릭이 발생하도록 설정한다.   
17행 lab3에 로그인 성공을 출력한다.   

20행에서 로그인버튼을 클릭하면 생성한 로그인 함수를 실행하도록 설정한다.   
  
## 최종 코드와 프로그램 실행 화면   
  
최종 코드는 다음과 같습니다.   
```python
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
```

#### 프로그램 초기화면은 다음과 같습니다.   
![login](https://user-images.githubusercontent.com/58906858/151758951-270a8094-ef1d-47bf-a8d6-a28ca0bbae6e.png)

#### 아이디와 비번을 입력하고 로그인버튼을 누르면 다음과 같이 다음 카카오 로그인 창이 열리는데    
![chrome](https://user-images.githubusercontent.com/58906858/151759564-23be583e-e5f9-4ca6-8f55-316393d9589f.png)  
  
*2022-01-31 현재 웹 보안 정책으로 크롤링이 정상적으로 작동되지 않음을 확인하였습니다. 
