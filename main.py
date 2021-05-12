from tkinter import *
from tkinter import colorchooser
from random import randint

from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Flash Card App")
root.geometry('500x500')
root.iconbitmap("instagram.ico")


# functions

def add_correct(num1, num2):
    correct = num1 + num2
    output_answer_correct = StringVar()
    output_answer_incorrect = StringVar()
    output_answer_correct.set(f"Correct {num1} + {num2} = {correct}")
    output_answer_incorrect.set(f"Incorrect: {num1} + {num2} = {correct}, not {add_answer.get()}")
    if int(add_answer.get()) == correct:
        add_correct_label.config(text=output_answer_correct.get())
    else:
        add_correct_label.config(text=output_answer_incorrect.get())

        # Clear the answer
    add_answer.delete(0, "end")

    # Generate two new random numbers
    num_1.set(randint(0, 10))
    num_2.set(randint(0, 10))
    add_flash.config(text=str(num_1.get()) + " + " + str(num_2.get()), font=("Muli", 72))


def add():
    hide_menu_frame()
    add_frame.pack(fill="both", expand=1)
    global num_1, num_2

    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 10))
    num_2.set(randint(0, 10))
    # Put random number onto the screen
    global add_flash
    add_flash = Label(add_frame, text=str(num_1.get()) + " + " + str(num_2.get()), font=("Muli", 72))
    add_flash.pack(pady=10)

    # Answer box
    global add_answer
    add_answer = Entry(add_frame)
    add_answer.pack(pady=5)
    # When we add arguments in function on buttons we need to add lambda
    # Answer button
    add_button = Button(add_frame, text="Answer", command=lambda: add_correct(num_1.get(), num_2.get()))
    add_button.pack(pady=5)

    # Create correct nd incorrect Message
    global add_correct_label
    add_correct_label = Label(add_frame, text="Enter Your Answer Above")
    add_correct_label.pack(pady=5)


def subtract_correct(num1, num2):
    correct = num1 - num2
    output_answer_correct = StringVar()
    output_answer_incorrect = StringVar()
    output_answer_correct.set(f"Correct {num1} - {num2} = {correct}")
    output_answer_incorrect.set(f"Incorrect: {num1} - {num2} = {correct}, not {subtract_answer.get()}")
    if int(subtract_answer.get()) == correct:
        subtract_correct_label.config(text=output_answer_correct.get())
    else:
        subtract_correct_label.config(text=output_answer_incorrect.get())

        # Clear the answer
    subtract_answer.delete(0, "end")

    # Generate two new random numbers
    num_1.set(randint(0, 10))
    num_2.set(randint(0, 10))
    subtract_flash.config(text=str(num_1.get()) + " - " + str(num_2.get()), font=("Muli", 72))


def subtract():
    hide_menu_frame()
    subtract_frame.pack(fill="both", expand=1)
    global num_1, num_2

    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 10))
    num_2.set(randint(0, 10))
    # Put random number onto the screen
    global subtract_flash
    subtract_flash = Label(subtract_frame, text=str(num_1.get()) + " - " + str(num_2.get()), font=("Muli", 72))
    subtract_flash.pack(pady=10)

    # Answer box
    global subtract_answer
    subtract_answer = Entry(subtract_frame)
    subtract_answer.pack(pady=5)
    # When we add arguments in function on buttons we need to add lambda
    # Answer button
    subtract_button = Button(subtract_frame, text="Answer", command=lambda: subtract_correct(num_1.get(), num_2.get()))
    subtract_button.pack(pady=5)

    # Create correct and incorrect Message
    global subtract_correct_label
    subtract_correct_label = Label(subtract_frame, text="Enter Your Answer Above")
    subtract_correct_label.pack(pady=5)


def multiply_correct(num1, num2):
    correct = num1 * num2
    output_answer_correct = StringVar()
    output_answer_incorrect = StringVar()
    output_answer_correct.set(f"Correct {num1} * {num2} = {correct}")
    output_answer_incorrect.set(f"Incorrect: {num1} * {num2} = {correct}, not {multiply_answer.get()}")
    if int(multiply_answer.get()) == correct:
        multiply_correct_label.config(text=output_answer_correct.get())
    else:
        multiply_correct_label.config(text=output_answer_incorrect.get())

        # Clear the answer
    multiply_answer.delete(0, "end")

    # Generate two new random numbers
    num_1.set(randint(0, 10))
    num_2.set(randint(0, 10))
    multiply_flash.config(text=str(num_1.get()) + " * " + str(num_2.get()), font=("Muli", 72))


