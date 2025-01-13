from tkinter import *
from tkinter import messagebox
import base64
import os


def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).strip()  # Trim trailing newlines
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(
            screen2, 
            text="DECRYPTED TEXT", 
            font="arial 12 bold", 
            fg="black", 
            bg="#00bd56"
        ).pack(pady=10)
        
        text2 = Text(screen2, font="Roboto 10", bg="black", fg="white", wrap=WORD, relief=GROOVE, bd=0)
        text2.pack(fill=BOTH, expand=True, padx=10, pady=5)

        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    else:
        messagebox.showerror("Decryption", "Invalid Password")


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip()  # Trim trailing newlines
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(
            screen1, 
            text="ENCRYPTED TEXT", 
            font="arial 12 bold", 
            fg="black", 
            bg="#ed3833"
        ).pack(pady=10)
        
        text2 = Text(screen1, font="Roboto 10", bg="black", fg="white", wrap=WORD, relief=GROOVE, bd=0)
        text2.pack(fill=BOTH, expand=True, padx=10, pady=5)

        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    else:
        messagebox.showerror("Encryption", "Invalid Password")


def main_screen():
    global screen, code, text1

    screen = Tk()
    screen.title("PctApp")
    screen.geometry("400x500")
    screen.configure(bg="#1a1a1a")

    # Load Icon
    try:
        image_icon = PhotoImage(file="/Users/joaorafaelbaiao/Desktop/Encryption and Decryption project/Key.png")
        screen.iconphoto(False, image_icon)
    except Exception as e:
        print(f"Error loading icon: {e}")

    # Reset function
    def reset():
        code.set("")
        text1.delete(1.0, END)

    # Heading
    Label(
        screen, 
        text="Encryption & Decryption Tool", 
        font=("calibri", 16, "bold"), 
        bg="#1a1a1a", 
        fg="white"
    ).grid(row=0, column=0, columnspan=2, pady=10)

    # Input text
    Label(
        screen, 
        text="Enter text for encryption and decryption:", 
        font=("calibri", 12), 
        bg="#1a1a1a", 
        fg="white"
    ).grid(row=1, column=0, columnspan=2, padx=10, sticky=W)

    text1 = Text(
        screen, 
        font="Roboto 12", 
        bg="black", 
        fg="white", 
        wrap=WORD, 
        relief=GROOVE, 
        height=6
    )
    text1.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=NSEW)

    # Input key
    Label(
        screen, 
        text="Enter secret key:", 
        font=("calibri", 12), 
        bg="#1a1a1a", 
        fg="white"
    ).grid(row=3, column=0, columnspan=2, padx=10, sticky=W)

    code = StringVar()
    Entry(
        screen, 
        textvariable=code, 
        show="*", 
        font=("arial", 14), 
        bg="black", 
        fg="white"
    ).grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=NSEW)

    # Buttons
    Button(
        screen, 
        text="ENCRYPTION", 
        bg="#ed3833", 
        fg="black", 
        font=("arial", 12), 
        command=encrypt
    ).grid(row=5, column=0, pady=20, padx=10, sticky=NSEW)

    Button(
        screen, 
        text="DECRYPTION", 
        bg="#00bd56", 
        fg="black", 
        font=("arial", 12), 
        command=decrypt
    ).grid(row=5, column=1, pady=20, padx=10, sticky=NSEW)

    Button(
        screen, 
        text="RESET", 
        bg="#1089ff", 
        fg="black", 
        font=("arial", 12), 
        command=reset
    ).grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky=NSEW)

    # Make rows/columns scalable
    screen.grid_rowconfigure(2, weight=1)  # Textbox row
    screen.grid_rowconfigure(5, weight=0)  # Buttons
    screen.grid_columnconfigure(0, weight=1)  # First column
    screen.grid_columnconfigure(1, weight=1)  # Second column

    screen.mainloop()


main_screen()
