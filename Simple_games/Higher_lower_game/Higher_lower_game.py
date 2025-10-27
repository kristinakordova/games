import art 
import game_data 
import random

def choose_entries(data, second_entry):
    import random
    first_entry = second_entry
    second_entry = random.choice(data)
    if first_entry == second_entry:
        second_entry = random.choice(data)
    return first_entry, second_entry

def compare_scores(first_entry, second_entry):
    "takes user guess and checks if they got it right"
    follower_count_A =  first_entry["follower_count"]
    follower_count_B = second_entry["follower_count"]
    user_guess = str(input("Who has more followers? Type A or B")).lower()
    if follower_count_A > follower_count_B:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
def format_data(account):
    name= account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, from {country}."


def game(data, second_entry, score, should_contirnue):
    first_entry, second_entry = choose_entries(data, second_entry)

    print(logo)
    print(f"Current score {score}")
    print(f"Compare A: {format_data(first_entry)}")

    print(vs)
    print(f"Against B: {format_data(second_entry)}")

    is_correct = compare_scores(first_entry, second_entry)
    if is_correct:
        score +=1
        print(f"You are right! Current score {score}")
        return score, should_contirnue
    else:
        print(f"You are wrong! Final score {score}")
        should_contirnue = False
        return score, should_contirnue

data = game_data.data
logo = art.logo
vs = art.vs
score = 0
should_contirnue = True
second_entry = random.choice(data)

while should_contirnue:
    score, should_contirnue = game(data, second_entry, score, should_contirnue)
print("You were wrong, game over!")
