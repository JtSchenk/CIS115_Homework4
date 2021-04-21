from random import *

num_sticks = 20 #Start with 20 sticks
current_player = 2

def not_quite_right(num_sticks):
    if((0 <= num_sticks and num_sticks < 20)):
        random_num = randint(1,10)
        print(random_num)
        if(1 <= random_num and random_num <= 3):
            new_sticks = randint(1,4)
            num_sticks = new_sticks + num_sticks
            print("{} stick(s) added. {} sticks remain.".format(new_sticks, num_sticks)) 
        else:
            print("No sticks added. {} sticks remain.".format(num_sticks))
    return num_sticks      


#find out a way to keep the line going
def display_board(num_sticks):
    for x in range(1, num_sticks+1):
        print("|", end= " ")
    for x in range(1, num_sticks+1):
        print(x, end= " ")


def take_sticks(current_player, num_sticks):
    remove_sticks = 5 # set so the while loop works.
    while(remove_sticks > 3):
        print("Input a valid number to remove sticks. (1) (2) (3)")
        remove_sticks = int(input("\nPlayer {}, how many sticks do you pickup? ".format(current_player)))
    num_sticks = num_sticks - remove_sticks
    return num_sticks

#not_quite_right(num_sticks)
#display_board(num_sticks)
take_sticks(current_player, num_sticks)
#def display_summary(player_number, sticks_taken, sticks_added, num_sticks):

#def main():