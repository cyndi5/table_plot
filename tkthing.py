import argparse
import tkinter as tk
import tkinter.messagebox


def handle_click(event):
    # Display a message showing which button was clicked.
    tk.messagebox.showinfo("Button Clicked", "You clicked the " + event + " button.")


def main():
    parser = argparse.ArgumentParser(description='Uses Plotly Dash core to plot a CSV from Google Science Journal accelerometer readings.')
    parser.add_argument("--file", required=True, default=None, type=str, help="path to CSV")
    
    args = parser.parse_args()
    print(args.file)
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

