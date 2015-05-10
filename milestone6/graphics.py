from Tkinter import *

master = Tk()
Label(text="Tennis court").pack()

w = Canvas(master, width=900, height=400)
w.pack()

w.create_rectangle(110, 80, 780, 320, fill="blue")
w.create_line(110, 80, 780, 80, fill="white", width=5.0) # top doubles line
w.create_line(110, 125, 780, 125, fill="white", width=5.0) # top singles line
w.create_line(110, 320, 780, 320, fill="white", width=5.0) # bottom doubles line
w.create_line(110, 275, 780, 275, fill="white", width=5.0) # bottom singles line
w.create_line(110, 80, 110, 320, fill="white", width=5.0) # right baseline
w.create_line(780, 80, 780, 320, fill="white", width=5.0) # left baseline
w.create_line(235, 125, 235, 275, fill="white", width=5.0) # left service line
w.create_line(655, 125, 655, 275, fill="white", width=5.0) # right service line
w.create_line(235, 200, 655, 200, fill="white", width=5.0) # center service line
w.create_line(445, 75, 445, 325, fill="black", width=5.0) #net

separator = Frame(height=2, bd=1, relief=RIDGE)
separator.pack(fill=X, padx=5, pady=5)

Label(text="Commands").pack()

#start_match = Button(master, text="Start Match", command=start)
#start_match.pack(side=LEFT)
def fsi():
    first_serve.destroy()
    second_serve.destroy()
    double_fault.destroy()
    server_won = Button(master, text="Server won", command=server_outcome)
    server_lost = Button(master, text="Server lost", command=receiver_outcome)
    server_won.pack()
    server_lost.pack()

def ssi():
    first_serve.destroy()
    second_serve.destroy()
    double_fault.destroy()
    server_won = Button(master, text="Server won", comman=server_outcome)
    server_lost = Button(master,text="Server lost", command=receiver_outcome)
    server_won.pack()
    server_lost.pack()

def df():
    first_serve.destroy()
    second_serve.destroy()
    double_fault.destroy()
    print "you suck at serving"

def start():
    start_match.destroy()
    global first_serve
    first_serve = Button(master, text="First Serve", command=fsi)
    global second_serve
    second_serve = Button(master, text="Second Serve", command=ssi)
    global double_fault
    double_fault = Button(master, text="Double Fault", command=df)
    first_serve.pack()
    second_serve.pack()
    double_fault.pack()
#def fsi():
#    first_serve.destroy()
#    server_won = Button(master, text="Server won", command=server_outcome)
#    server_lost = Button(master, text="Server lost", command=receiver_outcome)
#    server_won.pack()
#    server_lost.pack()
global start_match
start_match = Button(master,text="Start Match", command=start)
start_match.pack(side=LEFT)

mainloop()
