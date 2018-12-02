import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def main():
    print_intro()
    preference_list = ask_questions()
    print_drink(preference_list)


def print_intro():
    print("Let me set ye up with a drink.\n")


def ask_questions():
    preference_list = []
    for key in questions:
        invalid_answer = True;
        while invalid_answer:
            invalid_answer = False;
            answer = str(input(questions[key] + "[y/n]: "))
            print(answer)
            if answer == "y" or answer == "Y":
                preference_list.append(key)
            elif answer != "n" and answer != "N":
                invalid_answer = True
                print("Oi, ye didn't answer me question")

    return preference_list


def print_drink(preference_list):
    for i in preference_list:
        print(random.choice(ingredients[i]), end="")
        if i != preference_list[-1]:
            print(", ", end="")
    print()


if __name__ == "__main__":
    main()
