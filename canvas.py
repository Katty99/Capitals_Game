from tkinter import Tk, Canvas


def create_root():
    root = Tk()

    root.title("Capitals Game")
    root.resizable(False, False)
    root.geometry('1024x768')

    return root


def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()
