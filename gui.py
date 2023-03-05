import tkinter as tk
import random
from canvas import root, frame
from helpers import clear_screen, clear_all
from country_capital import country_capital_dict


# Creating the final page
def final_page():
    clear_screen()
    clear_text()
    clear_label()
    clear_answer_check()
    if len(answered_questions) >= len(country_capital_dict) - 4:
        message = f'You won!\nTotal points {correct_answers}'
        end_label = tk.Label(root, text=message, font=("Times New Roman", 50))
        end_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        frame.create_window(512, 450, window=end_label)

    else:
        message = f'You lose!\nTotal points {correct_answers}'
        end_label = tk.Label(root, text=message, font=("Times New Roman", 50))
        end_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        frame.create_window(512, 450, window=end_label)


def start_game():
    clear_screen()
    display_question()


def clear_text():
    answer.delete(0, len(answer.get()))


def clear_label():
    clear_all(text_label)


def clear_answer_check():
    clear_all(correct_incorrect_label)


def next_questions():
    clear_screen()
    clear_text()
    clear_label()
    clear_answer_check()
    display_question()


# Creating a function to check whether the user answer is correct or not
def check_answer():
    current_answer = answer.get()
    clear_screen()
    global correct_incorrect_label
    global wrong_answers
    if current_answer == current_correct_answer:
        global correct_answers
        correct_answers += 1
        correct_incorrect_label = tk.Label(root, text='Correct', font=("Times New Roman", 20))
        correct_incorrect_label.place(x=512, y=650, anchor=tk.CENTER)
    else:
        wrong_answers += 1
        reveal = f"The correct answer was {current_correct_answer}"
        correct_incorrect_label = tk.Label(root, text=reveal, font=("Times New Roman", 20))
        correct_incorrect_label.place(x=512, y=650, anchor=tk.CENTER)

    if len(answered_questions) == len(country_capital_dict) or wrong_answers == 5:
        final_page()

    else:
        next_question = tk.Button(
            root,
            text='Next>',
            font=('Times New Roman', 20),
            height=2,
            width=10,
            bg='#31301b',
            command=next_questions
            )
        frame.create_window(750, 700, window=next_question)


# Creating a function for displaying the questions
def display_question():
    countries = list(country_capital_dict)
    if len(answered_questions) <= len(country_capital_dict) and wrong_answers < 5:
        for country in random.sample(countries, len(countries)):
            if country not in answered_questions:
                question = f"Which is the capital city of {country}?"
                global text_label
                text_label = tk.Label(root, text=question, font=("Times New Roman", 20))
                text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                frame.create_window(512, 450, window=answer)
                global current_correct_answer
                current_correct_answer = country_capital_dict[country]
                answered_questions.append(country)

                submit_button = tk.Button(
                    root,
                    text='Submit',
                    font=('Times New Roman', 20),
                    height=2,
                    width=15,
                    bg='#31301b',
                    command=check_answer
                    )
                frame.create_window(512, 600, window=submit_button)
                return text_label
    else:
        final_page()


# Creating background

background_image = tk.PhotoImage(file='european_capitals_game.png')

background = tk.Label(
    root,
    image=background_image
)
background.place(x=0, y=0)

start_button = tk.Button(
    root,
    text='Start Game',
    font=('Times New Roman', 20),
    height=2,
    width=15,
    bg='#31301b',
    command=start_game
)

frame.create_window(512, 600, window=start_button)


# Defining the correct answer and getting the user input

answer = tk.Entry(root, bd=0)
current_correct_answer = ''

# Creating label variables in order to make them global

text_label = None
correct_incorrect_label = None

# Creating counters

correct_answers = 0
wrong_answers = 0
answered_questions = []

root.mainloop()
