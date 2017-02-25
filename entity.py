import random
import file_manager


class Entity:

    name = ""
    health = 0
    attack = 0
    defence = 0
    money = 0

    file_stuff = file_manager.FileManager()

    def attack_target(self, thing_being_attacked):
        roll = self.dice_roll(20)
        print("{} rolled a {}".format(self.name, roll))
        if roll >= 15:
            damage = self.attack * 2 - thing_being_attacked.defence
            thing_being_attacked.set_health(thing_being_attacked.health - damage)
            print("{} hit doing critical damage of {}".format(self.name, damage))
        elif roll < 15 and roll >= 10:
            damage = self.attack - thing_being_attacked.defence
            thing_being_attacked.set_health(thing_being_attacked.health - damage)
            print("{} hit doing damage of {}".format(self.name, damage))
        if roll >=5 and roll <10:
            print("{} missed!".format(self.name))
            if roll < 5:
                damage = self.attack * 2 - thing_being_attacked.defence
                self.set_health(self.health - damage)
                print("{} missed and hit themselves dealing {} damage".format(self.name, damage))

    def get_health(self):
        return self.health

    def set_health(self, number):
        self.health = number


    def dice_roll(self, sides):
        return random.randrange(1, sides)

    def check_if_alive(self):
        if self.health <= 0:
            print("{} DIED!".format(self.name))
            return False
        else:
            print("{} health is {}".format(self.name, self.health))
            return True

class Hero(Entity):

    def __init__(self, file_name):
        character_data = self.file_stuff.get_json(file_name)
        self.name = character_data["name"]
        self.health = character_data["health"]
        self.level = character_data["level"]
        self.attack = character_data["attack"]
        self.defence = character_data["defence"]
        self.money = character_data["money"]

    def level_up(self):
        level_splice = int(self.level[-1])
        level_splice += 1
        self.level = "level {}".format(level_splice)
        self.attack += 5
        self.defence += 5

    def save(self):
        data = {
            "name": self.name,
            "attack": self.attack,
            "defence": self.defence,
            "level": self.level,
            "health": self.health,
            "money": self.money
        }
        self.file_stuff.write_to_json("json/{}.json".format(self.name), data)



class Enemy(Entity):

    def __init__(self):
        enemy_data = self.file_stuff.get_json("json/enemies.json")
        enemy_list = []
        for key in enemy_data["enemies"]:
            enemy_list.append(key)
        random_enemy = random.randrange(len(enemy_list))
        self.name = enemy_list[random_enemy]
        self.health = enemy_data["enemies"][self.name]["health"]
        self.attack = enemy_data["enemies"][self.name]["attack"]
        self.defence = enemy_data["enemies"][self.name]["defence"]
