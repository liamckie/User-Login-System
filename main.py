from tkinter import *
import os


'''
TODO List:
- Logout()
- Create functions so only one screen is open at a time
- (Dashboard) Create home button
- Create a "Back" button to go to the previous screen
'''


def delete1():  # Deletes the message on the screen once the user has clicked on the "OK" button
    password_not_recognised_screen.destroy()


def delete2():  # Deletes the message on the screen once the user has clicked on the "OK" button
    user_not_found_screen.destroy()


def delete3():  # Deletes the message on the screen once the user has clicked on the "OK" button
    saved_screen.destroy()


def delete4():  # Deletes the message on the screen once the user has clicked on the "OK" button
    delete_note_screen1.destroy()


def logout():
    pass


def saved():
    global saved_screen

    saved_screen = Toplevel(screen)
    saved_screen.title("")
    saved_screen.geometry("240x100")
    Label(saved_screen, text="Note Saved", font=("monospace", 12)).pack()
    Button(saved_screen, text="OK", width="10", height="1", command=delete3).pack()


def save():
    filename = raw_filename.get()
    notes = raw_note.get()

    data = open(filename, "w")
    data.write(notes)
    data.close()

    saved()


def create_note():
    global raw_filename
    global raw_note

    raw_filename = StringVar()
    raw_note = StringVar()

    create_note_screen = Toplevel(screen)
    create_note_screen.title("Info")
    create_note_screen.geometry("300x250")
    Label(create_note_screen, text="Please enter filename for the note below: ").pack()
    Entry(create_note_screen, textvariable=raw_filename).pack()
    Label(create_note_screen, text="Please enter the contents for the note below: ").pack()
    Entry(create_note_screen, textvariable=raw_note).pack()
    Button(create_note_screen, text="Save", command=save).pack()


def view_note1():
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()

    view_note_screen1 = Toplevel(screen)
    view_note_screen1.title("Notes")
    view_note_screen1.geometry("400x400")

    Label(view_note_screen1, text=data1).pack()
    # Label(view_note_screen1, text=data1).pack()


def view_note():
    global raw_filename1

    raw_filename1 = StringVar()

    view_note_screen = Toplevel(screen)
    view_note_screen.title("View Note")
    view_note_screen.geometry("250x250")
    # Label(view_note_screen, text="Notes").pack()

    all_files = os.listdir()
    Label(view_note_screen, text="Please choose one of the files below").pack()
    Label(view_note_screen, text=all_files).pack()

    Entry(view_note_screen, textvariable=raw_filename1).pack()
    Button(view_note_screen, text="OK", command=view_note1).pack()


def delete_note1():
    global delete_note_screen1

    filename3 = raw_filename2.get()
    os.remove(filename3)

    delete_note_screen1 = Toplevel(screen)
    delete_note_screen1.title("Notes")
    delete_note_screen1.geometry("240x100")

    Label(delete_note_screen1, text=filename3 + " has been removed", font=("monospace", 12)).pack()
    Button(delete_note_screen1, text="OK", width="10", height="1", command=delete4).pack()
    # Label(view_note_screen1, text=data1).pack()


def delete_note():
    global raw_filename2

    delete_note_screen = Toplevel(screen)
    delete_note_screen.title("View Note")
    delete_note_screen.geometry("250x250")
    # Label(view_note_screen, text="Notes").pack()

    all_files = os.listdir()
    Label(delete_note_screen, text="Please choose one of the files below").pack()
    Label(delete_note_screen, text=all_files).pack()

    raw_filename2 = StringVar()
    Entry(delete_note_screen, textvariable=raw_filename2).pack()
    Button(delete_note_screen, text="OK", command=delete_note1).pack()


def session():
    session_screen = Toplevel(screen)
    session_screen.title("Dashboard")
    session_screen.geometry("400x400")
    Label(session_screen, text="Welcome to the Dashboard!").pack()
    Button(session_screen, text="Create Note",command=create_note).pack()
    Button(session_screen, text="View Note", command=view_note).pack()
    Button(session_screen, text="Delete Note", command=delete_note).pack()
    Button(session_screen, text="Exit", command=session_screen.quit).pack()


def login_success():
    session()
    # global login_success_screen
    #
    # login_success_screen = Toplevel(screen)
    # login_success_screen.title("Success")
    # login_success_screen.geometry("240x100")
    # Label(login_success_screen, text = "Login Successful", font = ("monospace", 12)).pack()
    # Button(login_success_screen, text = "OK", width = "10", height = "1", command = delete1).pack()


def password_not_recognised():
    global password_not_recognised_screen

    password_not_recognised_screen = Toplevel(screen)
    password_not_recognised_screen.title("")
    password_not_recognised_screen.geometry("240x100")
    Label(password_not_recognised_screen, text="Password not recognised", font=("monospace", 12)).pack()
    Button(password_not_recognised_screen, text="OK", width="10", height="1", command=delete1).pack()


def user_not_found():
    global user_not_found_screen

    user_not_found_screen = Toplevel(screen)
    user_not_found_screen.title("")
    user_not_found_screen.geometry("240x100")
    Label(user_not_found_screen, text="User not found", font=("monospace", 12)).pack()
    Button(user_not_found_screen, text="OK", width="10", height="1", command=delete2).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="").pack()
    Label(register_screen, text="Registration Successful :D", fg="green", font=("monospace", 13)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()


def register():
    global username
    global password
    global username_entry
    global password_entry
    global register_screen

    register_screen = Toplevel(screen)
    register_screen.title("Register")
    register_screen.geometry("300x275")

    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text = "").pack()

    Label(register_screen, text="Username * ").pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="Password * ").pack()
    password_entry = Entry(register_screen, textvariable=password)
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width="10", height="1", command=register_user).pack()


def login():
    global login_screen
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    login_screen = Toplevel(screen)
    login_screen.title("Login")
    login_screen.geometry("300x275")

    Label(login_screen, text="Please enter details below").pack()
    Label(login_screen, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username * ").pack()
    username_entry1 = Entry(login_screen, textvariable=username_verify)
    username_entry1.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_entry1 = Entry(login_screen, textvariable=password_verify)
    password_entry1.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width="10", height="1", command=login_verify).pack()


def main_screen():
    global screen

    screen = Tk()
    screen.geometry("300x275")
    screen.title("Notes 1.0")

    Label(text="Notes 1.0", bg="grey", width="300", height="2", font=("monospace", 13)).pack()
    Label(text="").pack()
    Button(text="Login", width="30", height="2", command=login).pack()
    Label(text="").pack()
    Button(text="Register", width="30", height="2", command=register).pack()
    Label(text="").pack()
    Button(text="Exit", width="30", height="2", command=screen.quit).pack()

    screen.mainloop()

main_screen()