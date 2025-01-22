import random
import time 

def arithmetic(level):
    mistakes=0
    start_time=time.time()  
    for problem in range(1, level*3 +1):  #  3 additional questions per level
        if time.time()-start_time>60:  # 1 minute time limit per level
            print("Game Over, you made it to level " + str(level) + " and answered " + str(problem-1) + "/" + str(level*3) + " problems")
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
        answer=int(input())  #  need to implement error catching for when input includes a character that is not an interger like "("
        ###
        ###
        ###

        while answer!=correct_answer:
            answer=int(input())  # repeatedly prompts player for answer until correct
            mistakes+=1
            start_time-=5  # time penalty for wrong answer
    
    
    total_time=time.time()-start_time
    print("You beat level " + str(level)+ " in " + str(total_time) + " seconds with " + str(mistakes) + " mistake(s)")   
    if total_time<60:  # new level
        return arithmetic(level+1)
    

    return "Game Over!"

arithmetic(1)
