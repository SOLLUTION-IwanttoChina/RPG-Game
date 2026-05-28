#healthPoint-HP
import sys
import random
player_hp = 100
enemy_hp = 100
attack_damage = 25
heal_amount = 20
attack_fromtheenemy = 25
enemy_hill= 15

print("_-_=Welcome to the fight simulator=_-_")
print("You need to defeat your opponent in 5 levels.")
print(f"your HP: {player_hp} | enemys HP {enemy_hp}")
try:
    print("select action")
    print("1=attack the enemy")
    print("2=cure yourself")
    user_choise = int(input("enter the number 1 or 2: "))
    if user_choise == 1:
        enemy_hp = enemy_hp - attack_damage
        print(f"Result: You attacked the enemy and dealt {attack_damage} damage!")
        print(f"enemy health now {enemy_hp}")
    elif user_choise == 2:
        player_hp = player_hp + heal_amount
        print(f"You restored {heal_amount} your HP ")
        print(f"you have {player_hp} HP")
    else:
        print ("error wrong character")
except ValueError:
    print ("ERORR: only numbers, no letters ")

print("next lvl  1: ")

try:
    print("the enemy is attacking you")
    print("select action")
    print("1=dodge to the left")
    print("2=dodge to the right")
    user_choise = int(input("enter the number 1 or 2: "))
    attack_enemy = random.randint(1, 2)
    if user_choise == attack_enemy:
        print("Well done, you managed to dodge!")
    elif user_choise != attack_enemy:
        player_hp= player_hp - attack_fromtheenemy
        print("the enemy hit you")
        print(f"You have {player_hp} HP")
    else:
        print("error wrong character")
except ValueError:
    print ("ERORR: only numbers, no letters ")

print("next lvl 2: ")

print("You've gained access to the bonus, but your opponent has become more dangerous!")
try:
    print("select bonus")
    print("1=knife")
    print("2=unknown")
    user_choise = int(input("enter the number 1 or 2: "))
    if user_choise == 1:
        print("You got a knife! You get bonus damage.")
        attack_damage = attack_damage + 10
        attack_damage = 35
        print(f"You attack damage {attack_damage}")
    elif user_choise == 2:
        print("You got a katana! Your damage has increased significantly!")
        attack_damage = attack_damage + 15
        attack_damage = 40
        print(f"You attack damage {attack_damage}")
    else:
         print("error wrong character")
except ValueError:
    print ("ERORR: only numbers, no letters ")

print("next lvl: 3")
try:
    print("choose next action")
    print("1=normal attack")
    print("2=risky combo")
    print("3=point combo")
    user_choise = int(input("enter the number 1,2 or 3: "))
    dodg = random.randint(1, 2)
    print ("choose the place of impact")
    user_choise_place = int(input("enter the place 1-left or 2-right, ONLY NUMBER: "))
    if dodg == user_choise_place:
        if user_choise == 1:
            enemy_hp = enemy_hp - attack_damage
            print(f"Result: You attacked the enemy and dealt {attack_damage} damage!")
            print(f"enemy health now {enemy_hp}")
        elif user_choise == 2:
            combo = random.randint(1, 50)
            enemy_hp = enemy_hp - combo
            print(f"Result: You attacked the enemy and dealt {combo} damage!")
            print(f"enemy health now {enemy_hp}")
        elif user_choise == 3:
            enemy_hp = enemy_hp - 10
            print(f"Result: You attacked the enemy and dealt 10 damage!")
            print(f"enemy health now {enemy_hp}")
            print("your spot combo is very bad!")
        else:
             print("error wrong character")
    elif dodg != user_choise_place:
        print("your opponent was able to dodge")
    else:
        print("error wrong character")
except ValueError:
    print ("ERORR: only numbers, no letters ")
attack_fromtheenemy = 60
try:
    print("next lvl 4:")
    print ("Your opponent is attacking you he use combo, dodge his blow.")
    print("select action")
    print("1=dodge to the left")
    print("2=dodge to the right")
    user_choise = int(input("enter the number 1 or 2: "))
    attack_enemy = random.randint(1, 2)
    if user_choise == attack_enemy:
        print("Well done, you managed to dodge!")
    elif user_choise != attack_enemy:
        player_hp= player_hp - attack_fromtheenemy
        print("your opponent hit you with a combo, his combo is very strong!")
        print(f"You have {player_hp} HP")
    else:
        print("error wrong character")
except ValueError:
    print ("ERORR: only numbers, no letters ")
try:
    print("next lvl:5")
    print("choose next action")
    print("1=normal attack")
    print("2=risky combo")
    print("3=point combo")
    user_choise = int(input("enter the number 1,2 or 3: "))
    dodg = random.randint(1, 2)
    print("choose the place of impact")
    user_choise_place = int(input("enter the place 1-left or 2-right, ONLY NUMBER: "))
    if dodg == user_choise_place:
         if user_choise == 1:
            enemy_hp = enemy_hp - attack_damage
            print(f"Result: You attacked the enemy and dealt {attack_damage} damage!")
            print(f"enemy health now {enemy_hp}")
         elif user_choise == 2:
            combo = random.randint(1, 50)
            enemy_hp = enemy_hp - combo
            print(f"Result: You attacked the enemy and dealt {combo} damage!")
            print(f"enemy health now {enemy_hp}")
         elif user_choise == 3:
            enemy_hp = enemy_hp - 10
            print(f"Result: You attacked the enemy and dealt 10 damage!")
            print(f"enemy health now {enemy_hp}")
            print("your spot combo is very bad!")
         else:
            print("error wrong character")
    elif dodg != user_choise_place:
        print("your opponent was able to dodge")
    else:
        print("error wrong character")
except ValueError:
    print("ERORR: only numbers, no letters ")
if enemy_hp < 1:
    print("Well done! You won this short game!")
    print("Thanks for playing my game!")
    print("wait for my next games!")
elif enemy_hp > 0:
    print("You couldn't pass this extremely easy game, try again.")
    print(f"the enemy has {enemy_hp} HP left")
    print("Try to complete this game again!")
    print("Just remember that you need to complete this game in 5 levels.")
else:
    print("Error")
    print("An error occurred, we apologize, please try playing the game again!")