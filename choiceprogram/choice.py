from hashlib import new
import tkinter
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image
import tkinter.font
import random
import pandas as pd
import csv
import time

in_text = input('몇 반인가요? : ')

# 반별 명단 불러오기
data = open('class600.csv', encoding="utf-8")
data_csv = csv.reader(data)
next(data_csv)
df = pd.DataFrame(data_csv)
class1 = list(df[0])
class2 = list(df[1])
class3 = list(df[2])
class4 = list(df[3])
class5 = list(df[4])

# 발표자 뽑기 버튼 클릭시 실행할 함수 만들기


def click_btn():
    if in_text == '1':
        label["text"] = random.choice(class1)
        label.update()

    elif in_text == '2':
        label["text"] = random.choice(class2)
        label.update()

    elif in_text == '3':
        label["text"] = random.choice(class3)
        label.update()

    elif in_text == '4':
        label["text"] = random.choice(class4)
        label.update()

    else:
        label["text"] = random.choice(class5)
        label.update()


root = tkinter.Tk()
root.title("발표자 뽑기 프로그램")

# img = Image.open(r"C:\Users\User\Desktop\choiceprogram\ron.jpg")
# img.show()

# 배경 만들기
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=1000, height=800, bg="skyblue")
canvas.pack()
canvas_img = tkinter.PhotoImage(file="img\castle.jpg")

canvas.create_image(500, 500, image=canvas_img)

# 라벨 추가
label = tkinter.Label(root, text="????", font=("배달의민족 주아", 120), bg="white")
label.place(x=300, y=150)

# 버튼 추가
button = tkinter.Button(root, text="발표자는 누구", font=(
    "배달의민족 주아", 50), command=click_btn)

button.place(x=300, y=500)

root.mainloop()
