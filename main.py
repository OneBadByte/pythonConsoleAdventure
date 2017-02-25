import file_manager
import store
import entity
import time
import json

file_stuff = file_manager.FileManager()
game_is_running = True

filer = file_manager.FileManager()


def opening_screen():
    print("Welcome")
    print()
    print("what do you want to do?\nfor new game type new\nto load game type load\nTo quit type quit")
    running = True
    while running:
        user_input = input()
        if user_input == "new":
            return character_creator()
        elif user_input == "load":
            while True:
                character_name = input("what is your characters name: ")
                file_exists = filer.check_if_file_exists("json/{}.json".format(character_name))
                if file_exists == True:
                    return "json/{}.json".format(character_name)
                else:
                    print("that character doesn't exist try again!")
                    continue
        elif user_input == "quit":
            game_is_running = False
            return game_is_running
        else:
            continue


def character_creator():
    name = input("enter characters name: ")
    data = {
        "name": name,
        "attack": 30,
        "defence": 15,
        "level": "level 1",
        "health": 100,
        "money": 0

    }
    filer.write_to_file("json/{}.json".format(name), json.dumps(data))
    return "json/{}.json".format(name)

def level_1(file_name):
    player = entity.Hero(file_name)
    enemy = entity.Enemy()
    while True:
        print()
        #player.check_if_alive()
        #enemy.check_if_alive()
        player.attack_target(enemy)
        enemy.attack_target(player)
        if enemy.check_if_alive() == False or player.check_if_alive() == False:
            player.level_up()
            player.save()
            break
        time.sleep(3)

def level_2(file_name):
    player = entity.Hero(file_name)
    enemy = entity.Enemy()
    while True:
        print()
        # player.check_if_alive()
        # enemy.check_if_alive()
        player.attack_target(enemy)
        enemy.attack_target(player)
        if enemy.check_if_alive() == False or player.check_if_alive() == False:
            player.level_up()
            player.save()
            break
        time.sleep(3)

def level_3(file_name):
    player = entity.Hero(file_name)
    enemy = entity.Enemy()
    while True:
        print()
        # player.check_if_alive()
        # enemy.check_if_alive()
        player.attack_target(enemy)
        enemy.attack_target(player)
        if enemy.check_if_alive() == False or player.check_if_alive() == False:
            player.level_up()
            player.save()
            break
        time.sleep(3)

file_name = opening_screen()
while game_is_running:
    level_to_start = filer.get_json(file_name)["level"]
    if level_to_start == "level 1":
        level_1(file_name)
    elif level_to_start == "level 2":
        level_2(file_name)
    elif level_to_start == "level 3":
        level_3(file_name)
    else:
        game_is_running = False
