from random import *

num_sticks = 20 #Start with 20 sticks

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


not_quite_right(num_sticks)