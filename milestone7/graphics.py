from Tkinter import *
from players import Player

master = Tk()

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
w.create_line(445, 75, 445, 325, fill="black", width=5.0) # net

separator = Frame(height=5, bd=3, relief=RIDGE)
separator.pack(fill=X, padx=5, pady=5)

def match_finished(player):
    end_text = "The match is finished!" + player + " has won!"
    match_finished = Label(master, text=end_text, font=("Georgia",16))
    match_finished.pack()

def winner(player):
    winner.destroy()
    error.destroy()
    if player == server:
	server.winners().append(1)
	receiver.winners().append(0)
	server.errors().append(0)
	receiver.errors().append(0)
    elif player == receiver:
	receiver.winners().append(1)
	server.winners().append(0)
	receiver.errors().append(0)
	server.errors().append(0)

def error(player):
    winner.destroy()
    error.destroy() 
    if player == server:
	server.errors().append(1)
	server.winners().append(0)
	receiver.errors().append(0)
	reciever.winners().append(0)
    elif player == receiver:
	receiver.errors().append(1)
	receiver.winners().append(0)
	server.errors().append(0)
	server.winners().append(0)

def server_outcome():
    server_won.destroy()
    server_lost.destroy()
    global winner
    global uf_error
    global f_error
    winner = Button(master, text="Winner", command=winner(server))
    error = Button(master, text="Unforced error", command=error(receiver))
    winner.pack()
    error.pack()
    
def receiver_outcome():
    server_won.destroy()
    server_lost.destroy()
    global winner
    global error
    global f_error
    winner = Button(master, text="Winner", command=winner(receiver))
    error = Button(master, text="Unforced error", command=error(server))
    winner.pack()
    error.pack()

def fsi():
    first_serve.destroy()
    second_serve.destroy()
    double_fault.destroy()
    global server_won
    global server_lost
    server_won = Button(master, text="Server won", command=server_outcome)
    server_lost = Button(master, text="Server lost", command=receiver_outcome)
    server_won.pack()
    server_lost.pack()

def ssi():
    first_serve.destroy()
    second_serve.destroy()
    double_fault.destroy()
    global server_won
    global server_lost
    server_won = Button(master, text="Server won", command=server_outcome)
    server_lost = Button(master,text="Server lost", command=receiver_outcome)
    server_won.pack()
    server_lost.pack()

def df():
    first_serve.destroy()
    second_serve.destroy()
    double_fault.destroy()

def server_1():
    player_one.destroy()
    player_two.destroy()
    server = Player("player_1")
    receiver = Player("player_2)"

def server_2():
    player_one.destroy()
    player_two.destroy()
    server = Player("player_2")
    receiver = Player("player_1")
    
def choose_server():
    global player_one
    player_one = Button(master, text="Player 1", command=server_1())
    global player_two
    player_two = Button(master, text="Player 2", command=server_2())
    player_one.pack()
    player_two.pack()

def play_point():
    global first_serve
    first_serve = Button(master, text="First Serve", command=fsi)
    global second_serve
    second_serve = Button(master, text="Second Serve", command=ssi)
    global double_fault
    double_fault = Button(master, text="Double Fault", command=df)
    first_serve.pack()
    second_serve.pack()
    double_fault.pack()

def play_game():
    while (True):
	play_point()
	if (server.points == 4):
	    server.games += 1
	    server, receiver = receiver, server
	    break
        elif (receiver.points == 4):
            receiver.games += 1
	    server, receiver = receiver, server
      	    break

def start():
    start_match.destroy()
    choose_server_text = Label(master, text="Choose who serves first:")
    choose_server_text.pack()
    choose_server()
    while (True):
	play_game()
        if (server.games == 6):
	    match_finished(server)
	    break
        elif (receiver.games == 6):
            match_finished(receiver)
	    break

global start_match
start_match = Button(master,text="Start Match", command=start)
start_match.pack()

mainloop()
