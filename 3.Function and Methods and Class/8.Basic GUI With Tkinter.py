# import turtle
#
# james = turtle.Turtle()
#
# """ drawing a cube """
# james.backward(100)
# james.left(90)
# james.backward(100)
# james.left(90)
# james.backward(100)
# james.left(90)
# james.backward(100)
# james.left(90)
#
# """ drawing four 4 """
#
# window = turtle.Screen()
# four = turtle.Turtle()
# # changing the title of the GUI
# window.title("Design Four")
# # changing the interface bacground color
# window.bgcolor("grey")
#
# # delaying a drawing by 100s
# window.delay(100)
#
# four.left(90)
# four.color("red")
# four.backward(100)
#
# four.right(90)
# four.color("blue")
# four.forward(100)
#
# four.right(90)
# four.color("green")
# four.backward(100)
# four.forward(200)

# login form

# from tkinter import *
# from functools import partial
#
#
# def login(username, password):
#     print("username :", username.get())
#     print("password :", password.get())
#
#
# # window
# root = Tk()
# root.geometry('400x400')
# root.title('Login Form')
#
# # username label and text entry box
# label_username = Label(root, text="Username").grid(row=0, column=0)
# username = StringVar()
# entry_username = Entry(root, textvariable=username).grid(row=0, column=1)
#
# # password label and password entry box
# label_password = Label(root, text="Password").grid(row=1, column=0)
# password = StringVar()
# entry_password = Entry(root, textvariable=password, show='*').grid(row=1, column=1)
#
# login_form = partial(login, username, password)
#
# # login button
# loginButton = Button(root, text="Sign In", command=login_form).grid(row=4, column=0)
#
# root.mainloop()

import tkinter as tk
import mysql.connector
from tkinter import *


def display_input():
    username_entered = Username.get()
    password_entered = password.get()

    print(f"Username : {username_entered}\nPassword{password_entered}")

    login(username_entered, password_entered)


def login(username_entered, password_entered):

    # if credential are match
    if password_entered:
        db = mysql.connector.connect(host="localhost",
                                     user=username_entered,
                                     password=password_entered,
                                     db="University")
        cursor = db.cursor()

    # If no password was pass by the user
    else:
        db = mysql.connector.connect(host="localhost",
                                     user=username_entered,
                                     db="University")
        cursor = db.cursor()

    # query
    sql = "select * from students"

    try:
        cursor.execute(sql)
        result = cursor.fetchall()

        # Printing the result

        for x in result:
            print(x)
        print("Query successfully")

    except:
        db.rollback()
        print("Error")


root = tk.Tk()
root.geometry("400x400")
root.configure(background='dodger blue')
icon_logo = PhotoImage(file="icon.png")
root.iconphoto(False, icon_logo)
root.resizable(False, False)
root.title("University Of Town ")


# Definging the first row

img =PhotoImage(file='icon.png')
Label(root, image=img).place(x=10, y=10)

label_username = tk.Label(root, text="Student Number", bg='powder blue')
label_username.place(x=50, y=135)

Username = tk.Entry(root, width=40, font=('arial', 15, 'bold'))
Username.place(x=150, y=130, width=150)

label_password = tk.Label(root, text="Password ", bg='powder blue')
label_password.place(x=50, y=175)

password = tk.Entry(root, width=40,  show='*', font=('arial', 15, 'bold'))
password.place(x=150, y=170, width=150)

btn_submit = tk.Button(root, text="Login", bg='tomato', command=display_input)
btn_submit.place(x=200, y=210, width=55)

root.mainloop()
