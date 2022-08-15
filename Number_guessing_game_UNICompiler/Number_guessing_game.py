from math import ceil, sqrt
import random

even_odd_calls = False
hint_count = 0
multiple_hint_count = 0
# Even_odd_hint2 = False
quality_flag = False
prime_check_done = False
multiple_hint_given = False


def is_prime(n: int) -> bool:
    """

    :param n: the number which we wish to check if it is prime or not
    :return: a bool value : True if n is prime, False o/w
    """
    # Checking for corner case
    if n <= 1:
        return False

    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def even_odd(secret: int, guess: int) -> None:
    """
    If the guessed no is even, but the secret no an odd one, then let the user know that they should guess an odd no,
    OR vice versa
    """

    if guess % 2 == 0 and secret % 2 != 0:
        print("The random number is an odd number.")
    elif guess % 2 != 0 and secret % 2 == 0:
        print("The random number is an even number.")
    else:
        even_odd2(secret)


def even_odd2(secret: int) -> None:
    """
    Function to check whether the secret no is even or odd
    """

    if secret % 2 == 0:
        print(f"The random number is an even number")
    else:
        print("The random number is an odd number")


def multiple_hint_func(secret: int, num: int, num2: int) -> int:
    """

    :param secret: the secret number
    :param num: the lower bound
    :param num2: the upper bound
    :return: a number that'll let the user know what the secret number is a multiple of
    """
    global even_odd_calls
    global prime_check_done
    global multiple_hint_given
    multiple_hint = 0
    if is_prime(secret) and not prime_check_done:
        prime_check_done = True
        # multiple_hint_given = True
        print("The random number is a prime number")
        return 0
    else:
        # for i in range(num, num2 + 1):
        for i in range(num, secret):
            if i != 0:
                if secret % i == 0 and i != secret and i != 1:
                    multiple_hint = i
                    print(f"The random number is a multiple of {multiple_hint}")
                    multiple_hint_given = True
                    return multiple_hint
                    # break
                else:
                    if i == secret:
                        break
                    continue
    if multiple_hint == 0:
        if not even_odd_calls:
            even_odd2(secret)
            even_odd_calls = True
            multiple_hint_given = True
            return 0


flag = True  # a flag to keep asking the user for a valid i/p until they finally enter one
while flag:
    num = (input("Enter the lower bound for guessing : "))
    num2 = input("Enter the upper bound for guessing : ")
    score = input("Enter the score with which you'd like to begin : ")
    num.strip()
    num2.strip()
    score.strip()
    if num.isdigit() and score.isdigit() and num2.isdigit() and (int(num) < int(num2)):
        print("Let us begin : ")
        num = int(num)
        num2 = int(num2)
        score = int(score)
        flag = False
    else:
        print("Invalid input!")

secret = random.randint(num, num2)

guess = None  # initially the guess is None because the player hasn't made any guess yet

count = 1  # the no of tries it took to guess the random number correctly

hint_list = [] # a list made to store the quality of the player's guesses
the_multiple_list = [] # made a global multiple_hint_list to store the 'multiple of' hints given to the player

while guess != secret:  # and (score != 0)
    guess = input(f"Please type a number between {str(num)} and {str(num2)} : ")
    if guess.isdigit():  # it is essential to check whether the input given by the user was a digit or not
        # since if the input was not a numeric digit (1,2,3,...) then we can't convert it to int type.
        # For eg if input = "satadru" (the string satadru), then we can't convert it to an integer, so we need to check beforehand
        guess = int(guess)
        guess_quality_check = abs(secret - guess) / abs(num - num2)

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
                print("Your guess is out of the selected range. Please try again")
                count += 1
                score -= 1
                continue
            print("Please try again")
            count += 1
            score -= 1
            if even_odd_calls is False and hint_count != 0 and not multiple_hint_given:
                even_odd(secret, guess)
                even_odd_calls = True

            if guess_quality_check < 0.5:
                print("You're close to the random number")
                hint_count += 1
            else:
                print("You're far away from the random number")
                hint_count += 1
            if len(hint_list) == 0 or guess_quality_check < hint_list[-1]:
                # hint_list[0] = guess_quality_check
                hint_list.append(guess_quality_check)
                if quality_flag is True and (hint_list[-1] is not None):
                    print("You're closer to the random number, compared to your previous guess")
                    hint_count += 1
                else:
                    quality_flag = True
            elif guess_quality_check == hint_list[-1]:
                print("Your current guess is no better than your previous guess") # this happens when the current guess of the player is equidistant from the random number, relative to their previous guess
                hint_list.append(guess_quality_check)
                hint_count += 1
            else:
                print("You're farther away from the random number compared to your previous guess")
                hint_list.append(guess_quality_check)
                hint_count += 1
            the_multiple = 0
            if hint_count > 0 and multiple_hint_count == 0:
                # if multiple_hint_count == 0:
                the_multiple = multiple_hint_func(secret, num, num2)
                the_multiple_list.append(the_multiple)
                multiple_hint_count += 1
                hint_count += 1
                continue
            if multiple_hint_count > 0:
                if the_multiple_list[-1] != 0 and (the_multiple_list[-1] is not None):
                    the_multiple2 = multiple_hint_func(secret, the_multiple_list[-1] + 1, num2)
                    hint_count += 1
                else:
                    continue

print(f"It took you, {count} guesses in total! ")
print(f"Your final score is {score}")

