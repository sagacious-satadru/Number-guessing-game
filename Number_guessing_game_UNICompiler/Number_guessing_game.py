from math import ceil
import random


even_odd_calls = False
hint_count = 0
multiple_hint_count = 0 
# Even_odd_hint2 = False
quality_flag = False

def even_odd(secret : int,guess : int)->None:
    """
    If the guessed no is even, but the secret no an odd one, then let the user know that they should guess an odd no, 
    OR vice versa
    """
    
    if guess % 2 == 0 and secret %2!=0:
        print("The secret number is an odd number.")
    elif guess %2!=0  and secret %2==0:
        print("The secret number is an even number.")

def even_odd2(secret : int)->None:
    """
    Function to check whether the secret no is even or odd
    """
    
    if secret % 2 == 0:
        print(f"The random number is an even number")
    else:
        print("The random number is an odd number")

def multiple_hint_func(secret,num,num2):
    global even_odd_calls    
    multiple_hint = 0    
    for i in range(num,num2+1):
        if secret % i == 0 and i!=secret and i!=1:
            multiple_hint = i
            
            if multiple_hint != 0:
                print(f"The random number is a multiple of {multiple_hint}")
                return multiple_hint
            break
        else:
            # if not Even_odd_hint2:
            if not even_odd_calls:
                even_odd2(secret)
                even_odd_calls = True
                return
                # Even_odd_hint2 = True
            # else:
                # print("Even odd hint already given. Please think accordingly")



flag = True
while flag:
    num = (input("Enter the lower bound for guessing : "))
    num2 = input("Enter the upper bound for guessing : ")
    score = input("Enter the score with which you'd like to begin : ")
    num.strip()
    num2.strip()
    score.strip()
    if num.isdigit() and score.isdigit() and num2.isdigit():
        print("Let us begin : ")
        num = int(num)
        num2 = int(num2)
        score = int(score)
        flag = False
    else:
        print("Invalid input!")

secret = random.randint(num, num2)

guess = None  # initially the guess is None because we haven't made any guess yet

count = 1  # the no of tries it took to guess the random number correctly

# midpoint_lb = ceil((((abs(num2-num)/2)) - num)/2 )
# midpoint_ub = ceil(abs((((abs(num2-num)/2)) - num2)/2) )

hint_list = [1]


while guess != secret:  # and (score != 0)    
    guess = input(f"Please type a number between {str(num)} and {str(num2)} : ")
    if guess.isdigit():  # it is essential to check whether the input given by the user was a digit or not
        # since if the input was not a numeric digit (1,2,3,...) then we can't convert it to int type.
        # For eg if input = "hello" (the string hello), then we can't convert it to an integer, so we need to check beforehand
        guess = int(guess)
        guess_quality_check = abs(secret - guess)/abs(num - num2) 

        # if guess > num or guess < 1:
        #     print("Your guess is out of the selected range")
        #     count += 1
        #     # continue
        # else:
        #     continue
        if guess == secret:
            print("Congratulations! you guessed the correct number")
        else:
            if guess > num2 or guess < num:
                print("Your guess is out of the selected range")
            print("Please try again")
            count += 1
            score -= 1
            if even_odd_calls == False and hint_count!=0:
                even_odd(secret,guess)
                even_odd_calls = True
            
            if guess_quality_check < 0.5:
                print("You're close to the random number")
                hint_count += 1
            else:
                print("You're far away from the random number")
                hint_count += 1
            if guess_quality_check < hint_list[0]:
                hint_list[0] = guess_quality_check
                if quality_flag == True and hint_list[0]!=1:
                    print("You're closer to the random number, compared to your previous guess")
                    hint_count += 1
                else:
                    quality_flag = True
            elif guess_quality_check == hint_list[0]:
                print("Your current guess is same as your previous guess")
                hint_count += 1
            else:
                print("You're farther away from the random number compared to your previous guess")
                hint_count += 1
            the_multiple = 0
            if hint_count > 0:
                # if multiple_hint_count == 0:
                the_multiple = multiple_hint_func(secret,num,num2)
                multiple_hint_count += 1
                hint_count += 1
                if multiple_hint_count > 0:
                    if the_multiple != 0 and (the_multiple is not None):
                        the_multiple2 = multiple_hint_func(secret,the_multiple,num2)
                        hint_count += 1
                    else:
                        continue                   

                                 
                

            
print(f"It took you, {count} guesses in total! ")
print(f"Your final score is {score}")






