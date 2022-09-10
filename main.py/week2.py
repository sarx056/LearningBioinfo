"""Week 2 - we will be learning event driven programming"""

import turtle

t = turtle.Turtle()
ts = t.getscreen()
t.shape('turtle')
t.color('yellow')
ts.bgcolor('black')

def move():
    t.forward(2)

def turn_left():
    t.left(90)

def turn_right():
    t.right(90)

def spin():
    for i in range(4):
        t.right(90)

ts.onkey(move,'space')
ts.onkey(turn_left, 'Left')
ts.onkey(turn_right, 'Right')
ts.onkey(spin, 's')
ts.listen()
turtle.done()


#steps in making event driven programming are
#first import
#make event handlers and helper functions
#register the handlers

'''note that the code following can be used in codeskulptor3 which has simplegui module in it 
and this pycharm doesnt and i tried downloading and it wont work lmao '''


'''lets first make a simple event driven programme
a timer that ticks every second once'''
import simplegui

'''event handler, is basically the function we wanna execute in our program'''
def tick():
    print('tick!')

'''register the handlers, 
and this is where we implement simplegui 
and tell what to do with the event and the handler'''

timer = simplegui.create_timer(1000, tick)

#start the timer
timer.start()


""" lets make a simple interactive calculator using simpleGUI"""
import simplegui

#here we are storing the data needed for the calculator
store = 3
operand = 15

#then we make event handlers for the calculator
def output():
    global store, operand
    print("store = ", store)
    print("operand = ", operand)

#this function swaps the values
def swap():
    global store, operand
    store, operand = operand, store
    output()

#for adding our values
def add():
    global store, operand
    store = store + operand
    output()

#for subracting our values
def sub():
    global store, operand
    store = store - operand
    output()

#lets create a frame
frame = simplegui.create_frame('calculator', 200, 200)

#registering our handlers
frame.add_button('print', output, 100)
frame.add_button('swap', swap, 100)
frame.add_button('add', add, 100)
frame.add_button('sub', sub, 100)

#start the frame
frame.start()


#the same thing but with a input option
import simplegui

store = 4
operand = 2


def output():
    global store, operand
    print("store = ", store)
    print("operand = ", operand)


def swap():
    global store, operand
    store, operand = operand, store
    output()


def add():
    global store, operand
    store = store + operand
    output()


def sub():
    global store, operand
    store = store - operand
    output()


def multi():
    global store, operand
    store = store * operand
    output()


def div():
    global store, operand
    store = store / operand
    output()


def enter(inp):
    global operand
    operand = int(inp)
    output()


frame = simplegui.create_frame('calculator', 400, 400)

frame.add_button('print', output, 100)
frame.add_button('swap', swap, 100)
frame.add_button('add', add, 100)
frame.add_button('sub', sub, 100)
frame.add_button('multiply', multi, 100)
frame.add_button('divide', div, 100)
frame.add_input('input', enter, 100)

frame.start()

import simplegui


# making a simple interactive program which says hello and bye
# first create the messages
message_1 = 'hello!'
message_2 = 'goodbye!'

def print_hello():
    """make the event handler for hello"""
    global message_1
    print(message_1)

def print_goodbye():
    """make the event handler for goodbye"""
    global message_2
    print(message_2)

# create frame
frame = simplegui.create_frame('greetings', 300, 300)

# add buttons
frame.add_button('click to say hi!', print_hello, 100)
frame.add_button('click to say bye!', print_goodbye, 100)

# start the event
frame.start()