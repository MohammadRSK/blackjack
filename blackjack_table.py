from tkinter import *
from design import *

root = Tk()
root.geometry('1280×720')
root.title('JimShapedCasinp - Blackjack')
root.configure(bg = background_color)
###***
# UI Frames
###***

#Player:
player_frame = Frame(root, bg = background_color, ** hightlight_frame_with_white )
player_frame.pack(side = BOTTOM, fill = X)

player_options_frame = Frame(player_frame, bg = background_color)
player_options_frame.pack(**pack_left_and_fill_y)

#Dealer:
dealer_frame = Frame(root, bg = background_color, **hightlight_frame_with_white)
dealer_frame.pack(side = TOP, fill = X)

dealer_cards_frame = Frame(dealer_frame, bg = background_color)
dealer_cards_frame.pack(side = TOP, fill = Y)

#Score Board:
scoreboard = Frame(root, bg = background_color, **hightlight_frame_with_white)
scoreboard.pack(side = LEFT, fill = Y)

dealer_score = Frame(scoreboard, bg = background color)
dealer_score.pack(side = TOP, fill = BOTH)

player_score = Frame(scoreboard, bg = background_color)
player_score.pack(side = BOTTOM, fill = BOTH)

player_score_label = Label(player_score, bg = background_color, text = 'Player Score: ', **button_args)
player_score_label.pack()

dealer_score_label = Label(dealer score, bg = background_color, text = 'Dealer Score: ', **button_args)
dealer_score_label.pack()
#score Board END

#player options in the deal:
deal = Button(player_options_frame, text = 'DEAL', * button_args, bg = "#34A3A")
deal.pack(**pack_left_and_fill_y)

hit = Button (player_options_frame, text = 'HIT', bg = '#FF3300', **button_args, state = DISABLED, name = 'hit')
  

stand = Button(player_options_frame, text = 'STAND', bg = '#F§EDID', **button_args, state = DISABLED, name = 'stand')

double = Button(player_options_frame, text = 'DOUBLE', bg = '#ccooce', **button_args, state = DISABLED, name = 'double')

split = Button(player_options_frame, text = 'SPLIT', bg = '#66FFFF', **button_args, state = DISABLED, name = 'split')

hit.pack(side    = TOP, fill = x)
stand.pack(side  = TOP, fil1 = x)
double.pack(side = TOP, fill = X)
split.pack(side  = TOP, fill = x)
#player options END

#Deal a game:
def deal_init()
###
#Clean plauer frame from the hit cards:
###
#Initialize Card Instances so this way i will have a new deck each time deal is pressed
cards_instances = []
for card in collect_cards():
cards_instances.append(Card(name = card)
print (f'{card} added to deck')

#set the Buttons click function ‹Button-1> Stand for left click

#hit.bind()
#stand.bind()

deal.bind('<Button-1>', lambda event: deal_init())




root.mainloop()

