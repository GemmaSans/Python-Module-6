#!/usr/bin/env python3

from alchemy import potions


if __name__ == "__main__":
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    str_pot = potions.strength_potion()
    print(f"Testing strength_potion: {str_pot}")
    heal_pot = potions.healing_potion()
    print(f"Testing healing_potion: {heal_pot}")
