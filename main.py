import tkinter as tk
from tkinter import messagebox

class ModalDialog:
    def __init__(self, root, title, message):
        self.root = root
        self.title = title
        self.message = message
        self.backdrop = tk.Frame(self.root, bg="gray", opacity=0.5)
        self.backdrop.place(relwidth=1, relheight=1, anchor="center")
        self.dialog = tk.Frame(self.root, bg="white")
        self.dialog.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
        self.title_label = tk.Label(self.dialog, text=title, font=("Arial", 16))
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")
        self.message_label = tk.Label(self.dialog, text=message, font=("Arial", 14), wraplength=400)
        self.message_label.place(relx=0.5, rely=0.3, anchor="center")
        self.close_button = tk.Button(self.dialog, text="Close", command=self.close_dialog)
        self.close_button.place(relx=0.9, rely=0.9, anchor="e")

    def close_dialog(self):
        self.backdrop.destroy()
        self.dialog.destroy()

def main():
    root = tk.Tk()
    root.title("Modal Dialog")
    modal = ModalDialog(root, "Modal Dialog", "This is a modal dialog with a backdrop and a close button.")
    root.mainloop()

if __name__ == "__main__":
    main()
