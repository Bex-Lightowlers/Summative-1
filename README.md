# Let's get Quizy! 
## Introduction
This quiz will test your math skills by asking 5 math multiplication questions. 
The game will randomly generate 5 maths questions, and you have to guess what the X is and input the missing numbers. 

Good Luck! 🍀

# User Guide
This game will help improve your maths and problem-solving skills by asking 5 randomly generated maths questions. 
At the end, you will be given a score out of 5. 

## Features
- Immediate feedback on your answers.
- Random generation of maths questions.
- Quick quiz for bite-sized learning.
- Easy to quit whenever you want.

## What you will need
You will need access to a computer with Python installed. 

To install Python follow the following links - 
   - Windows: Download from [python.org](https://www.python.org/downloads/windows/)
   - macOS: Download from [python.org](https://www.python.org/downloads/mac-osx/)

## How to play
- Run the game in the terminal by clicking this button in the top right corner. ![Run button](https://github.com/Bex-Lightowlers/Summative-1/blob/main/Run_button%202025-04-10%20135109.png)
- The questions will appear in the bottom terminal. Now start answering the math question.
- Input the answer in the answer box and press "Enter".
- You will be advised if it's correct or incorrect straight away.
- Answer all 5 questions.
- At the end, you will receive an overall score.

# Technical Documentation

## Summative 1 
This script runs maths equations. It includes the following:

- Using function `equation_gen()` to generate the equation:
  ```
  a * x = b
  ```
  The functions used are as below:
  ```
  def equation_gen():

    '''
    This code will ask the user 5 maths questions and 
    at the end will give a score out of 5.
    '''
    unknown_x = random.randint(1, 10) # Code for x
    coef_a = random.randint(1, 10) # Code for equation
    result = coef_a * unknown_x # Answer
    return f"{coef_a} * x = {result}", unknown_x
  ```
- It generates random numbers using `ramdom.randit(1, 10)` for a & x which equates to b. 
- Prompts the user to input their answer using `input()`
- Generates 5 questions using `i in range(5)`
- Provides immediate feedback if correct or incorrect by using `if-else` statement
- At the end, displaced overall score.

To clone the repository 
```
https://github.com/Bex-Lightowlers/Summative-1.git
```

