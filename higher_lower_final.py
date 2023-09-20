from high_low_game_data import data
from high_low_art import logo, vs
import os
import random

def chose_account():
    return random.choice(data)
    
def format_data(account):

    acc_name = account["name"]
    acc_description = account["description"]
    acc_country = account["country"]

    return f"{acc_name}, {acc_description}, {acc_country}"

def comparison(chose, a_acc, b_acc):
    if a_acc>b_acc:
        return chose == 'a'
    else:
        return chose == 'b' 
    

def game():
    print(logo)
    score = 0
    game_should_continue = True

    acc_a = chose_account()
    acc_b = chose_account()

    while game_should_continue == True:
        acc_a = acc_b
        acc_b = chose_account()

        while acc_a == acc_b:
            acc_b = chose_account()

            print(f"Compare A: {format_data(acc_a)}")
            print(vs)
            print(f"Compare B: {format_data(acc_b)}")

            guess = input("who has more followers A or B: ").lower()

            a_followers_count = acc_a["follower_count"] 
            b_followers_count = acc_b["follower_count"] 
            is_true = comparison(guess, a_followers_count, b_followers_count )

            os.system('cls')
            print(logo)
            if is_true:
                score += 1
                print(f"yes you are right. your final score is {score}")

            else:
                game_should_continue = False
                print(f"no you are incorrect. your final score is {score}")
game()
