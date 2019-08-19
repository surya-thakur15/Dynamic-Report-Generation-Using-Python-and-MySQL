from dbw import *
from tkinter import *

"""this module is for the first GUI """

root = Tk()

root.title("Pixel Panda")
root.iconbitmap(default='logo.ico')
lbl = Label(root, text="Welcome to Wizard", font=("Arial Bold", 20), fg="#020042", bg="#e8e8fc")
lbl.grid(column=0, row=0, pady=(56, 20), padx=(92, 90))
root.resizable(0, 0)
root.geometry('600x380')
root.config(bg="#e8e8fc")


def clicked():
    s_name = txt.get()
    data_fetch_from_key(s_name)  # this method is defined in dbw


txt = Entry(root, width=50, bg="#fff")

txt.insert(0, 'Report Code: <DDMMYY><RunNo><ClientCode>')
txt.bind("<FocusIn>", lambda args: txt.delete('0', 'end'))

txt.grid(column=0, row=1)
root.bind("<Return>", lambda event: clicked())

btn = Button(root, text="Generate Report", bg="#aca7ce", fg="black", command=clicked)


###############################################################################################################
btn.grid(column=0, row=3, pady=20)

root.mainloop()
