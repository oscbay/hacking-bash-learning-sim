import tkinter as tk
import terminal
import startup
import tokenizer
import os
import io
from contextlib import redirect_stdout


SANDBOX = True

base_path = os.getcwd()

def setup_sandbox():
    if SANDBOX:
        sandbox_path = os.path.join(os.path.dirname(__file__), "sim_environment")
        os.makedirs(sandbox_path, exist_ok=True)
        os.chdir(sandbox_path)


def enter_command():
    entry_text = entry.get()
    if not entry_text.strip():
        return

    output = io.StringIO()
    with redirect_stdout(output):
        terminal.command_operation(SANDBOX, tokenizer.tokenize(entry_text), base_path)

    label.config(text=output.getvalue().rstrip())
    entry.delete(0, tk.END)


def main():
    setup_sandbox()

    root = tk.Tk()
    root.title("Hacking Simulator")

    global entry, label
    entry = tk.Entry(root, width=30)
    entry.pack(pady=20)

    button = tk.Button(root, text="Enter Command", command=enter_command)
    button.pack(pady=10)

    label = tk.Label(root, text="Enter a command")
    label.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()