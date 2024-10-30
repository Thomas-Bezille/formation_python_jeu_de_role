import random
import sys

ATTACK = "1"
POTION = "2"

life_player = 50
life_enemy = 50

potion_player = 3

skip_next_round = False

print(f"\n{"/" * 20}{"-" * 5} JEU DE ROLE {"-" * 5}{"/" * 20}")

while True:
    if skip_next_round == False:
        action_player = input("\nSouhaitez-vous attaquer ⚔️  (1) ou utiliser une potion 🧪 (2) ? >>> ")
        
        if action_player != ATTACK and action_player != POTION:
                print("Sasissez (1) pour attaquer ⚔️  ou (2) pour utiliser une potion 🧪")
                continue
        
        if action_player == ATTACK:
            power = random.randint(5, 10)
            life_enemy -= power
            print(f"Vous avez infligé {power} points de dégats à l'ennemi ⚔️")
        
        if action_player == POTION and potion_player > 0:
            heal = random.randint(15, 20)
            life_player += heal
            potion_player -= 1
            print(f"Vous avez récupérer {heal} points de vie ❤️ ({potion_player} restante(s))")
            skip_next_round = True
        elif action_player == POTION and potion_player <= 0:
            print("Vous n'avez plus de potion...")
            continue
    else:
        print("Vous passez votre tour... 💤")
        skip_next_round = False
    
    # Enemy Attack (He can only attack, he has no potion)
    power = random.randint(5, 15)
    life_player -= power
    print(f"L'ennemi vous a infligé {power} points de dégats ⚔️")
    
    # Resume
    print(f"Il vous reste {life_player} points de vie.")
    print(f"Il reste {life_enemy} points de vie à l'ennemi.")
    print("-" * 50)