def multiply():
    hide_menu_frame()
    multiply_frame.pack(fill="both", expand=1)
    global num_1, num_2

    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 10))
    num_2.set(randint(0, 10))
    # Put random number onto the screen
    global multiply_flash
    multiply_flash = Label(multiply_frame, text=str(num_1.get()) + " * " + str(num_2.get()), font=("Muli", 72))
    multiply_flash.pack(pady=10)

    # Answer box
    global multiply_answer
    multiply_answer = Entry(multiply_frame)
    multiply_answer.pack(pady=5)
    # When we add arguments in function on buttons we need to add lambda
    # Answer button
    multiply_button = Button(multiply_frame, text="Answer", command=lambda: multiply_correct(num_1.get(), num_2.get()))
    multiply_button.pack(pady=5)

    # Create correct and incorrect Message
    global multiply_correct_label
    multiply_correct_label = Label(multiply_frame, text="Enter Your Answer Above")
    multiply_correct_label.pack(pady=5)


def divide_correct(num1, num2):
    correct = round((num1 / num2), 2)
    output_answer_correct = StringVar()
    output_answer_incorrect = StringVar()
    output_answer_correct.set(f"Correct {num1} / {num2} = {correct}")
    output_answer_incorrect.set(f"Incorrect: {num1} / {num2} = {correct}, not {divide_answer.get()}")
    if float(divide_answer.get()) == correct:
        divide_correct_label.config(text=output_answer_correct.get())
    else:
        divide_correct_label.config(text=output_answer_incorrect.get())

        # Clear the answer
    divide_answer.delete(0, "end")

    # Generate two new random numbers
    num_1.set(randint(0, 10))
    num_2.set(randint(1, 10))
    divide_flash.config(text=str(num_1.get()) + " / " + str(num_2.get()), font=("Muli", 72))


def divide():
    hide_menu_frame()
    divide_frame.pack(fill="both", expand=1)
    global num_1, num_2

    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 10))
    num_2.set(randint(1, 10))
    # Put random number onto the screen
    global divide_flash
    divide_flash = Label(divide_frame, text=str(num_1.get()) + " / " + str(num_2.get()), font=("Muli", 72))
    divide_flash.pack(pady=10)

    # Answer box
    global divide_answer
    divide_answer = Entry(divide_frame)
    divide_answer.pack(pady=5)
    # When we add arguments in function on buttons we need to add lambda
    # Answer button
    divide_button = Button(divide_frame, text="Answer", command=lambda: divide_correct(num_1.get(), num_2.get()))
    divide_button.pack(pady=5)

    # Create correct and incorrect Message
    global divide_correct_label
    divide_correct_label = Label(divide_frame, text="Enter Your Answer Above, Two digits after the comma")
    divide_correct_label.pack(pady=5)


def hide_menu_frame():
    # destroy children widget in each frame
    for widget in add_frame.winfo_children():
        widget.destroy()

    for widget in subtract_frame.winfo_children():
        widget.destroy()

    for widget in add_frame.winfo_children():
        widget.destroy()

    for widget in add_frame.winfo_children():
        widget.destroy()

    for widget in start_frame.winfo_children():
        widget.destroy()

    #     Hide all frames
    add_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()
    start_frame.pack_forget()


# Define main menu
my_menu = Menu(root)
root.config(menu=my_menu)


def home():
    hide_menu_frame()
    start_frame.pack(fill="both", expand=1)
    start_label = Label(start_frame, text="Welcome To Math Calculations", font=("Helvetica", 18)).pack(pady=40)
    # button to flashcards
    a_button = Button(start_frame, text="Addition Flashcard", command=add).pack(pady=5)
    a_button = Button(start_frame, text="Subtract Flashcard", command=subtract).pack(pady=5)
    a_button = Button(start_frame, text="Multiply Flashcard", command=multiply).pack(pady=5)
    a_button = Button(start_frame, text="Divide Flashcard", command=divide).pack(pady=5)


# Create menu items
math_menu = Menu(my_menu)
my_menu.add_cascade(label="MathCards", menu=math_menu)
math_menu.add_command(label="Add", command=add)
math_menu.add_command(label="Subtract", command=subtract)
math_menu.add_command(label="Multiply", command=multiply)
math_menu.add_command(label="Divide", command=divide)
math_menu.add_separator()
math_menu.add_command(label="Home", command=home)
math_menu.add_command(label="Exit", command=root.quit)

# Create Math frames
add_frame = Frame(root, width=400, height=400)
subtract_frame = Frame(root, width=400, height=400)
multiply_frame = Frame(root, width=400, height=400)
divide_frame = Frame(root, width=400, height=400)

start_frame = Frame(root, height=400, width=400)

# show the start screen
home()


root.mainloop()

if __name__ == '__main__':
    pass
