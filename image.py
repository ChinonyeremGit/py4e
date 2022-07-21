from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('my boy')

image1 = ImageTk.PhotoImage((Image.open("images/i1.png")).resize((250,200)))
image2 = ImageTk.PhotoImage((Image.open("images/i2.png")).resize((250,200)))
image3 = ImageTk.PhotoImage((Image.open("images/i3.png")).resize((250,200)))
image4 = ImageTk.PhotoImage((Image.open("images/i4.png")).resize((250,200)))
image5 = ImageTk.PhotoImage((Image.open("images/i5.png")).resize((250,200)))
image6 = ImageTk.PhotoImage((Image.open("images/i6.png")).resize((250,200)))

li = [image1, image2, image3, image4, image5, image6]

# create label and add resize image
my_label = Label(image=image1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back


    my_label.grid_forget()
    my_label= Label(image=li[image_number-1])
    button_forward= Button(root, text='>>', command=lambda:forward(image_number+1))
    button_back= Button(root, text='<<', command=lambda:back(image_number-1))

    if image_number==6:
        button_forward= Button(root, text='>>', state= DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label= Label(image=li[image_number-1])
    button_forward= Button(root, text='>>', command=lambda:forward(image_number+1))
    button_back= Button(root, text='<<', command=lambda:back(image_number-1))
    if image_number == 1:
        button_back= Button(root, text='<<', state= DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid

button_back= Button(root, text='<<', command=back, state= DISABLED)
button_forward= Button(root, text='>>', command=lambda: forward(2))
button_quit= Button(root, text='exit program', command=root.quit)
button_quit.grid(row=1, column=1)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)

def update(image_number):
    status = Label(root, text = 'image ' + str(image_number)+ ' of ' + str(len(li)), bd=1, relief=SUNKEN, anchor=E,command=update)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
status = Label(root, text = 'image 1 of ' + str(len(li)),command=lambda:update(image_number), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()
