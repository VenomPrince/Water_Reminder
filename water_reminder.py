import tkinter as tk
from tkinter import messagebox
import time
import threading

REMINDER_INTERVAL = 10 * 60   # 30 minutes (in seconds)

def show_reminder(drink_counter_label, drink_counter):
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askokcancel("💧 Water Reminder", "Time to drink some water!")
    root.destroy()

    if response:  # If "OK" is clicked
        drink_counter[0] += 1  # Increment the drink counter
        drink_counter_label.config(text=f"Water Drank: {drink_counter[0]}")

def main():
    # Variable to track the countdown
    countdown = REMINDER_INTERVAL
    drink_counter = [0]  # Use a list to allow modification in nested functions

    def update_countdown():
        nonlocal countdown
        minutes, seconds = divmod(countdown, 60)
        countdown_label.config(text=f"Next reminder in: {minutes:02}:{seconds:02}")
        if countdown > 0:
            countdown -= 1
            root.after(1000, update_countdown)  # Update every second
        else:
            # Show the reminder and reset the countdown
            show_reminder(drink_counter_label, drink_counter)
            countdown = REMINDER_INTERVAL  # Reset countdown
            update_countdown()  # Restart the countdown

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Water Reminder")
    root.geometry("300x150")
    root.resizable(False, False)

    # Label to indicate the app is running
    label = tk.Label(root, text="💧 Running in background...")
    label.pack(pady=10)

    # Countdown label
    countdown_label = tk.Label(root, text="")
    countdown_label.pack()

    # Drink counter label
    drink_counter_label = tk.Label(root, text="Water Drank: 0")
    drink_counter_label.pack(pady=10)

    # Start the countdown update
    update_countdown()

    root.mainloop()

if __name__ == "__main__":
    main()
