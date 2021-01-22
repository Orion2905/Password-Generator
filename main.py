import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

class Main:
    def __init__(self, root):
        root.title('Password Generator')
        root.geometry('500x250')
        root.resizable(False, False)
        root.grid_columnconfigure(0, weight=1)

        self.root = root

        font_2 = ('Tw Cen MT', 14, 'bold')
        font_3 = ('Bell MT', 16, 'bold')

        self.title = tk.Label(root, text="Password Generator", font=("The Bold Font",16))
        self.title.pack(pady=10)

        self.title_2 = tk.Label(root, text="Enter password Length")
        self.title_2.pack()

        self.text_variable = tk.StringVar()
        self.password = tk.Entry(root, textvariable=self.text_variable, justify="center", border=2, font=font_2, bg="#cccccc")
        self.password.pack(fill="both", padx=20, ipady=10)

        self.button_gen = tk.Button(root, text="generate your password", command=self.pass_gen, bg="#00b300")
        self.button_gen.pack(fill="both", padx=20)

        self.copy = tk.Button(root, text="copy to clipboard", command=self.copy_to_clipboard, bg="#6666ff")
        self.copy.pack(fill="both", padx=20)

        self.gener_pass = tk.Label(self.root, text="", font=font_3, bg="yellow")
        self.gener_pass.pack(pady=10, fill="both")

        self.done = tk.Label(self.root, text="")
        self.done.pack(fill="both")

    def pass_gen(self):
        a = 10
        try:
            lenght = int(self.password.get())
            chars = "abcdefghijklmnopqrstuvwyxz1234567890-+*/.#"
            char_list = list(chars)

            password = ""

            print("password Length = %d" % int(lenght))

            for i in range(int(lenght)):
                password = random.choices(char_list, k=int(lenght))

            print("Your password is: ","".join(password),"Password Length is: %d" % len(password))
            self.gener_pass.configure(text="".join(password))
            print(self.gener_pass.cget("text"))
        except Exception as e:
            messagebox.showerror(title="Error", message="Error: %s"
                                                              % str(e))

    def copy_to_clipboard(self):
        pyperclip.copy(self.gener_pass.cget("text"))
        self.done.configure(text="your password has been copied")
        spam = pyperclip.paste()


if __name__ == "__main__":
    root = tk.Tk()
    main = Main(root)
    root.mainloop()