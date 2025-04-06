import random

def equation_gen():

    '''
    This code will ask the user 5 maths questions and 
    at the end will give a score out of 5.
    '''
    unknown_x = random.randint(1, 10) # Code for x
    coef_a = random.randint(1, 10) # Code for equation
    result = coef_a * unknown_x # Answer
    return f"{coef_a} * x = {result}", unknown_x

score = 0 # This tracks the correct answers

print ("Welcome to the maths quiz")

for i in range(5): # Ask 5 questions
    equation, correct_x = equation_gen() # Equation 
    print("Solve the equation " + equation) # Print the question and equation
    user_input = int(input("What does x = ")) # Question box to input answer
    if user_input == correct_x:
        print("Correct!")
        score+=1
    else:
         print("Incorrect!")
print(f" You got {score} out of 5 correct!") # Overall score