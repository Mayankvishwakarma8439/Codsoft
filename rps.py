from tkinter import *
from tkinter import messagebox
import random


user_score = 0
computer_score = 0
round_results = []


def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)


def play(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Scissors" and computer_choice == "Paper")
        or (user_choice == "Paper" and computer_choice == "Rock")
    ):
        user_score += 1
        result = "You win!"
    else:
        computer_score += 1
        result = "Computer wins!"

    round_results.append(result)
    update_score()
    result_label.config(text=f"Computer chose {computer_choice}. {result}")
    ask_play_again()


def update_score():
    user_score_label.config(text=f"User: {user_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")


def display_round_results():
    round_results_window = Toplevel(root)
    round_results_window.title("Round Results")
    round_results_window.geometry("600x350")
    round_results_window.configure(background="grey")
    results_text = "\n".join(f"Round {i + 1}: {result}" for i, result in enumerate(round_results))
    round_results_label = Label(round_results_window,background="#ffe042",fg="#e71989",font=("jokerman",20,"bold"),text=results_text)
    round_results_label.pack(pady=20)


def ask_play_again():
    play_again = messagebox.askyesno("Play Again?", "Do you want to play another round?")
    if play_again:
        result_label.config(text="")
    else:
        display_round_results()
        

root = Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("600x350")
root.configure(background="#13100a")
title_=Label(root,font=("showcard gothic",15),background="#13100a",fg="white",text="...Welcome to Rock, Paper and Scissors Game....")
instr_=Label(root,font=("8514oem",10),background="#13100a",fg="white",text="Choose Rock, Paper or Scissor:")
title_.pack(pady=5)
instr_.pack(pady=8)
rock_button = Button(root,cursor="mouse",background="#f4904b",font=("century schoolbook",13,"bold"),width=25, text="Rock", command=lambda: play("Rock"))
paper_button = Button(root,cursor="mouse",background="#f4904b",font=("century schoolbook",13,"bold"),width=25, text="Paper", command=lambda: play("Paper"))
scissors_button = Button(root,cursor="mouse",background="#f4904b", text="Scissors",font=("century schoolbook",13,"bold"),width=25, command=lambda: play("Scissors"))


user_score_label = Label(root,font=("courier new",10,"bold"),background="yellow", text="User: 0")
computer_score_label = Label(root,font=("courier new",10,"bold"),background="yellow", text="Computer: 0")

result_label = Label(root,background="#13100a",font=("8514oem",11),fg="white", text="")


rock_button.pack(pady=2)
paper_button.pack(pady=2)
scissors_button.pack(pady=2)
user_score_label.pack(pady=15)
computer_score_label.pack(pady=2)
result_label.pack(pady=10)


root.mainloop()
