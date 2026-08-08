import segno
import tkinter as tk
from tkinter import messagebox as msg
import datetime 
def qr_creation():
    encode = str(entry1.get())
    qr = segno.make_qr(encode)
    qr.save(f"segnoQR{datetime.datetime.now().strftime('%d.%m.%Y %H.%M.%S')}.png")
    msg.showinfo("Успех!","QR код успешно сгенерирован! Он появится в папке с программой")

root = tk.Tk()
root.title("sengoQR")
root.geometry("350x150")
label1 = tk.Label(text="Введите данные для кодировки (строка, число, вебсайт)")
label1.pack()
entry1 = tk.Entry()
entry1.pack()
but1 = tk.Button(text="Создать QR код!", command=qr_creation)
but1.pack()
root.mainloop()



