import segno
import tkinter as tk
from tkinter import messagebox as msg
import datetime 
def qr_creation():
    encode = str(entry1.get())
    qr = segno.make_qr(encode)
    qr.save(f"segnoQR{datetime.datetime.now().strftime('%d.%m.%Y %H.%M.%S')}.png")
    msg.showinfo("Success!","QR code was successfully generated")

root = tk.Tk()
root.title("sengoQR")
root.geometry("350x150")
label1 = tk.Label(text="Enter data for encode (string, number, website)")
label1.pack()
entry1 = tk.Entry()
entry1.pack()
but1 = tk.Button(text="Generate QR code!", command=qr_creation)
but1.pack()
root.mainloop()



