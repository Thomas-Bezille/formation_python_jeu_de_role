import random
import sys

life_player = 50
life_enemy = 50

potion_player = 3

print("//////////----- JEU DE ROLE -----//////////")

while life_player > 0 or life_enemy > 0:
    action_player = input("\nSouhaitez-vous attaquer ⚔️ (1) ou utiliser une potion 🧪 (2) ? >>> ")