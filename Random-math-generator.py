
from time import time
import random
from random import randint
score=0
amount=int(input("How many questions would you like to answer? : "))
rounds=amount
operators=["+","-","*","/"]
start=time()
for i in range(amount):
    operator=random.choice(operators)
    rand1=randint(10,1000)
    rand2=randint(10,1000)
    if operator== "-":
        rand2 = randint(0,rand1)
    elif(operator=="/"):
        rand2=randint(1,10)
        rand1=rand2*randint(1,1000)
    elif(operator=="*"):
        rand2=randint(1,9)
    
    
    problem=str(rand1)+operator+str(rand2)
    print(problem)
    
    answer=int(input("enter your answer : "))
    correctAnswer = eval(problem)

    if answer==correctAnswer:
        print("The answer is correct")
        score+=1
        rounds-=1
        print("You have to answer",amount,"questions. You have",rounds,"left. Your score currently is", score, ".")
    else:
        print("The answer is incorrect")
        rounds-=1
        print("You have to answer",amount,"questions. You have",rounds,"left. Your score currently is", score, ".")

end = time()

time_taken = round(end-start)

print("It took you",time_taken , "seconds to answer all the questions")
