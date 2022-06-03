from random import choice
character_list = {"R":"Rock","P":"Paper","S":"Scissors"}

print("Welcome to Rock Paper And Scissors Game")
print()

first_player_choice = input("""Choose one option between the following:
    "R" for "Rock",
    "P" for "Paper",
    "S" for "Scissors" : """)
print()

while(not(character_list.__contains__(first_player_choice.upper())) ):
    first_player_choice = input("""Invalid input. Try Again !!!
Choose one option between the following:
"R" for "Rock",
"P" for "Paper",
"S" for "Scissors" : """)
print()
second_player_choice = choice(list(character_list))

if(character_list[first_player_choice.upper()] == "Rock"): 
    if(character_list[second_player_choice.upper()] == "Paper"):
        print("""Player One (Rock) : CPU (Paper)
    Paper beats Rock. CPU Wins!!!""")
    elif(character_list[second_player_choice.upper()] == "Scissors"):
        print("""Player One (Rock) : CPU (Scissors)
    Rock beats Scissors. Player One Wins!!!""")
if(character_list[first_player_choice.upper()] == "Paper"): 
    if(character_list[second_player_choice] == "Rock"):
        print("""Player One (Paper) : CPU (Rock)
    Paper beats Rock. Player One Wins!!!""")
    elif(character_list[second_player_choice] == "Scissors"):
        print("""Player One (Paper) : CPU (Scissors)
    Scissors beats Paper. CPU Wins!!!""")
if(character_list[first_player_choice.upper()] == "Scissors"): 
    if(character_list[second_player_choice] == "Rock"):
        print("""Player One (Scissors) : CPU (Rock)
    Rock beats Scissors. CPU Wins!!!""")
    elif(character_list[second_player_choice] == "Paper"):
        print("""Player One (Scissors) : CPU (Paper)
    Scissors beats Paper. Player One Wins!!!""")

print()   
while(first_player_choice.upper() == second_player_choice):

    print("""Player One (%s) : CPU (%s) 
    It's a Tie""" %(character_list[first_player_choice.upper()], character_list[second_player_choice]))

    first_player_choice = input("""Choose one option between the following:
    "R" for "Rock",
    "P" for "Paper",
    "S" for "Scissors" : """)
    print()
    while(not(character_list.__contains__(first_player_choice.upper())) ):
        first_player_choice = input("""Invalid input. Try Again !!!
Choose one option between the following:
"R" for "Rock",
"P" for "Paper",
"S" for "Scissors" : """)
    second_player_choice = choice(list(character_list))
    print()

    if(character_list[first_player_choice.upper()] == "Rock"): 
        if(character_list[second_player_choice.upper()] == "Paper"):
            print("""Player One (Rock) : CPU (Paper)
    Paper beats Rock. CPU Wins!!!""")
        elif(character_list[second_player_choice.upper()] == "Scissors"):
            print("""Player One (Rock) : CPU (Scissors)
    Rock beats Scissors. Player One Wins!!!""")
    if(character_list[first_player_choice.upper()] == "Paper"): 
        if(character_list[second_player_choice] == "Rock"):
            print("""Player One (Paper) : CPU (Rock)
    Paper beats Rock. Player One Wins!!!""")
        elif(character_list[second_player_choice] == "Scissors"):
            print("""Player One (Paper) : CPU (Scissors)
    Scissors beats Paper. CPU Wins!!!""")
    if(character_list[first_player_choice.upper()] == "Scissors"): 
        if(character_list[second_player_choice] == "Rock"):
            print("""Player One (Scissors) : CPU (Rock)
    Rock beats Scissors. CPU Wins!!!""")
        elif(character_list[second_player_choice] == "Paper"):
            print("""Player One (Scissors) : CPU (Paper)
    Scissors beats Paper. Player One Wins!!!""")
    print()
