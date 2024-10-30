import random
import sys

ATTACK = "1"
POTION = "2"

life_player = 50
life_enemy = 50

potion_player = 3

print("\n//////////----- JEU DE ROLE -----//////////")

while life_player > 0 or life_enemy > 0:
    action_player = input("\nSouhaitez-vous attaquer ⚔️  (1) ou utiliser une potion 🧪 (2) ? >>> ")
    if action_player != ATTACK and action_player != POTION:
        print("Sasissez (1) pour attaquer ⚔️  ou (2) pour utiliser une potion 🧪")
    
    if action_player == ATTACK:
        power = random.randint(5, 10)
        life_enemy -= power
        print(f"Vous avez infligé {power} points de dégats à l'ennemi ⚔️")
        print(life_enemy)