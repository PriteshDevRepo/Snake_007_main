#Development of Snake game
import random
import time


snake_body=[(9,10),(10,10),(11,10)]
print(snake_body)
board_width=(20,20)
new_head=snake_body[-1]
new_direction="right"
direction="right"
score=0;
#generation of food random coordinate
food_x = random.randint(0, board_width[0]-1)
food_y = random.randint(0, board_width[0]-1)
print("food cordinates:",(food_x,food_y))
while True:
    #==========================================================
    #Take input from user
    user_input=input("Enter a direction (up/down/left/right):")
    if user_input == "up":
        direction ="up"
    elif user_input == "down":
        direction="down"
    elif user_input == "left":
        direction ="left"
    elif user_input=="right":
        direction="right"
    else:
        print("Invalid Input!!! Please provide valid direction")
    
    #Move snake
    directions={'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    
    if direction == "up"and new_direction!="down":
        new_direction ="up"
        dx,dy= directions[new_direction]
        new_head=(new_head[0]+dx,new_head[1]+dy)
        snake_body.append(new_head)
        
    elif user_input == "down" and new_direction!="up":
        new_direction="down"
        dx,dy= directions[new_direction]
        new_head=(new_head[0]+dx,new_head[1]+dy)
        snake_body.append(new_head)
        
    elif direction == "left" and new_direction!="right":
        new_direction ="left"
        dx,dy= directions[new_direction]
        new_head=(new_head[0]+dx,new_head[1]+dy)
        snake_body.append(new_head)
        
    elif direction=="right" and new_direction!="left":
        new_direction="right"
        dx,dy= directions[new_direction]
        new_head=(new_head[0]+dx,new_head[1]+dy)
        snake_body.append(new_head)
    else:
        dx,dy= directions[new_direction]
        new_head=(new_head[0]+dx,new_head[1]+dy)
        snake_body.append(new_head)
        
    
    
    #append if food eat, remove last element if not eaten
    

    # food consuption
    if new_head==(food_x,food_y):
        #snake_body.append((food_x,food_y)) => Not needed
        score +=1
        print(snake_body)
        food_x = random.randint(0, board_width[0]-1)
        food_y = random.randint(0, board_width[0]-1)
    
    elif new_head!=(food_x,food_y):
        #check_collision self and walls
        #self
        snake_body.pop(0)
        print(snake_body)
        for i in snake_body[-1]:
            if i == new_head:
                print("Game over, tune khud ko khaaya sarkar")
                print("Your Score is",score)
                break

    #wall collision
        if new_head[0]>= board_width[0] or new_head[0]<=0 or new_head[1]>=board_width[1] or new_head[1]<=0:
            print("Game over wall collision ! :-[ !!");
            print("Your Score is",score)
            break