import random
import sys

# Player
player_hp = 100
player_defense = 0

def attack(enemy_hp):
    damage = random.randint(10, 20)
    enemy_hp -= damage
    print('====================\n'
          "You attack the enemy, dealing", damage, "damage.")
    return enemy_hp

def defend():
    global player_defense
    player_defense += 10
    print("You raise your shield, increasing your defense. (Damage reduced by 10)")

def dodge():
    dodge_chance = random.randint(0,8)
    if dodge_chance < 4:
        print("You swiftly move aside, successfully dodging the enemy's attack.")
        return True
    else:
        print("You attempt to dodge the enemy's attack but fail.")
        return False

def take_damage(damage):
    global player_hp, player_defense
    damage -= player_defense
    if damage > 0:
        player_hp -= damage
    else:
        print("You successfully block the enemy's attack.")

def recover():
    global player_hp
    recovered_hp = random.randint(20, 25)
    player_hp +=recovered_hp
    print("You recover", recovered_hp, "HP. Your HP is now", player_hp)
    return
    
    
# Bosses
bosses = [
    {'name': 'Godfrey', 'hp': 150, 'attack_damage': 20},
    {'name': 'Rennala', 'hp': 180, 'attack_damage': 25},
    {'name': 'Margit' , 'hp': 200, 'attack_damage': 30},
    {'name': 'MALENIA', 'hp': 250, 'attack_damage': 40}
]

def fight_boss(boss):
    global player_hp, player_defense

    print("You encounter", boss['name'] + ". They have", boss['hp'], "HP.")

    while player_hp > 0 and boss['hp'] > 0:
        print("\nYour HP:", player_hp)
        print(boss['name'] + "'s HP:", boss['hp'])
        print("What will you do? (ATTACK/DEFEND/DODGE/RECOVER)")

        move = input(">>> ")

        if move.lower() == "attack":
            boss['hp'] = attack(boss['hp'])
        elif move.lower() == "defend":
            defend()
        elif move.lower() == "dodge":
            dodge()
            continue  # continue to not take damage after dodge
        elif move.lower() == "recover":
            recover()
        else:
            print("Invalid move. You didn't do anything.")

        if boss['hp'] > 0:
            if move.lower() == "defend":  # Check if the player defended
                boss_damage = random.randint(10, boss['attack_damage'] - 10)
            else:
                boss_damage = random.randint(10, boss['attack_damage'])
                take_damage(boss_damage)
                print("The", boss['name'], "attacks you, dealing", boss_damage, "damage.")

    if player_hp > 0:
        print('\n' "Congratulations! You defeated", boss['name'] + "\n")
    else:
        print("YOU DIED.")
        sys.exit()


def show_instructions():
    print("Instructions:")
    print("You are in the Land Bettarnisheden.")
    print("You are one of the Tarnished, a group of exiles from the Lands Bettarnisheden who are summoned back after the war. The player must traverse the realm and fight to repair the Elden Ring and become the Elden Lord.")
    print('During each battle, you can choose to attack, defend, dodge, or recover.')
    print("Your HP starts at 1000. Defeat all bosses to win the game.")
    print("Good luck!\n")

def game_lore():
    print("+++Lore:+++")
    print("1. Godfrey was the first Elden Lord and husband of Queen Marika the Eternal. He was a mortal hero of legendary prowess who would become the first of the demigods, but after achieving his crowning victory, he lost his grace. He was then exiled from the Lands Bettarnisheden and became the very first Tarnished.")
    print("2. As a young astrologer who gazed at the night sky and always chased the stars, Rennala would encounter an enchanting full moon that would one day bewitch the Academy of Raya Lucaria.")
    print("3. Margit is an Omen who gained notoriety during The Shattering, in which he slaughtered countless champions who harbored ambitions for Lordship, stacking high their corpses during the Second Defense of Leyndell.")
    print("4. Malenia was born the child of Queen Marika the Eternal and her second husband, the Elden Lord Radagon. Both Malenia and Empyreans, meaning she has the potential to one day replace their mother as a new god of a coming age. But since Radagon and Marika were in fact the same person, Malenia was afflicted with the Scarlet Rot, unable to ever grow into adulthood.\n")

while True:
    print("welcome thee tarnished to text-elden ring\n")

    while True:
        print('=== Start Menu ===')
        print('1. Start')
        print('2. Instructions')
        print('3. Game Lore')
        print('4. Quit')
        print('===================')

        choice = input("Enter your choice: ")

        if choice == '1':
            fight_boss(bosses[0])
            fight_boss(bosses[1])
            fight_boss(bosses[2])
            fight_boss(bosses[3])
        elif choice == "2":
            show_instructions()
        elif choice == '3':
            game_lore()
        elif choice == '4':
            print("Thank you for playing!")
            sys.exit()
        else:
            print("Incorrect input. Please try again.")