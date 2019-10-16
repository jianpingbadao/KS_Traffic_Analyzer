import tkinter as tk
# import cv2
# import PIL.Image, PIL.ImageTk


win = tk.Tk()
win.geometry("500x300")
win.title("Testing Widgets")

# cv_img = cv2.cvtColor(cv2.imread("2016-McLaren-570S-front-three-quarters-in-motion-02.wdp.jxr"), cv2.COLOR_BGR2RGB)
canvas = tk.Canvas(win, width = 300, height = 300)      
canvas.pack()      
img = tk.PhotoImage(file = 'C:\\Users\\mhepel\\Desktop\\CSE 321 Project\ \hole.png')      
canvas.create_image(20,20,image=img) 

frame_1 = tk.Frame(win)
frame_1.place(height = 300, width = 500)

label_1 = tk.Label(frame_1, text = "Label 1")
label_1.pack()
a = [0]
b = 0
carspeed = 0
def button_click():
    global b
    b = b+ 1
    label_3.config(text = b)
    print("hi")
    global carspeed 
    # carspeed = 20
    # global a 
    # a = a + carspeed
    # global n 
    a[0] = (a[0]*(b-1)+carspeed)/b
    print(a[0])
    label_2.config(text = "%.2f"%a[0] )

def ret_input():
    global carspeed
    carspeed = text_box.get("1.0", "end-1c")
    carspeed = int(carspeed)

button_1 = tk.Button(frame_1, text = "One press", command = button_click)
button_1.place(x = 50, y = 200, width = 100)

button_2 = tk.Button(frame_1, text = "Inc car",  command = button_click)
button_2.place(x = 350, y = 200, width = 100)
# frame_2 = tk.Frame(win)
# frame_2.place(x = 50, width = 100)

label_2 = tk.Label(frame_1, text = a)
label_2.place(x = 100, y = 250, width = 50)
label_3 = tk.Label(frame_1, text = b)
label_3.place(x = 400, y = 250, width = 100)

label_4 = tk.Label(frame_1, text = "Avg Speed:")
label_4.place(x = 0, y = 250, width = 100)
label_5 = tk.Label(frame_1, text = "Num of cars")
label_5.place(x = 300, y = 250, width = 100)

label_6 = tk.Label(frame_1, text = "mph")
label_6.place(x = 150, y = 250, width = 100)

# e1 = tk.Entry(win)
# e1.grid(row = 0, column = 0)
text_box = tk.Text(win, height = 2, width = 10)
text_box.pack()
button_3 = tk.Button(win, text = "enter", command = lambda:ret_input()).pack()
label_7 = tk.Label(frame_1, text = win)
label_7.place(x = 300, y = 150, width = 100)


# button_1.clicked.connect(self.inc)

# def inc(self, text):
  #   a = a/2
    # self.label_2.setText(a)


win.mainloop()