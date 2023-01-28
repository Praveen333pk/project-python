from tkinter import *
from pyqrcode import *
import png
from PIL import ImageTk,Image
def generate():
    link_name=name_entry.get()
    link=link_entry.get()
    file_name=link_name+".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,420,window=image_label)
root=Tk()
canvas=Canvas(root,width=400,height=600)
canvas.pack()
app_label=Label(root,text="QR Code Generator",fg='blue',font=("Arial",30))
canvas.create_window(200,50,window=app_label)
name_label=Label(root,text="Link Name")
link_label=Label(root,text="Link")
canvas.create_window(200,100,window=name_label)
canvas.create_window(200,150,window=link_label)
name_entry=Entry(root)
link_entry=Entry(root)
canvas.create_window(200,120,window=name_entry)
canvas.create_window(200,170,window=link_entry)
button=Button(text="Generate QR Code",command=generate)
canvas.create_window(200,200,window=button)
root.mainloop()