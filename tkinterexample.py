from Tkinter import *

class App:

    def __init__(self, master):
        self.squareside=80.
        squareside = 80.
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        
        gameframe = Frame(master,borderwidth = 5)
        gameframe.pack(side=LEFT)
        if 0:        
            canvas = Canvas(width=200,height=200,bg='red')
            canvas.pack(expand=YES,fill=BOTH)
            
            img = PhotoImage(file='yellow.gif')
            board = Label(gameframe,image=img)
            board.pack()

        w = Canvas(gameframe,width=8*squareside,height=8*squareside)
        w.pack()
        for j in (1,3,5,7):
            for i in (1,3,5,7):
                w.create_rectangle(i*squareside,j*squareside, i*squareside+squareside, j*squareside+squareside, fill="white")
                w.create_rectangle((i-1)*squareside,(j-1)*squareside, (i-1)*squareside+squareside, (j-1)*squareside+squareside, fill="white")
                w.create_rectangle((i-1)*squareside,j*squareside, (i-1)*squareside+squareside, j*squareside+squareside, fill="blue")
                w.create_rectangle(i*squareside,(j-1)*squareside, i*squareside+squareside, (j-1)*squareside+squareside, fill="blue")
                
        
#        w.create_oval(0,0,squareside,squareside,fill="red")
#        self.drawPiece(w,0,0,"red")
        self.drawStartBoard(w)
    def drawPiece(self,w,I,J,c):
        buff = .2
        w.create_oval( (I+buff)*self.squareside, (J+buff)*self.squareside, (I+1-buff)*self.squareside, (J+1-buff)*self.squareside, fill=c)
    def say_hi(self):
        print "hi there, everyone!"
        
    def drawStartBoard(self,w):
        for j in (0,2):
            for i in (0,2,4,6):
                self.drawPiece(w,i,j,"red")
	    for j in (0,2,4,6):
	        self.drawPiece(w,j+1,1,"red")
	        self.drawPiece(w,j,6,"black")
        for j in (5,7):
            for i in (1,3,5,7):
                self.drawPiece(w,i,j,"black")
    

        
root = Tk()
root.title('Neural Checkers')

app = App(root)

root.mainloop()



# YARGHHH, ONLY JUNK CODE BE FOUND IN THE DEPTHS BELOW! YARGHH!
if 0:
    root = Tk()

    w = Label(root, text="Hello, world!")

    mainframe = Frame(root)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)



    k = Button(mainframe, text="Hello")
    #w.pack()
    k.pack(side=LEFT)

    root.mainloop()

if 0:
    from Tkinter import *
    from Tkinter import tk

    def calculate(*args):
        try:
            value = float(feet.get())
            meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass
        
    root = Tk()
    root.title("Feet to Meters")

    mainframe = tk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    feet = StringVar()
    meters = StringVar()

    feet_entry = tk.Entry(mainframe, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W, E))

    tk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
    tk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

    tk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
    tk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    tk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    feet_entry.focus()
    root.bind('<Return>', calculate)

    root.mainloop()
