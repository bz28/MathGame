

# Game Instructions
###
###
# 1. Run game in terminal (great for airplane flights or when you don't have wifi).
# 2. Arithmetic problem will appear. Answer correctly for new question to appear.
# 3. If all questions on current level answered within time limit (60 seconds), you will move on to the next level.
# 4. Incorrect answers results in a 5 second time penalty.
# 5. Have fun!
###
###


# updates:
#         change to class structure for easier implementation
#         leaderboard
###

import random
import time 
def arithmetic(level):
    print("You are on Level " + str(level))
    print("#"*20)
    time.sleep(2) #  1 second to read message
    print("Game starts in 3 seconds, good luck!")
    print("#"*20)
    time.sleep(3)
    mistakes=0
    start_time=time.time()  
    for problem in range(1, level*3 +1):  #  3 additional questions per level
        if time.time()-start_time>60:  # 1 minute time limit per level
            print("Game Over!")
            print("#"*20)
            time.sleep(1)
            print("Time limit exceeded!")
            print("#"*20)
            time.sleep(1)
            print("You made it to level " + str(level) + " and answered " + str(problem-1) + "/" + str(level*3) + " problems")
            print("#"*20)
            print('Would you like to play again? Press y for yes, and n for no')
            play_again=input()
            while play_again not in ['n','y']:
                print('Invalid Response')
                play_again=input()
            if play_again=='y':
                for i in range(15):
                    print("#"*20)

                time.sleep(1)
                return arithmetic(1)
            return
        
        operations=['*','+','-', '/']
        random_operation=random.randint(0,3)
        x=random.randint(2,99)
        y=random.randint(2,99)

        correct_answer=None  # initializing correct answer

        if random_operation==0:
            while x*y>1000:  # ensures multiplication is not too difficult
                x=random.randint(2,99)
                y=random.randint(2,99)
            correct_answer=x*y

        elif random_operation==1:
            correct_answer=x+y

        elif random_operation==2:
            if y>x:  # ensures subtraction is not negative
                temp=x
                x=y
                y=temp
            correct_answer=x-y

        else:
            while y>x or x%y!=0 or x==y:
                x=random.randint(20,999)  # ensures division is not too easy
                y=random.randint(2,99)
            correct_answer=x//y

        # display question
        ###
        ###
        print(str(x) + operations[random_operation] + str(y))
        ###
        ###
        ###

        # Prompts player for answer input
        ###
        ###        
        answer=input()  
        while not answer.isdigit():
            print('Invalid answer, try again!')
            print('#'*20)
            answer=input()
        answer=int(answer)
        ###
        ###
        ###

        while answer!=correct_answer:
            print("Wrong answer, try again!")
            print('#'*20)
            answer=input()  # repeatedly prompts player for answer until correct
            while not answer.isdigit():
                print('Invalid answer, try again!') 
                print("#" *20)              
                answer=input()
            answer=int(answer)
            mistakes+=1
            start_time-=5  # time penalty for wrong answer
            if time.time()-start_time>60:  # 1 minute time limit per level
                print("Game Over!")
                print('#'*20)
                time.sleep(1)
                print("Time limit exceeded!")
                print('#'*20)
                time.sleep(1)
                print("You made it to level " + str(level) + " and answered " + str(problem-1) + "/" + str(level*3) + " problems")
                print('#'*20)
                print('Would you like to play again? Press y for yes, and n for no')
                play_again=input()
                while play_again not in ['n','y']:
                    print('Invalid Response')
                    play_again=input()
                if play_again=='y':
                    for i in range(15):
                        print("#"*20)

                    time.sleep(1)
                    return arithmetic(1)
                return
            
        print("Correct!")
        print('#'*20)
    
    
    total_time=time.time()-start_time
    time.sleep(1)
    print("You beat level " + str(level)+ " in " + str(total_time) + " seconds with " + str(mistakes) + " mistake(s)")   

    time.sleep(2)  # 2 second cooldown period
    for i in range(15):
        print("#"*20)
    time.sleep(1)

    if total_time<60:  # new level
        return arithmetic(level+1)
    
    print('#'*20)
    print("Game Over!")
    print('#'*20)
    time.sleep(1)
    print("Time limit exceeded!")
    print('#'*20)
    time.sleep(1)
    print("You made it to level " + str(level) + " and answered " + str(problem-1) + "/" + str(level*3) + " problems")
    print('#'*20)

    print('Would you like to play again? Press y for yes, and n for no')
    play_again=input()
    while play_again not in ['n','y']:
        print('Invalid Response')
        play_again=input()
    if play_again=='y':
        for i in range(15):
            print("#"*20)

        time.sleep(1)
        return arithmetic(1)
    return
    

arithmetic(1)
