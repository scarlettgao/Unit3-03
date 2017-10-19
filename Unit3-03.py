# Created by: Scarlett Gao
# Created on: Oct 2017
# Created for: ICS3U
# This program is for rock,paper and scissors

import ui

from numpy import random

computer_op = random.randint(1,3)

user_ans = None
computer_ans = None

if (computer_op == 1) :
     computer_ans = 'Rock'
elif (computer_op == 2):
     computer_ans = 'Paper'
elif   (computer_op == 3):
     computer_ans = 'Scissors'

def rock_touch_up_inside (sender):
    global user_ans 
    user_ans = str('Rock')
    check_answer()

def paper_touch_up_inside (sender):
    global user_ans
    user_ans = str('Paper')
    check_answer()
    
def scissors_touch_up_inside (sender):
    global user_ans
    user_ans = str('Scissors')
    check_answer()

def check_answer ():
    print(computer_ans)
    print(user_ans)
    
    if computer_ans == str('Rock') and user_ans == str('Rock'):
        view['output_label'].text = ("It's a tie!")
    elif computer_ans == str('Rock') and user_ans == str('Paper'):
        view['output_label'].text = ("You win")
    elif computer_ans == str('Rock') and user_ans == str('Scissors'):
        view['output_label'].text = ("You have lost")
    elif computer_ans == str('Paper') and user_ans == str('Paper'):
        view['output_label'].text = ("It's a tie!")
    elif computer_ans == str('Paper') and user_ans == str('Rock'):
    	  view['output_label'].text = ("You have lost")
    elif computer_ans == str('Paper') and user_ans == str('Scissors'):
        view['output_label'].text = ("You win")
    elif computer_ans == str('Scissors') and user_ans == str('Scissors'):
        view['output_label'].text = ("It's a tie!")
    elif computer_ans == str('Scissors') and user_ans == str('Paper'):
        view['output_label'].text = ("You have lost")
    elif computer_ans == str('Scissors') and user_ans == str('Scissors'):
        view['output_label'].text = ("You win!")

view = ui.load_view()
view.present('sheet')
