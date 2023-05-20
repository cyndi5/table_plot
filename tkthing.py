import argparse
from pathlib import Path
import tkinter as tk
import tkinter.messagebox


def handle_click(event):
    '''Display a message showing which button was clicked.'''
    tk.messagebox.showinfo("Button Clicked", "You clicked the " + event + " button.")


def main():
    '''Main function'''

    # Handle command-line arguments
    parser = argparse.ArgumentParser(description='Reads list of keywords from a file.')
    parser.add_argument("--file", required=True, default=None, type=str, help="path to keywords file")
    args = parser.parse_args()
    print(args.file)

    # One-liner to read lines into an array, stripping newlines
    lines = map(lambda x: x.strip(), Path(args.file).read_text().splitlines())

    for line in lines:
        print(f"Line: '{line}'")

    # Create a window.
    root = tk.Tk()

    # Create two buttons.
    button1 = tk.Button(root, text="Button 1", command=lambda: handle_click('1'))
    button2 = tk.Button(root, text="Button 2", command=lambda: handle_click('2'))

    # Pack the buttons.
    button1.pack()
    button2.pack()

    # Start the main loop.
    root.mainloop()


if __name__ == "__main__":
    print("Running main()")
    main()

