import random
import sys

ATTACK = "1"
POTION = "2"

life_player = 50
life_enemy = 50

potion_player = 3

skip_next_round = False

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
    
    if action_player == POTION and potion_player > 0:
        heal = random.randint(15, 20)
        life_player += heal
        potion_player -= 1
        print(f"Vous avez récupérer {heal} points de vie ❤️ ({potion_player} restante(s))")
        skip_next_round = True
        print(life_player)
    elif potion_player <= 0:
        continue