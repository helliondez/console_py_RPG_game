import entity_data
import sys
import os
import re
from entity import Player, Enemy

different_spieces = ' | '.join(entity_data.SPIECES_TYPES)
different_classes = ' | '.join(entity_data.CLASS_TYPES)

def main():
    # This is aded now?
    created_character = starting_character_creation()
    player_character = Player(created_character[0], created_character[1], created_character[2], created_character[3])
    player_character.printing_character()
    enemy_npc = Enemy('slime', entity_data.ENEMY_TYPES['slime'])
    print('\nBattle simulation now starting!\n')
    while True:
        user_choice = input('Attack or Escape?\n > ')
        if user_choice.lower() == 'attack':
            player_character.damage_application(enemy_npc)
        elif user_choice.lower() == 'escape':
            sys.exit()
        else:
            print('Invalid input')
            continue
        enemy_npc.damage_application(player_character)
        print(f'Your health: {player_character.health}    Enemy health: {enemy_npc.health}')

def starting_character_creation() -> list:
    # All questions get added here.
    questions = [
        f'What is you name?\n > ', 
        f'What kind of creature are you?\n{different_spieces}\n > ', 
        f'What kind of adventurer are you?\n{different_classes}\n > ',
        ]
    list_of_answers = []
    # For the use of making sure the loop is continued if all checks are not passed.
    confirmation_bool = True
    loop_count = 1
    
    for question in questions:
        while confirmation_bool:
            user_input = input(question)
            # This series of checks are for the questions variable. This can be better done but good enough.
            # Any new checks for any new questions in the questions variable go here.
            if not re.match("^[A-Za-z]*$", user_input) and loop_count == 1:
                print(f'{user_input} is an invalid name, only alphabetic characters can be use with no spaces.')
                continue
            elif not any( element in user_input.lower() for element in entity_data.SPIECES_TYPES) and loop_count == 2:
                print(f'{user_input.capitalize()} isn\'t one of the selectable spieces.')
                continue
            elif not any( element in user_input.lower() for element in entity_data.CLASS_TYPES) and loop_count == 3:
                print(f'{user_input.capitalize()} isn\'t one of the selectable classes.')
                continue
            else:
                user_input = user_input.capitalize()
                input_confirmation = confirmation_check(user_input)
                if input_confirmation == True:
                    list_of_answers.append(user_input.lower())
                    confirmation_bool = False
                else:
                    continue
            loop_count += 1
        confirmation_bool = True

    list_of_answers.append(entity_data.CLASS_TYPES[list_of_answers[2].lower()])
    return list_of_answers

def confirmation_check(user_input: str) -> bool:
    set_confirmation = False
    user_input = user_input.capitalize()
    check_input = input(f'{user_input} is correct?\n > ')
    match check_input:
        case 'yes' | 'y':
            set_confirmation = True
        case 'no' | 'n':
            pass
    return set_confirmation

if __name__ == '__main__':
    main()