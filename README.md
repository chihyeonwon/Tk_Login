# Tk_Login
tkinter 라이브러리와 Python 언어를 사용해서 다음, 카카오 자동 로그인 프로그램 만들기

위젯에 대한 설명
사용자가 프로그램을 쓰기 쉽게 라벨을 붙임으로써 다른 위젯이 어떤 것인지 설명할 수 있습니다.
프로그램이 어떤 상태인지에 대해서도 설명할 수 있습니다.

라벨 관련함수

Label 함수 전체창 변수로 전달
lab = Label(win)
lab.config(text="")
img 옵션을 img 객체로 넣어줍니다.
lab.config(image = img)
이미지 객체는 PhotoImage 함수를 통해 만듭니다.
file 옵션에는 그림파일 주소 및 이름 .master옵션에는 창 변수
img = PhotoImage(file="".master=win)
subsample함수로 축소가능
img = img.subsample(3) # 1/3로축소
ent.config(show= "*") *형태로 가리기 입력 문자 숨기기
ent.insert(0."temp@temp.com") 글자입력 0은 삽입할 위치 뒤에 입력할 내용 입력창 문자열 삽입
ent.delete(0.3) 0~2번째 문자열 삭제 입력창 문자열 삭제
ent.bind("<Button-1>".clear) 입력창 클릭시 명령 클릭됐을 때 실행되는 함수를 . 뒤에
def clear(event) 입력변수 event 
event의 의미 아무때나 실행(run)이 되는 게아니라 좌클릭될 때만



lab.pack()

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

## ID 라벨과 입력창 생성

Label 함수를 사용해서 lab1 변수 이름의 라벨을 만들어주고 라벨을 배치합니다.
```python
lab1 = Label(win)

lab1.pack()
```

라벨
```python
lab1 = Label(win)
lab1.config(text="ID")
lab1.pack()
```


입력창
```python
ent1 = Entry(win)

ent1.pack()
