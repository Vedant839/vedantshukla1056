import tkinter as tk
from tkinter import messagebox
import random

# Function to handle user input and determine game outcome
def play_game(user_choice):
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    ai_choice = random.choice(list(choices.keys()))

    result, result_face = determine_winner(user_choice, ai_choice)
    message = f"You chose {choices[user_choice]}.\nAI chose {choices[ai_choice]}.\n\nResult: {result}\n\n{result_face}"

    messagebox.showinfo("Result", message)

# Function to determine the winner based on choices
def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "It's a tie!", random.choice(Tied_faces)
    elif (user_choice == 'R' and ai_choice == 'S') or (user_choice == 'P' and ai_choice == 'R') or (user_choice == 'S' and ai_choice == 'P'):
        return "You win!", random.choice(Win_faces)
    else:
        return "You lose!", random.choice(Lost_faces)

# ASCII faces
Win_faces = ["(•◡•)", "(｡◕‿◕｡)", "ツ", "(^̮^)", "(¬‿¬)", "(˘◡˘)", "( •̀ᴗ•́ )", "ƪ(˘⌣˘)ʃ", "(✪‿✪)", "(• ◡•)"]
Lost_faces = ["(ㆆ _ ㆆ)", "(º﹃º)", "（◞‸◟）", "(ꆤ︵ꆤ)"]
Tied_faces = ["('-')", "(´・＿・`)", "(一_一)", "(꒪⌓꒪)"]

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create buttons for Rock, Paper, and Scissors
btn_rock = tk.Button(root, text="Rock", width=10, height=2, command=lambda: play_game('R'))
btn_paper = tk.Button(root, text="Paper", width=10, height=2, command=lambda: play_game('P'))
btn_scissors = tk.Button(root, text="Scissors", width=10, height=2, command=lambda: play_game('S'))

# Arrange buttons on the window
btn_rock.grid(row=0, column=0, padx=10, pady=10)
btn_paper.grid(row=0, column=1, padx=10, pady=10)
btn_scissors.grid(row=0, column=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
