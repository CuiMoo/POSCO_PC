from tkinter import *
from tkinter import ttk,messagebox

root = Tk()
root.geometry('1000x750')
root.title('Resistor calculator')

Eint = ttk.Entry(root,font=(None,30))
Eint.pack(pady=20)
Bent = ttk.Button(root,text='Enter')
Bent.pack(ipadx=10,ipady=10)

#######Canvas borad############
canvas = Canvas(root,width=500,height=300)
canvas.pack(pady=10)

#resistor leg
canvas.create_polygon([0,240,500,240,500,260,0,260],fill='grey',outline='white')
#resistor body
canvas.create_polygon([100,200,400,200,400,300,100,300],fill='#e8be64')
#color1
canvas.create_polygon([150,200,175,200,175,300,150,300],fill='red')
#color2
canvas.create_polygon([200,200,225,200,225,300,200,300],fill='brown')
#color3
canvas.create_polygon([250,200,275,200,275,300,250,300],fill='blue')
#color4
canvas.create_polygon([325,200,350,200,350,300,325,300],fill='#e3a217')

root.mainloop()
'''

from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
'''