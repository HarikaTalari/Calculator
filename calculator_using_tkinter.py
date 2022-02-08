from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("350x350")
root.resizable(False, False)
root.configure(bg="black")

res = ""


def clear_text():
    global res
    res = ""
    text_area.config(text="")


def display(value):
    global res
    res += value
    text_area.config(text=res)


def calculate_result():
    global res
    final_answer = ""
    if res != "":
        try:
            final_answer = eval(res)
        except:
            final_answer = "Invalid Input"
            res = ""
    text_area.config(text=final_answer)


text_area = Label(root, width=50, height=2, bg="#fff", font=('arial', 15, 'bold'))
text_area.pack()

seven = Button(root, text="7", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("7")).place(x=0,y=70)
eight = Button(root, text="8", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("8")).place(x=90,y=70)
nine = Button(root, text="9", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("9")).place(x=180,y=70)
four = Button(root, text="4", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("4")).place(x=1,y=140)
five = Button(root, text="5", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("5")).place(x=90,y=140)
six = Button(root, text="6", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("6")).place(x=180,y=140)
one = Button(root, text="1", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("1")).place(x=2,y=210)
two = Button(root, text="2", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("2")).place(x=90,y=210)
three = Button(root, text="3", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("3")).place(x=180,y=210)
zero = Button(root, text="0", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("0")).place(x=3,y=280)
add = Button(root, text="+", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("+")).place(x=270,y=70)
sub = Button(root, text="-", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("-")).place(x=270,y=140)
mul = Button(root, text="*", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("*")).place(x=270,y=210)
div = Button(root, text="/", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: display("/")).place(x=270,y=280)
clear = Button(root, text="C", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: clear_text()).place(x=90,y=280)
equals = Button(root, text="=", width=10, height=3, bg="#2a2d36", fg="#fff", command=lambda: calculate_result()).place(x=180, y=280)

root.mainloop()
