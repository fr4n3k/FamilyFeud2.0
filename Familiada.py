import random
from os import listdir, getcwd
from os.path import isfile, join, dirname, abspath


def number_of_players():#zwraca nam TYLKO 1 liczbe<!!!!!
    verify=True
    while verify:
        no_of_players=int(input("What's the number of players? (2 - 4): "))
        if no_of_players in range(1,5):
            print(" ")
            verify=False
        else:
            continue
    return no_of_players


def nick(players):#zwraca nam graczy
    nickname=[]
    for i in range(players):
        name=input("Enter a nickname: ")
        nickname.append(name)
    return nickname


def print_players(list_of_players):
    
    for index, nick in enumerate(list_of_players):
        print("Player no", index + 1, "is: ", nick)#


def number_of_rounds():

    while True:
        rounds=int(input("How many rounds would you like to play? (1 - 5): "))
        if rounds in range(1,6):
            print(" ")
            return rounds
        else:
            continue


def read_file():
    
    file_directory = dirname(abspath(__file__))
    categories = [file for file in listdir(file_directory+'/Categories/') 
                if isfile(join(file_directory+'/Categories/', file))]
    lista =[]
    current_category = random.choice(categories)
    text = open(join(file_directory+'/Categories/', current_category)).read()
    lines = text.split('\n')
    for line in lines:
        lista.append(line)
    del lista[-1]

    lista_question_answer = []
    for item in lista[:]:
        lista_question_answer.append(item.split(','))
    current_game_answers = {}
    for i in range (0, len(lista_question_answer)):
        current_game_answers[lista_question_answer[i][0]]= lista_question_answer[i][1]
    category_name = current_category.rstrip('.txt')
    return [category_name, current_game_answers]


def create_table() -> list:
    ''' create_table prints an empty table of 10 answers and returns it'''

    row=["----------", "---"].copy()
    answers_table =[]
    for i in range(10):
        answers_table.append(row.copy())
    # for index, row in enumerate(answers_table):
    #     print(index+1, "  ".join(row))    
    return answers_table


def game_question(category_and_answers) -> list:

    print (category_and_answers[0])
    answer=input("Your answer is: " )
    if answer in category_and_answers[1].keys():
        # print(category_and_answers[1], category_and_answers[1][answer])
        list_answer_score =[answer, category_and_answers[1][answer]]
        
    else:
        list_answer_score=["Wrong answer", 0]

    return list_answer_score
    

def change_table(game_table, answer_score):
    
    which_element=10-int(answer_score[1])

    if which_element in range(0, 10):
        game_table[which_element]=answer_score
        for index, row in enumerate(game_table):
            print(index+1, "  ".join(row))
    else:
        print("wrong answer")
        print("X   X\n X X \n  X  \n X X \nX   X")
        #print("X","","","X")
        #print("","","X","")
        #print("X","","","X")        

    return game_table


def mix_players(players_list):
    temp_players=list(players_list)
    random.shuffle(temp_players)
    print("List of players: ",  temp_players)
    return temp_players


def players_and_points(players_list):
    dict_player_point = {}
    for player in players_list:
        dict_player_point[player] = 0
    return dict_player_point


def score_table(players_score: dict):

    width=21
    print("="* width)
    print("| nickname | points |")
    #print("-"* width)
    list_score = []
    for player, score in players_score.items():
        list_score.append((player, score))
    for item in list_score:
        print("-"* width)
        print ("|",item[0], "|",item[1])     
    print("-"* width)


def game():

    
    rounds= number_of_rounds()
    
    
    how_many_players = number_of_players()
    list_of_playing_people = nick(how_many_players)
    print_players(list_of_playing_people)
    points = players_and_points(list_of_playing_people)
    

    for round in range(rounds):
        print('====================')
        print('round',round + 1)
        category_answers = read_file()
        current_game_table = create_table()
        players_list=mix_players(list_of_playing_people)

        for player in players_list:
            print('--------------------')
            print(player, 'is answering:')
        
            players_answer = game_question(category_answers)
            change_table(current_game_table, players_answer)
            points[player] += int(players_answer[1])
            print(f"Player {player} has {points[player]} points")
        
        score_table(points)

    winner = max(points.values())
    for player in points.keys():
        if points[player] == winner:
            print(f"{player} has won!")


game()

