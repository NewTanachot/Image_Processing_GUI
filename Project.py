import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path

import cv2
from PIL import ImageTk,Image

global filePath
global G_rotate_img

filePath = ''

def choose_img():
    FILE = Path(__file__).resolve()
    global filePath
    filePath = filedialog.askopenfilename(initialdir=FILE.parent) # Pop up dialog for select the file with this file's parent directory
    
    path_label = tk.Label(second_frame,text='Path: ' +filePath)
    path_label.grid(row=3,column=1, pady=10)

# def rotate

def edge_detect(frame_2):
    global filePath, edge
    
    img_copy = cv2.imread(filePath)

    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, 50, 100)
    edge = Image.fromarray(edge)
    edge = ImageTk.PhotoImage(edge)

    tk.Label(frame_2, image=edge).grid(row=1,column=0)

def show_btn():

    global G_rotate_img

    if not filePath: #No image or incorrect file type
        messagebox.showwarning("Error", "No image selected!")
        return
    # Create GUI to make Top level of that window (default = root)
    # Using the 'tk.Tk()' the program cannot find the image
    edit_img = tk.Toplevel() 

    edit_first_frame = tk.Frame(edit_img)
    edit_first_frame.pack()
    
    edit_second_frame = tk.Frame(edit_img)
    edit_second_frame.pack()

    rotate_cw_icon = ImageTk.PhotoImage(Image.open('./img_res/rotate.png').resize((25,25)))
    rotate_countercw_icon = ImageTk.PhotoImage(Image.open('./img_res/counter-rotate.png').resize((25,25)))

    rotate_cw = tk.Button(edit_first_frame,image=rotate_countercw_icon, command=lambda: rotate_img(edit_second_frame, True))
    rotate_cw.grid(row=0,column=1, pady=10)

    rotate_cw = tk.Button(edit_first_frame,image=rotate_cw_icon, command=lambda: rotate_img(edit_second_frame, False))
    rotate_cw.grid(row=0,column=2, padx=10, pady=10)

    # filter = tk.Button(first_frame,text='filter')
    # filter.grid(row=0,column=2,padx=10 ,pady=10)

    edge_btn = tk.Button(edit_first_frame, text="Edge", command=lambda: edge_detect(edit_second_frame))
    edge_btn.grid(row=0,column=3, padx=10 , pady=10)

    img = Image.open(filePath)
    photo = ImageTk.PhotoImage(img)
    tk.Label(edit_second_frame, image=photo).grid(row=0,column=0)

    G_rotate_img = cv2.cvtColor(cv2.imread(filePath), cv2.COLOR_BGR2RGB)

    edit_img.title('Image Editor')
    edit_img.mainloop()
    
def rotate_img(frame_2, isCounterClockwise):
  
    global edge, G_rotate_img
    
    if isCounterClockwise == True:
        G_rotate_img = cv2.rotate(G_rotate_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    else:
        G_rotate_img = cv2.rotate(G_rotate_img, cv2.ROTATE_90_CLOCKWISE)

    edge = Image.fromarray(G_rotate_img)
    edge = ImageTk.PhotoImage(edge)

    tk.Label(frame_2, image=edge).grid(row=1,column=0)

app_name = 'Image Processing'

app_root = tk.Tk()
first_frame = tk.Frame(app_root)
first_frame.pack()
second_frame = tk.Frame(app_root)
second_frame.pack()
third_frme = tk.Frame(app_root)
third_frme.pack()

take_pic_button = tk.Button(first_frame,text='Take a photo')
take_pic_button.grid(row=0,column=1, pady=10)
choose_button = tk.Button(second_frame,text='Choose image',command=choose_img)
choose_button.grid(row=2,column=1, pady=10)
show_button = tk.Button(third_frme,text='Show image',command=show_btn)
show_button.grid(row=4,column=1, pady=10)

app_root.geometry("500x200")
app_root.title(app_name)
app_root.mainloop()