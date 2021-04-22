from random import *

global start
start = True

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


def display_board(num_sticks):
    for x in range(1, num_sticks+1):
        if(x < 10):
            print("|", end= " ")
        else:
            print("| ", end= " ")
    print()
    for x in range(1, num_sticks+1):
        if(x < 10):
            print("|", end= " ")
        else:
            print("| ", end= " ")
    print()
    for x in range(1, num_sticks+1):
        if(x < 10):
            print("|", end= " ")
        else:
            print("| ", end= " ")
    print()
    for x in range(1, num_sticks+1):
        if(x < 10):
            print("|", end= " ")
        else:
            print("| ", end= " ")
    print()
    for x in range(1, num_sticks+1):
        print(x, end= " ")


def take_sticks(current_player, num_sticks):
    remove_sticks = int(input("\nPlayer {}, how many sticks do you pickup? ".format(current_player)))
    num_sticks = num_sticks - remove_sticks
    return num_sticks

def display_summary(current_player, remove_sticks, new_sticks, num_sticks):
    print("Player {} took {}, pictsie magic added {} back. There are {} sticks left".format(current_player, remove_sticks, new_sticks, num_sticks))

def main():
    if(start == True):
        num_sticks = 15 #Start with 20 sticks
        current_player = 1
        remove_sticks = 0
        new_sticks = 0
        start == False
    while(num_sticks != 0):
        not_quite_right(num_sticks)
        display_board(num_sticks)
        take_sticks(current_player, num_sticks)
        display_summary(current_player, remove_sticks, new_sticks, num_sticks)
        if(current_player == 1):
            current_player = 2
        else:
            current_player = 1

main()